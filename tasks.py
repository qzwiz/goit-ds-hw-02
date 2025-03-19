import sqlite3

DB_NAME = "task_manager.db"

def execute_query(query, params=None):
    with sqlite3.connect(DB_NAME) as con:
        cur = con.cursor()
        if params:
            cur.execute(query, params)
        else:
            cur.execute(query)
        con.commit()
        return cur.fetchall()

# Отримати всі завдання з користувачами та статусами
query_tasks = """
SELECT tasks.id, tasks.title, tasks.description, users.fullname, status.name AS status
FROM tasks
JOIN users ON tasks.user_id = users.id
JOIN status ON tasks.status_id = status.id;
"""

# Виконання запиту
tasks = execute_query(query_tasks)
for task in tasks:
    print(task)

# Оновити статус завдання
update_status = "UPDATE tasks SET status_id = ? WHERE id = ?"
execute_query(update_status, (2, 1))

# Видалити користувача (і всі його завдання)
delete_user = "DELETE FROM users WHERE id = ?"
execute_query(delete_user, (3,))
