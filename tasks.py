from database import connect

def add_task(title, description, priority, due_date):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO tasks (title, description, priority, due_date, status)
    VALUES (?, ?, ?, ?, ?)
    """, (title, description, priority, due_date, "Pendente"))

    conn.commit()
    conn.close()


def list_tasks():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    conn.close()
    return tasks


def complete_task(task_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE tasks SET status = 'Concluída' WHERE id = ?
    """, (task_id,))

    conn.commit()
    conn.close()


def delete_task(task_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))

    conn.commit()
    conn.close()