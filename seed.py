import sqlite3
from faker import Faker
import random

DB_NAME = "task_manager.db"
faker = Faker()

def seed_data():
    with sqlite3.connect(DB_NAME) as con:
        cur = con.cursor()

        # Додавання статусів
        statuses = [('new',), ('in progress',), ('completed',)]
        cur.executemany("INSERT INTO status (name) VALUES (?)", statuses)

        # Додавання користувачів
        users = [(faker.name(), faker.email()) for _ in range(5)]
        cur.executemany("INSERT INTO users (fullname, email) VALUES (?, ?)", users)

        # Отримуємо id користувачів і статусів
        cur.execute("SELECT id FROM users")
        user_ids = [row[0] for row in cur.fetchall()]

        cur.execute("SELECT id FROM status")
        status_ids = [row[0] for row in cur.fetchall()]

        # Додавання завдань
        tasks = [
            (faker.sentence(), faker.text(), random.choice(status_ids), random.choice(user_ids))
            for _ in range(10)
        ]
        cur.executemany("INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, ?, ?)", tasks)

        con.commit()
        print("✅ Дані успішно додані!")

if __name__ == "__main__":
    seed_data()
