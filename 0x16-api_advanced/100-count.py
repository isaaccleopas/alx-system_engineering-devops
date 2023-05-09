#!/usr/bin/python3
""" Count it! """
import re
import requests


def count_words(subreddit, word_list, word_count=None):
    """
    Recursively counts the occurrences of
    the given keywords in the hot titles of a subreddit.
    """
    if word_count is None:
        word_count = {}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json()
    
    for child in data['data']['children']:
        title = child['data']['title'].lower()
        for word in word_list:
            if word not in word_count:
                word_count[word] = 0
            count = len(re.findall(rf"\b{word}\b", title))
            if count > 0:
                word_count[word] += count
    
    if data['data']['after'] is not None:
        count_words(subreddit, word_list, word_count=word_count)
    
    elif len(word_count) > 0:
        sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            print(f"{word}: {count}")
