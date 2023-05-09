#!/usr/bin/python3
import requests


def recurse(subreddit, hot_list=[], after=None):
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
