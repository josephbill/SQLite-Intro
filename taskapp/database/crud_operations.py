# class blueprint , creation db objects 
import sqlite3
class CRUDOperations:
    def __init__(self,db_path) -> None:
        self.db_path = db_path
    

    # methods to effect on each instance 
    def create_table(self):
         conn = sqlite3.connect(self.db_path)
        #  a cursor is an object that provides an interface to interact with the db 
        # execute sql commands and retrieve data from database results sets. 
         cursor = conn.cursor()
         cursor.execute('''
                        CREATE TABLE IF NOT EXISTS tasks (
                             id INTEGER PRIMARY KEY, 
                             name TEXT NOT NULL, 
                             description TEXT
                        )
                        '''
                        )
        #  users table
         cursor.execute('''
                        CREATE TABLE IF NOT EXISTS users (
                             id INTEGER PRIMARY KEY, 
                             name TEXT NOT NULL, 
                             email TEXT NOT NULL
                        )
                        '''
                        )
        #  join table 
         cursor.execute('''
                        CREATE TABLE IF NOT EXISTS user_tasks (
                             id INTEGER PRIMARY KEY, 
                             user_id INTEGER,
                             task_id INTEGER,
                             FOREIGN KEY (user_id) REFERENCES users(id),
                             FOREIGN KEY (task_id) REFERENCES tasks(id)
                        )
                        '''
                        )
         conn.commit()
         conn.close()

    # associating methods 
    # assign task to a user (populate our user_tasks)
    def assing_task_to_user(self, user_id, task_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO user_tasks (user_id,task_id) VALUES (?,?)',(user_id,task_id))
        conn.commit()
        conn.close()

    #  SQL JOINS 
    #  JOIN clauses : used to combine rows from two or more tables , based on a related column between them. 
    #  method should display user info and the task associated 
    def get_assigned_tasks(self,user_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        # join statement 
        cursor.execute('''
             SELECT tasks.id, tasks.name, tasks.description FROM tasks
             INNER JOIN user_tasks ON tasks.id = user_tasks.task_id
             WHERE user_tasks.user_id = ?
                      ''',(user_id,))
        # returning this as a collection (fetchAll.)
        tasks = cursor.fetchall()
        conn.close()
        return tasks
    

    def create_user(self,name,email):
        conn = sqlite3.connect(self.db_path)
        #  a cursor is an object that provides an interface to interact with the db 
        # execute sql commands and retrieve data from database results sets. 
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name,email) VALUES (?,?)',(name,email))
        conn.commit()
        conn.close()
    # end of associating methods 
    

    def create_item(self,name,description):
        conn = sqlite3.connect(self.db_path)
        #  a cursor is an object that provides an interface to interact with the db 
        # execute sql commands and retrieve data from database results sets. 
        cursor = conn.cursor()
        cursor.execute('INSERT INTO tasks (name,description) VALUES (?,?)',(name,description))
        conn.commit()
        conn.close()


    def read_item(self):
        conn = sqlite3.connect(self.db_path)
        #  a cursor is an object that provides an interface to interact with the db 
        # execute sql commands and retrieve data from database results sets. 
        cursor = conn.cursor()
        cursor.execute('SELECT id, name , description FROM tasks')
        # return here is as collection 
        #  list of tuples 
        items = cursor.fetchall()
        conn.commit()
        conn.close()
        return items



    def update_item(self, item_id, name, description):
        conn = sqlite3.connect(self.db_path)
        #  a cursor is an object that provides an interface to interact with the db 
        # execute sql commands and retrieve data from database results sets. 
        cursor = conn.cursor()
        cursor.execute('UPDATE tasks SET name = ? , description = ? WHERE id = ?',(name,description,item_id))
        conn.commit()
        conn.close()
 


    def delete_item(self,item_id):
        conn = sqlite3.connect(self.db_path)
        #  a cursor is an object that provides an interface to interact with the db 
        # execute sql commands and retrieve data from database results sets. 
        cursor = conn.cursor()
        cursor.execute('DELETE FROM tasks WHERE id = ?',(item_id,))
        conn.commit()
        conn.close()
 

