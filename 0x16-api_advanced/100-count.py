#!/usr/bin/python3
"""Count it"""
import requests

def count_words(subreddit, word_list, count={}):
    """
    Returns a list containing the titles of all hot articles for a
    given subreddit. If no results are found for the given subreddit,
    the function should return None.
    """
    if not word_list:
        sorted_count = sorted(count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_count:
            print("{}: {}".format(word, count))
        return

    word = word_list[0].lower()
    word_list = word_list[1:]

    headers = {'User-Agent': 'Mozilla/5.0'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()

    for child in data['data']['children']:
        title = child['data']['title'].lower()
        occurrences = title.count(word)
        if occurrences > 0:
            count[word] = count.get(word, 0) + occurrences

    count_words(subreddit, word_list, count)
