#!/usr/bin/python3
# url function constructs the URL to access the subreddit information.
# User-Agent is included so as to avoid request limits
# if the response is 200 it is successful and will return the number of subs 

import requests

def number_of_subscribers(subreddit):
  url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
  headers = {'User-Agent': 'request'}
  response = requests.get(url, headers=headers)

  if response.status_code == 200:
    return response.json()['data']['subscribers']

  return 0
