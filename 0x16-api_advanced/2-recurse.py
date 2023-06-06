#!/usr/bin/python3
"""Recursively queries Reddit for titles of hot articles for a subreddit"""
import requests


def recurse(subreddit, hot_list=[]):
    """lists containing the titles of all hot articles for a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers,
                            allow_redirects=False)
    if response.status_code != 200:
        return None

    data = response.json()
    posts = data["data"]["children"]
    for post in posts:
        title = post["data"]["title"]
        hot_list.append(title)

    next_page = data["data"]["after"]
    if next_page is not None:
        return recurse(
    subreddit, hot_list=hot_list, after=next_page)
    else:
        return hot_list
