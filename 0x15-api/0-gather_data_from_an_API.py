#!/usr/bin/python3
"""Displays the to-do list for a given employee ID."""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed_tasks = [todo.get("title")
                       for todo in todos if todo.get("completed") is True]
    print("Employee {} is done with tasks ({}/{}):".format(
        user.get("name"), len(completed_tasks), len(todos)))
    [print("\t{}".format(task)) for task in completed_tasks]
