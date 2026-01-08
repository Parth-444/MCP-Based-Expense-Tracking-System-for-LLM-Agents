from fastmcp import FastMCP
import sqlite3
from pathlib import Path

DB_PATH = Path("expense.db")
CATEGORIES_PATH = Path(__file__).parent / "categories.json"
mcp = FastMCP(name="ExpenseTracker")

def initiate_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS expenses(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     date TEXT NOT NULL,
                     amount REAL NOT NULL,
                     category TEXT NOT NULL,
                     subcategory TEXT DEFAULT '',
                     note TEXT DEFAULT ''
                     )
                     """)
initiate_db()


@mcp.tool()
def add_expense(date, amount, category, subcategory ="", note= ""):
    '''add new expense entry to database'''
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.execute("INSERT INTO expenses (date, amount, category, subcategory, note) VALUES (?,?,?,?,?)",
        (date, amount, category, subcategory, note)
        )
        return {"status":"ok", "id":cur.lastrowid}


@mcp.tool()
def list_expenses(start_date, end_date):
    '''List all the expenses by date range'''
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.execute("SELECT * FROM expenses WHERE date BETWEEN ? AND ? ORDER BY id ASC", (start_date, end_date))
        cols = [d[0] for d in cur.description]
        return [dict(zip(cols, r)) for r in cur.fetchall()]
    
@mcp.tool()
def edit_expense(date, amount, category):
    """Edit an expense entry by category and date"""
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.execute(
            """
            UPDATE expenses
            SET amount = ?
            WHERE category = ?
              AND date = ?
            """,
            (amount, category, date)
        )
    return {"status": "ok", "rows_updated": cur.rowcount}


@mcp.tool()
def delete_expense(date, category):
    """Delete an existing expense"""
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.execute("DELETE FROM expenses WHERE date= ? AND category = ?", (date, category))
    return {"status": "ok", "rows_deleted": cur.rowcount}

# @mcp.resource("expense://categories", mime_type="application/json")
# def categories():
#     with open (CATEGORIES_PATH, "r", encoding="utf-8") as f:
#         return f.read()
@mcp.resource("expense://categories", mime_type="application/json")
def categories():
    try:
        return CATEGORIES_PATH.read_text(encoding="utf-8")
    except Exception as e:
        return f'{{"error": "{str(e)}"}}'



if __name__ == "__main__":
    mcp.run()