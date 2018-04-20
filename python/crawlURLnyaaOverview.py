# -*- coding: utf-8 -*-

import time
import re
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
# from progressbar import ProgressBar
import sys
import argparse
import json


parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', dest='input', type=argparse.FileType('r'), default=sys.stdin,
                    help='input file (json)')
# parser.add_argument('-o', '--output', dest='output', nargs='?', type=argparse.FileType('w'), default=sys.stdout,
                    # help='output file')
parser.add_argument('-', '--', dest='', default='',
                    help='')
args = parser.parse_args()


START, END = 1, 5
# P = ProgressBar(START, END)

def scrapingJS(url):
    # Selenium settings
    options = webdriver.chrome.options.Options()
    options.add_argument("--headless")  # これ消せばブラウザ画面が出ます
    driver = webdriver.Chrome(chrome_options=options)
    # get a HTML response
    driver.get(url)
    html = driver.page_source  # more sophisticated methods may be available
    # parse the response
    soup = BeautifulSoup(html, 'lxml')

    return soup


if __name__ == '__main__':
    URL = "https://sukebei.nyaa.si/?c=1_0&p={}"
    other_lang = lambda x: ('nglish' in x) or ('韓国語' in x) or ('中国語' in x)

    for i in range(START, END):
        # P.update(i)
        url = URL.format(i)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')

        D = dict()
        tb_obj = soup.find('tbody')
        for tr in tb_obj.find_all('tr', class_="success"):
            try:
                a_lst = tr.find_all('a')
                category = a_lst[0].get('title').split(' ')[-1]
                title = a_lst[1].get('title')
                detail = 'https://sukebei.nyaa.si' + a_lst[1].get('href')
                torrent = 'https://sukebei.nyaa.si' + a_lst[2].get('href')
                magnet = a_lst[3].get('href')

                td_lst = tr.find_all('td')
                size = tr.find_all('td')[3].string
                date = tr.find_all('td')[4].string.replace('-','').replace(' ','').replace(':','')

                if other_lang(title):
                    continue

                d_soup = scrapingJS(detail)
                img = d_soup.find('img').get('src')

                print('\t'.join([title, category, detail, size, date, torrent, magnet, img]))
            except:
                sys.stderr.write('Rise something error. Skip this method\n')