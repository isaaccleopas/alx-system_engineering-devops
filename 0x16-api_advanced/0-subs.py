#!/usr/bin/python3
"""This queries the subscribers on Reddit of subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Function returns the number of subscribers of subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
