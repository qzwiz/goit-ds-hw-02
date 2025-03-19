import sqlite3

DB_NAME = "task_manager.db"

def create_db():
    with sqlite3.connect(DB_NAME) as con:
        cur = con.cursor()

        with open("task_manager.sql", "r", encoding="utf-8") as f:
            sql_script = f.read()

        cur.executescript(sql_script)
        print("✅ База даних успішно створена!")

if __name__ == "__main__":
    create_db()
