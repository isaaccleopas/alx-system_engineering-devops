#!/usr/bin/python3
"""Displays the todo list of an employee"""
import requests
import sys


if __name__ == '__main__':
    base_url = 'https://jsonplaceholder.typicode.com/'
    employee_id = sys.argv[1]
    users = requests.get(base_url + 'users/{}'.format(employee_id)).json()
    todo_list = requests.get(base_url + 'todos',
                             params={'userId': employee_id}).json()

    employee_name = users['name']
    num_completed_tasks = [
        todo_item.get('title') for todo_item in todo_list
        if todo_item.get('userId') == int(employee_id)
        and todo_item.get('completed') is True
    ]
    total_num_tasks = len(todo_list)

    print('Employee {} is done with tasks ({}/{}):'.format(
        employee_name, len(num_completed_tasks), total_num_tasks))
    [print('\t{}'.format(title)) for title in num_completed_tasks]
