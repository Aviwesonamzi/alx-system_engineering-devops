import json
import requests

# API endpoints
users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"

# Fetch data from the APIs
users = requests.get(users_url).json()
todos = requests.get(todos_url).json()

# Dictionary to hold all tasks by user ID
all_tasks = {}

# Process each user
for user in users:
    user_id = user['id']
    username = user['username']
    
    # Filter tasks by user ID
    user_tasks = [
        {
            "username": username,
            "task": todo['title'],
            "completed": todo['completed']
        }
        for todo in todos if todo['userId'] == user_id
    ]
    
    # Add to the main dictionary
    all_tasks[user_id] = user_tasks

# Export data to JSON file
with open("todo_all_employees.json", "w") as json_file:
    json.dump(all_tasks, json_file)
