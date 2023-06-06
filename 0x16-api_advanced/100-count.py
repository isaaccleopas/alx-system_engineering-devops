#!/usr/bin/python3
"""Counts it."""
import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """
    Returns a list containing the titles of all hot articles for a
    given subreddit. If no results are found for the given subreddit,
    the function should return None.
    """
    if count_dict is None:
        count_dict = {}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()
    posts = data["data"]["children"]
    for post in posts:
        title = post["data"]["title"].lower()
        for word in word_list:
            word = word.lower()
            if word in title:
                count_dict[word] = count_dict.get(word, 0) + 1

    next_page = data["data"]["after"]
    if next_page is not None:
        return count_words(subreddit, word_list, after=next_page,
                           count_dict=count_dict)

    sorted_counts = sorted(count_dict.items(),
                           key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print("{}: {}".format(word, count))
