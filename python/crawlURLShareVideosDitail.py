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
                    help='input file')
parser.add_argument('-o', '--output', dest='output', nargs='?', type=argparse.FileType('w'), default=sys.stdout,
                    help='output file')
parser.add_argument('-', '--', dest='', default='',
                    help='')
args = parser.parse_args()

# def scraping(url):
#     # Selenium settings
#     options = webdriver.chrome.options.Options()
#     options.add_argument("--headless")  # これ消せばブラウザ画面が出ます
#     driver = webdriver.Chrome(chrome_options=options)
#     # get a HTML response
#     driver.get(url)
#     html = driver.page_source  # more sophisticated methods may be available
#     # parse the response
#     soup = BeautifulSoup(html, 'lxml')
#
#     return soup


if __name__ == '__main__':

    for line in sys.stdin:
        line = line.strip()
        l_lst = line.split('\t')
        # print(l_lst[0])
        # exit()
        # url = 'http://share-videos.se/auto/video/97474606?uid=13'
        url = l_lst[0]
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')

        movie, link = None, None
        for l in soup.text.split('\n'):
            if '</iframe>' in l:
                movie = '<iframe' + l.split('<iframe')[-1].split('</iframe>')[0]
            elif 'ソース元' in l:
                link = l.split('a href="')[-1].split('"')[0]

        if movie and link:
            print(line + '\t{}\t{}'.format(link, movie))
