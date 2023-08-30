from database.crud_operations import CRUDOperations

db_path = 'database/tasks.db'
crud = CRUDOperations(db_path)

# Create the table only if it doesn't exist
crud.create_table()

# Create items only if they don't exist
existing_items = crud.read_item()
if not existing_items:
    crud.create_item('Task 1', 'Cover content on SQL')
    crud.create_item('Task 2', 'Grading code challenge')
    crud.create_item('Task 3', 'Publish Scores')


# Read the items
items = crud.read_item()
print("Reading Items:")
for item in items:
    print(item)

# Update the item
crud.update_item(1, "New Update", "Cover content on SQL")
# Read the items
items = crud.read_item()
print("Reading Items after update:")
for item in items:
    print(item)

# Delete
crud.delete_item(2)
items = crud.read_item()
print("Reading Items after delete:")
for item in items:
    print(item)


# testing associated methods 
crud.create_user('Joseph','joseph@gmail.com')
crud.create_user('Alice','alice@gmail.com')

crud.assing_task_to_user(1,1)
crud.assing_task_to_user(1,3)
crud.assing_task_to_user(2,3)

# get the users tasks 
user_tasks = crud.get_assigned_tasks(1)
print("Check assigned tasks for Joseph:")
for task in user_tasks:
    print(task)