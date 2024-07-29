#!/usr/bin/python3
import json
import requests

def fetch_data():
    # Base URL for API
    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch all users
    users = requests.get(f'{base_url}/users').json()

    # Dictionary to hold all data
    all_tasks = {}

    for user in users:
        user_id = user['id']
        username = user['username']

        # Fetch todos for the current user
        todos = requests.get(f'{base_url}/todos', params={'userId': user_id}).json()

        # List to store the tasks in the required format
        user_tasks = []
        for todo in todos:
            user_tasks.append({
                'username': username,
                'task': todo['title'],
                'completed': todo['completed']
            })

        # Assign tasks to the user_id in the dictionary
        all_tasks[user_id] = user_tasks

    # Write the dictionary to a JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_tasks, json_file)

if __name__ == "__main__":
    fetch_data()
