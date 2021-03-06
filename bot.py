# -*- coding: utf-8 -*-
import praw
import time
from praw.helpers import comment_stream
from urllib2 import HTTPError

r = praw.Reddit("sup son fixer by /u/TheShadowZero")
r.login()

target_text = '¯\_(ツ)_/¯'
response_text = '¯\\\\\_(ツ)_/¯ -- here, you dropped a \\\ '

subreddit = r.get_subreddit('dota2')


processed = []
while True:
	try:
		for c in subreddit.get_comments():
			if target_text.decode("utf-8") in c.body and c.id not in processed:
				c.reply(response_text)
				processed.append(c.id)
	except HTTPError, e:
		if e.code in [429, 500, 502, 503, 504]:
			time.sleep(60)
			pass
	time.sleep(180)
