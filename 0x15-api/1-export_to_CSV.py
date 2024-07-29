#!/usr/bin/python3
"""
Fetches TODO list progress for a given employee ID and exports to CSV.
"""

import csv
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

    # Write to CSV
    csv_filename = '{}.csv'.format(employee_id)
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todo_response:
            csv_writer.writerow([employee_id, username, task.get('completed'), task.get('title')])

    print("Data exported to {} successfully.".format(csv_filename))
