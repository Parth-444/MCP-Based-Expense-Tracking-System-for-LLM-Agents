## MCP-Based Expense Tracker 🧾
A lightweight Model Context Protocol (MCP) server that enables LLM-powered agents to track, manage, and query personal expenses through structured tools and resources.
Built using FastMCP, SQLite, and Python, this project demonstrates how AI agents can interact with persistent financial data in a safe and deterministic way.

## ✨ Features

- **📌 MCP Tools for Expense Management**

  1. Add new expense entries

  2. List expenses within a date range

  3. Edit existing expenses

  4. Delete expenses by date and category

💾 Persistent Storage

Uses SQLite for durable, local data storage

Automatically initializes database schema on startup

🗂 Structured Expense Categories

Exposes predefined categories and subcategories via MCP resources

Categories stored in JSON for easy extensibility

🤖 LLM-Friendly Design

Deterministic tool interfaces

Structured JSON responses

Clean separation between tools (actions) and resources (data)

🏗 Architecture Overview
├── expense.db          # SQLite database (auto-created)
├── categories.json     # Expense categories & subcategories
├── main.py             # MCP server implementation


FastMCP handles tool and resource exposure

SQLite stores expense records

MCP Tools perform CRUD operations

MCP Resources provide contextual metadata to agents

🛠 MCP Tools
add_expense

Adds a new expense entry to the database.

Parameters

date (string)

amount (float)

category (string)

subcategory (optional)

note (optional)

list_expenses

Lists all expenses between a start and end date.

Parameters

start_date (string)

end_date (string)

edit_expense

Updates the amount of an existing expense.

Parameters

date (string)

category (string)

amount (float)

delete_expense

Deletes an expense entry.

Parameters

date (string)

category (string)

📚 MCP Resources
expense://categories

Returns all supported expense categories and subcategories in JSON format, enabling agents to reason over valid inputs.

🚀 Getting Started
1️⃣ Install Dependencies
pip install fastmcp

2️⃣ Run the MCP Server
python main.py


The server will:

Initialize the SQLite database

Register all MCP tools and resources

Be ready to connect with MCP-compatible clients (e.g., Claude Desktop)

🔌 Usage with AI Agents

This MCP server is designed to be consumed by LLM-based agents, enabling workflows such as:

“Add today’s food expense”

“Show my expenses for last week”

“Edit my fuel expense from yesterday”

“List all transport expenses this month”

The agent invokes tools programmatically while maintaining clean separation between reasoning and execution.

📈 Future Enhancements

Natural language expense querying

Monthly and category-wise summaries

Input validation and schema enforcement

Conversational memory for multi-step finance workflows

Integration with visualization dashboards

🎯 Why This Project?

This project demonstrates:

Practical use of Model Context Protocol

Tool-based agent architecture

Safe and structured AI–data interaction

Backend engineering fundamentals with AI integration

🧠 Author

Parth Singh Rana
AI / GenAI / Agentic Systems Enthusiast


