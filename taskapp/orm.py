import sqlite3

# TASKS 
class Task:
    def __init__(self,task_id,title,description,done) -> None:
        self.task_id = task_id
        self.title= title
        self.description= description
        self.done = done 

    # Database intialization 
# Database initialization and setup
def initialize_database():
    conn = sqlite3.connect("ormtasks.db")
    cursor = conn.cursor()
    # Create the tasks table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            task_id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            done BOOLEAN
        )
    ''')
    conn.commit()
    conn.close()    

# Create a new task in the database
def create_task(task):
    conn = sqlite3.connect("ormtasks.db")
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO tasks (title, description, done)
        VALUES (?, ?, ?)
    ''', (task.title, task.description, task.done))

    conn.commit()
    conn.close()


# Retrieve all tasks from the database
def get_all_tasks():
    conn = sqlite3.connect("ormtasks.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()

    tasks = []
    for row in rows:
        task = Task(row[0], row[1], row[2], row[3])
        tasks.append(task)

    conn.close()
    return tasks

# each object instance is then equated to a record row in our db table 
if __name__ == "__main__":
    initialize_database()

    # create a new task 
    new_task = Task(None, "Sample Task", "This is a sample",False)
    create_task(new_task)

    # retrieving a task 
    tasks = get_all_tasks()
    for task in tasks:
        print(f"Task ID: {task.task_id}, Task Title: {task.title}, Done: {task.done},")