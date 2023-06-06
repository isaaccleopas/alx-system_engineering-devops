#!/usr/bin/python3
"""Query Reddit for hot post of a subreddit."""
import requests

def top_ten(subreddit):
    """This function prints top 10 post of a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent':'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts[:10]:
            title = post['data']['title']
            print(title)
    else:
        print("None")
