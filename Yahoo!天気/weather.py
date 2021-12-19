'''
===================================================================
Project Name    : 天気予報
File Name       : weather.py
Encoding        : UTF-8
Creation Date   : 2021/1/14
Copyright (c) 2021 Yuma Horaguchi All rights reserved.
===================================================================
'''

import time
from bs4 import BeautifulSoup as bs
import feedparser
import ssl
import os
import itertools

def weather(city_1 : str, url_1 : str , city_2 : str, url_2 : str, city_3 : str, url_3 : str):
	if hasattr(ssl, '_create_unverified_context'):
		ssl._create_default_https_context = ssl._create_unverified_context

	data_1 = feedparser.parse(url_1)
	data_2 = feedparser.parse(url_2)
	data_3 = feedparser.parse(url_3)

	count = 0
	for entry_1, entry_2, entry_3, i in zip(data_1.entries, data_2.entries, data_3.entries, range(4)):
		try:
			weather_1 = entry_1.title.split(' ')
			weather_2 = entry_2.title.split(' ')
			weather_3 = entry_3.title.split(' ')
			os.system('cls' if os.name == 'nt' else 'clear')
			print(f'【 天 気 予 報  {weather_1[1].strip()}】')
			print(city_1, weather_1[4].center(5, "　"), weather_1[6].split('/')[0].center(5, ' ').replace('℃','°C'), "/" , weather_1[6].split('/')[1].center(5, ' ').replace('℃','°C'))
			print(city_2, weather_2[4].center(5, "　"), weather_2[6].split('/')[0].center(5, ' ').replace('℃','°C'), "/" , weather_2[6].split('/')[1].center(5, ' ').replace('℃','°C'))
			print(city_3, weather_3[4].center(5, "　"), weather_3[6].split('/')[0].center(5, ' ').replace('℃','°C'), "/" , weather_3[6].split('/')[1].center(5, ' ').replace('℃','°C'))
		except:
			os.system('cls' if os.name == 'nt' else 'clear')
			print(f'【 天 気 予 報  {weather_1[1].strip()}】')
			print('情報を取得中')
		time.sleep(3)

def main():
	sapporo       = 'https://rss-weather.yahoo.co.jp/rss/days/1400.xml'
	sendai        = 'https://rss-weather.yahoo.co.jp/rss/days/3410.xml'
	tokyo         = 'https://rss-weather.yahoo.co.jp/rss/days/4410.xml'
	saitama       = 'https://rss-weather.yahoo.co.jp/rss/days/4310.xml'
	chiba         = 'https://rss-weather.yahoo.co.jp/rss/days/4510.xml'
	mito          = 'https://rss-weather.yahoo.co.jp/rss/days/4010.xml'
	utsunomiya    = 'https://rss-weather.yahoo.co.jp/rss/days/4110.xml'
	yokohama      = 'https://rss-weather.yahoo.co.jp/rss/days/4610.xml'
	maebashi      = 'https://rss-weather.yahoo.co.jp/rss/days/4210.xml'
	kofu          = 'https://rss-weather.yahoo.co.jp/rss/days/4910.xml'
	nigata        = 'https://rss-weather.yahoo.co.jp/rss/days/5410.xml'
	shizuoka      = 'https://rss-weather.yahoo.co.jp/rss/days/5010.xml'
	kanazawa      = 'https://rss-weather.yahoo.co.jp/rss/days/5610.xml'
	nagoya        = 'https://rss-weather.yahoo.co.jp/rss/days/5110.xml'
	osaka         = 'https://rss-weather.yahoo.co.jp/rss/days/6200.xml'
	hiroshima     = 'https://rss-weather.yahoo.co.jp/rss/days/6710.xml'
	kochi         = 'https://rss-weather.yahoo.co.jp/rss/days/7410.xml'
	fukuoka       = 'https://rss-weather.yahoo.co.jp/rss/days/8210.xml'
	naha          = 'https://rss-weather.yahoo.co.jp/rss/days/9110.xml'
	city_name_1 = ['札　　幌(北 海 道)',
				   '仙　　台(宮 　 城)',
				   '東　　京(東 　 京)',
				   'さいたま(埼 　 玉)',
				   '千　　葉(千 　 葉)',
				   '水　　戸(茨 　 城)',
				   '宇 都 宮(栃 　 木)',
				   '前　　橋(群 　 馬)',
				   '甲　　府(山 　 梨)']
	city_name_2 = ['新　　潟(新 　 潟)',
				   '静　　岡(静 　 岡)',
				   '名 古 屋(愛 　 知)',
				   '大　　阪(大 　 阪)',
				   '広　　島(広 　 島)',
				   '高　　知(高 　 知)',
				   '福　　岡(福 　 岡)',
				   '那　　覇(沖 　 縄)']
	city_url_1 = [sapporo   ,
				  tokyo     ,
				  sendai    ,
				  saitama   ,
				  chiba     ,
				  mito      ,
				  utsunomiya,
				  maebashi  ,
				  kofu       ]
	city_url_2 = [nigata    ,
				  shizuoka  ,
				  kanazawa  ,
				  nagoya    ,
				  osaka     ,
				  hiroshima ,
				  kochi     ,
				  fukuoka   ,
				  naha       ]

	while True:
		for i in range(len(city_name_1) - 1):
			weather('横　　浜(神 奈 川)', yokohama, city_name_1[i], city_url_1[i], city_name_2[i], city_url_2[i])


if __name__ == "__main__":
	main()
