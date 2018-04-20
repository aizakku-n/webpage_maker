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
parser.add_argument('-o', '--output', dest='output', nargs='?', type=argparse.FileType('w'), default=sys.stdout,
                    help='output file')
parser.add_argument('-', '--', dest='', default='',
                    help='')
args = parser.parse_args()

def scraping(url):
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
    for line in args.input:
        line = line.strip('\n')
        l_lst = line.split('\t')

        url = l_lst[2]
        soup = scraping(url)

        img = soup.find('img').get('src')
        print('{}\t{}'.format(line, img))
