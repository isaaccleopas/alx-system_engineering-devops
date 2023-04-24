#!/usr/bin/python3
"""Displays to-do list information for a given employee ID and exports data in CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [(user.get("id"), user.get("username"), l.get("completed"), l.get("title")) for l in todos]
    filename = "{}.csv".format(user.get("id"))
    
    with open(filename, mode='w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for row in completed:
            writer.writerow(row)
            
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(t)) for t in completed]
