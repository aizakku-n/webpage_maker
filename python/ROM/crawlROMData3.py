# -*- coding: utf-8 -*-

import time
import re
from selenium import webdriver
import requests
import urllib
from bs4 import BeautifulSoup
import sys
import argparse
import json
from progressbar import ProgressBar
from selenium.webdriver.support.ui import Select

parser = argparse.ArgumentParser()
# parser.add_argument('-i', '--input', dest='input', default='', required=True,
                    # help='input file')
parser.add_argument('-o', '--output', dest='output', nargs='?', type=argparse.FileType('w'), default=sys.stdout,
                    help='output file')
parser.add_argument('-a', '--aleardy', dest='aleardy', default='',
                    help='')
parser.add_argument('-d', '--dir', dest='dir', default='data/DL3/',
                    help='')
args = parser.parse_args()


# rw = re.compile("[!'/().!&@+=#\"]")
# space = re.compile("\s+")
# rr = re.compile('[,]')

def consoleRomCrawler(soup):
    rd = dict()
    tbody = soup.find('tbody')
    for a in tbody.find_all('a', href=True):
        rd.setdefault('link', a.get('href'))
        rd.setdefault('id', a.get('href').split('/')[-1])
        rd.setdefault('title', a.text)

        s = BeautifulSoup(requests.get(rd['link']).text, 'lxml')
        t = s.find('tbody')

        for tr in t.find_all('tr'):
            if 'Region:' in tr.text:
                rd.setdefault('region', tr.text.replace('Region:','').strip())

        dl = s.find('a', id="download_link", href=True).get('href')
        r = BeautifulSoup(requests.get(dl).text, 'lxml')
        rd.setdefault('DL3', r.find('a', class_='wait__link', href=True).get('href'))

        return rd

if __name__ == '__main__':
    S1 = BeautifulSoup(requests.get('https://romsmania.cc/roms').text, 'lxml')
    LST = S1.find('tbody').find_all('a', href=True)


    for n, A1 in enumerate(LST):

        console = A1.text
        con_link = A1.get('href')

        with open(args.dir + console, 'w') as f:
            L = []
            S2 =  BeautifulSoup(requests.get(con_link).text, 'lxml')
            L.append(consoleRomCrawler(S2))

            div = S2.find('div', class_='pagination')
            if div:
                END = int(div.find_all('a', {'data-page':True, 'title':False})[-1].get('data-page'))
                p = ProgressBar(2, END+1)
                for i in range(2, END+1):
                    p.update(i+1)

                    time.sleep(1)
                    url = '{}?page={}'.format(con_link, i)
                    S2 = BeautifulSoup(requests.get(url).text, 'lxml')
                    L.append(consoleRomCrawler(S2))

            for d in L:
                print('\t'.join(['{}:{}'.format(k,v) for k, v in d.items()]), flush=True, file=f)

            print('{} fin.'.format(console), file=sys.stderr, flush=True)
