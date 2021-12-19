'''
===================================================================
Project Name    : ニュース
File Name       : news.py
Encoding        : UTF-8
Creation Date   : 2021/1/3
Copyright (c) 2021 Yuma Horaguchi All rights reserved.
===================================================================
'''

import time
from bs4 import BeautifulSoup as bs
import feedparser
import ssl
import os

def News_Time():
	pass

def News():
	if hasattr(ssl, '_create_unverified_context'):
		ssl._create_default_https_context = ssl._create_unverified_context

	RSS_URL = 'https://news.yahoo.co.jp/rss/topics/top-picks.xml'
	while True:
		data = feedparser.parse(RSS_URL)
		for entry in data.entries:
			os.system('cls' if os.name == 'nt' else 'clear')
			try:
				print('【 ニ ュ ー ス 】')
				print(entry.description)
			except:
				print('【 ニ ュ ー ス 】')
				print('情報を取得中')
			time.sleep(10)

def main():
	News()

if __name__ == "__main__":
	main()
