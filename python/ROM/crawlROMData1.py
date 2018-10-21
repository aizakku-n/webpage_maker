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
parser.add_argument('-i', '--input', dest='input', default='', required=True,
                    help='input file')
parser.add_argument('-o', '--output', dest='output', nargs='?', type=argparse.FileType('w'), default=sys.stdout,
                    help='output file')
parser.add_argument('-a', '--aleardy', dest='aleardy', default='',
                    help='')
args = parser.parse_args()

rw = re.compile("[!'@]")

if __name__ == '__main__':
    s = None
    with open(args.input, 'r') as f:
        s = BeautifulSoup(f.read(), 'lxml')
    if s is None:
        exit()

    for div in s.find_all('div', class_="rom-tr title"):
        d = dict()
        if div.find('a', href=True):
            d.setdefault('title', div.find('a', href=True).text)
            d.setdefault('id', rw.sub('', div.find('a', href=True).get('href').lstrip('/').replace('.htm','').replace('/','-').replace('@','_')))
            link = 'https://www.freeroms.com' + div.find('a', href=True).get('href')

            t = BeautifulSoup(requests.get(link).text, 'lxml')
            script = t.find('script', language="javascript")
            if script:
                for line in script.text.split('\n'):
                    if '<span><a href="' in line:
                    # if '<a href="http://download.freeroms.com' in line:
                        d.setdefault('DL1', line.split('<a href="')[-1].split('">Direct&nbsp;Download</a')[0])
                        print('\t'.join(['{}:{}'.format(k,v) for k, v in d.items()]), flush=True)
                        break
