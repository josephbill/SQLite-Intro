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
         conn.commit()
         conn.close()
    

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
 

