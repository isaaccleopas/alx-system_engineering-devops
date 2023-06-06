#!/usr/bin/python3o
"""Recursively queries Reddit for titles of hot articles for a subreddit."""
import requests


def recurse(subreddit, hot_lists=[]):
    """lists containing the titles of all hot articles for a subreddit"""
    def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()['data']
        children = data['children']
        after = data['after']

        for child in children:
            hot_list.append(child['data']['title'])

        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
