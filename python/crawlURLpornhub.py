# -*- coding: utf-8 -*-

import time
import re
# from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import sys
import argparse
import json
# from progressbar import ProgressBar



parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', dest='input', type=argparse.FileType('r'), default=sys.stdin,
                    help='input file (json)')
# parser.add_argument('-o', '--output', dest='output', nargs='?', type=argparse.FileType('w'), default=sys.stdout,
                    # help='output file')
parser.add_argument('-', '--', dest='', default='',
                    help='')
args = parser.parse_args()

START, END = 1, 10

if __name__ == '__main__':
    URL = "https://jp.pornhub.com/video?page={}"

    for i in range(START, END+1):

        url = URL.format(i)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')

        # print(soup)
        # exit()

        # for a in soup.find_all('div'):
        for d in soup.find_all('div', class_="thumbnail-info-wrapper clearfix"):
            a = d.find('a')
            # link = 'https://jp.pornhub.com/' + a.get('href')
            link = 'https://jp.pornhub.com/view_video.php?viewkey=415701615'
            title = a.get('title')

            print(link, title)

            d_soup = BeautifulSoup(requests.get(link).text, 'lxml')
            print(d_soup)

            exit()

        exit()
        # for ar in soup.find_all('article'):
        #     # print(ar)
        #
        #     a = ar.find('a')
        #     detail = None
        #     if a:
        #         detail = 'http://share-videos.se' + a.get('href')
        #
        #     img = ar.find('img')
        #     thum = None
        #     if img:
        #         thum = img.get('src')
        #
        #     if a and img:
        #         detail = 'http://share-videos.se' + a.get('href')
        #         thum = img.get('src')
        #         print('{}\t{}'.format(detail, thum))
