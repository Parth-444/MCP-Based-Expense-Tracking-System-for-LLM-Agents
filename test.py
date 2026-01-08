from fastmcp import FastMCP
import sqlite3
from pathlib import Path

DB_PATH = Path("expense.db")

def initiate_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS epenses (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     date TEXT NOT NULL,
                     amount REAL NOT NULL,
                     category TEXT NOT NULL,
                     subcategory TEXT DEFAULT '',
                     note TEXT DEFAULT '',
                     )
                     """)
initiate_db()


mcp = FastMCP(name="expense-tracker")

@mcp.tool
def add_expense(date, amount, category, subcategory ="", note= ""):
    '''add new expense entry to database'''
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.execute("INSERT INTO expenses (date, amount, category, subcategory, note), VALUES (?,?,?,?,?)",
        (date, amount, category, subcategory, note)
        )
        return {"status":"ok", "id":cur.lastrowid}


@mcp.tool
def list_expense():
    '''List all the expenses by user'''
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.execute("SELECT * FROM expenses ORDER BY id ASC")
        cols = [d[0] for d in cur.description]
        return [dict(zip(cols, r)) for r in cur.fetchall()]
    

if __name__ == "__main__":
    mcp.run()