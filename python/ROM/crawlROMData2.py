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


parser = argparse.ArgumentParser()
# parser.add_argument('-i', '--input', dest='input', default='', required=True,
                    # help='input file')
parser.add_argument('-o', '--output', dest='output', nargs='?', type=argparse.FileType('w'), default=sys.stdout,
                    help='output file')
parser.add_argument('-a', '--aleardy', dest='aleardy', default='',
                    help='')
args = parser.parse_args()

# URL = 'https://edgeemu.net/browse-n64-{}.htm'
# URL = 'https://edgeemu.net/browse-gb-{}.htm'
# URL = 'https://edgeemu.net/browse-nes-{}.htm'
# URL = 'https://edgeemu.net/browse-gbc-{}.htm'
# URL = 'https://edgeemu.net/browse-snes-{}.htm'
# URL = 'https://edgeemu.net/browse-gba-{}.htm'
URL = 'https://edgeemu.net/browse-saturn-{}.htm'

# L = ['N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
L = ['num','A','B','C','D','E','F','G','H','I','J','K','L',
    'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

rw = re.compile("[!'/().!&@+=#\"]")
space = re.compile("\s+")
rr = re.compile('[,]')

if __name__ == '__main__':
    URL = 'https://edgeemu.net/'
    S1 = BeautifulSoup(requests.get(URL).text, 'lxml')
    table1 = S1.find('table', class_="roms")
    for A1 in table1.find_all('a', href=True):
        console = A1.text.strip()
        con_link = URL + A1.get('href')

        S2 = BeautifulSoup(requests.get(con_link).text, 'lxml')
        p = S2.find('div', id="content").find('p', align="center")

        for A2 in p.find_all('a', href=True):
            init_link = URL + A2.get('href')

            S3 = BeautifulSoup(requests.get(init_link).text, 'lxml')
            table2 = S3.find('table', class_="roms")

            for A3 in table2.find_all('a', href=True):
                rom_link = URL + A3.get('href')
                rom = A3.text

                print(table2)
            exit()


    for i in L:
        soup = BeautifulSoup(requests.get(URL.format(i)).text, 'lxml')
        table = soup.find('table', class_='roms')
        for a in table.find_all('a', href=True):
            d = dict()
            d.setdefault('title', a.text)
            dl = 'https://edgeemu.net/{}'.format(a.get('href'))

            s = BeautifulSoup(requests.get(dl).text, 'lxml')

            div = s.find('div', class_="content")
            d.setdefault('id', space.sub('_', rr.sub(' ', rw.sub('', div.find('h3').text))))

            table = div.find('table', style=True)
            d.setdefault('DL2','https://edgeemu.net/' + table.find('a', href=True).get('href'))
            print('\t'.join(['{}:{}'.format(k,v) for k, v in d.items()]), flush=True)
            time.sleep(1)

        print("{} fin.".format(i), file=sys.stderr, flush=True)
