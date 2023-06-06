#!/usr/bin/python3
"""Recursively queries Reddit for titles of hot articles for a subreddit."""
import requests

def recurse(subreddit, hot_lists=[]):
    """lists containing the titles of all hot articles for a subreddit"""

