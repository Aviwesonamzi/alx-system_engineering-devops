#!/usr/bin/python3
"""
Fetches TODO list progress for a given employee ID and exports to JSON.
"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    base_url = 'https://jsonplaceholder.typicode.com/'

    # Get user information
    user_url = base_url + 'users/{}'.format(employee_id)
    user_response = requests.get(user_url).json()
    username = user_response.get('username')

    # Get TODO list for the user
    todo_url = base_url + 'todos'
    todo_response = requests.get(todo_url, params={'userId': employee_id}).json()

    # Structure data for JSON
    tasks = [{"task": task.get('title'),
              "completed": task.get('completed'),
              "username": username} for task in todo_response]
    data = {str(employee_id): tasks}

    # Write to JSON file
    json_filename = '{}.json'.format(employee_id)
    with open(json_filename, mode='w') as json_file:
        json.dump(data, json_file)

    print("Data exported to {} successfully.".format(json_filename))
