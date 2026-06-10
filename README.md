[README.md](https://github.com/user-attachments/files/28789975/README.md)
# ⚙️ CoreFlow AI: Automated Triage Middleware Pipeline

CoreFlow AI is a production-grade backend data pipeline designed to bridge the gap between unstructured user inputs (like frantic customer support messages or error logs) and structured relational enterprise storage. 

This application takes chaotic human language, passes it through an automated evaluation logic layer to extract meaning, assigns categories and priority values, and commits the sanitized data into a secure SQL database.

---

## 🚀 Key Features
* **Automated Data Processing:** Instantly parses text strings into structured data elements.
* **Relational Storage Integrity:** Uses optimized SQLite schema architectures with parameter mapping to prevent data errors.
* **Interactive Live Dashboard:** Built completely with a Streamlit interface so business stakeholders or clients can view real-time log warehouse additions.
* **Zero-Cost Local Architecture:** Includes a rule-based mock intelligence engine file for instant testing without infrastructure charges.

---

## 🗂️ Core Architecture & Responsibilities

The codebase follows professional modular formatting to keep user views, logic parameters, and data layers completely separated:

* `/src/database_manager.py` — **The Warehouse:** Manages database initialization, schema verification, safe row insertion methods, and state queries.
* `/src/mock_ai.py` — **The Engine Brain:** Reads contextual text patterns to classify issues by category (`Bug`, `Feature Request`, `UI Change`) and severity (`Critical`, `High`, `Medium`, `Low`).
* `/src/real_ai.py` — **The API Placeholder:** Left blank intentionally for seamless production migration to a live cloud model.
* `/app.py` — **The Front-End Interface:** Renders the clean presentation layer, text ingest parameters, and database tables.

---

## 🛠️ Built With
* **Python 3.10+** — For backend logic pipelines.
* **SQLite3** — For local relational data storage and indexing.
* **Streamlit** — For the web dashboard execution interface.
* **Pandas** — For rapid data frame formatting and visual spreadsheet rendering.

---

## 💻 How to Run This Project Locally

1. Clone or download this repository files to your computer.
2. Open your terminal inside the project directory and install the necessary package extensions:
   ```bash
   pip install streamlit pandas
