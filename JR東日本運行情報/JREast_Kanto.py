'''
===================================================================
Project Name    : JR東日本運行情報
File Name       : JREast_Kanto.py
Encoding        : UTF-8
Creation Date   : 2021/1/13
Copyright (c) 2021 Yuma Horaguchi All rights reserved.
===================================================================
'''

import time
from bs4 import BeautifulSoup as bs
import feedparser
import ssl
import os
import requests

def trainfo():
	source = requests.get('https://traininfo.jreast.co.jp/train_info/kanto.aspx').text
	soup  = bs(source, 'lxml')
	info  = soup.find_all('p', class_= 'mt10 sp_mt5 sp_mr25')
	while True:
		old_info = info
		source = requests.get('https://traininfo.jreast.co.jp/train_info/kanto.aspx').text
		soup   = bs(source, 'lxml')
		info   = soup.find_all('p', class_= 'mt10 sp_mt5 sp_mr25')
		if old_info != info:
			os.system("afplay -v 0.1 -r 0.90 -q 1 chime.mp3")
			os.system("afplay -v 0.1 -r 0.90 -q 1 chime.mp3")
		if info != []:
			for i in info:
				os.system('cls' if os.name == 'nt' else 'clear')
				print('【 J R 東 日 本 運 行 情 報 (首 都 圏 エ リ ア)】')
				print(i.text)
				time.sleep(10)
		else:
			os.system('cls' if os.name == 'nt' else 'clear')
			print('【 J R 東 日 本 運 行 情 報 (首 都 圏 エ リ ア)】')
			print('現在平常通り運転しております。')
			time.sleep(10)

def main():
	trainfo()

if __name__ == "__main__":
	main()
