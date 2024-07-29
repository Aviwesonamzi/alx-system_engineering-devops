#!/usr/bin/python3
"""
Fetches TODO list progress for a given employee ID using a REST API.
"""

import requests
import sys

if __name__ == "__main__":
    # Ensure the script is not executed when imported
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
    employee_name = user_response.get('name')

    # Get TODO list for the user
    todo_url = base_url + 'todos'
    todo_response = requests.get(todo_url, params={'userId': employee_id}).json()

    total_tasks = len(todo_response)
    done_tasks = [task for task in todo_response if task.get('completed')]
    done_count = len(done_tasks)

    # Print results
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, done_count, total_tasks
    ))
    for task in done_tasks:
        print("\t {}".format(task.get('title')))
