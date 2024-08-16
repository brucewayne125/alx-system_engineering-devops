#!/usr/bin/python3
# url function constructs the URL to access the subreddit information.
# User-Agent is included so as to avoid request limits
# if the response is 200 it is successful and will return the number of subs 

import requests

def number_of_subscribers(subredit):
  url = f"https://www.reddit.com/r/{subreddit}/about.json"
  headers = {'User-Agent': 'request'}
  response = requests.get(url, headers=headers, allow_redirects=False)

  if respnse.status_code == 200:
    return response.json()['data']['subscribers']
  return 0
