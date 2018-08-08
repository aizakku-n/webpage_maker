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
parser.add_argument('-j', '--json', dest='json', default='',
                    help='json file')
parser.add_argument('-', '--', dest='', default='',
                    help='')
args = parser.parse_args()


if __name__ == '__main__':
    L = []
    keys = ['title','category','detail','size','date','torrent','magnet','image']
    for line in args.input:
        if not line.strip():
            continue
        values = line.strip().split('\t')
        L.append(dict(zip(keys, values)))

    temp = '"itemSource": "<img src=\'{}\' alt='' />【 {} 】<br> added {} <br> {} \
            <br> <a href=\'{}\' onclick=\\"window.open(\'http://hentaimagnet.x.fc2.com/ch.html\')\\">source</a> <br> \
            <a href=\'{}\' onclick=\\"window.open(\'http://hentaimagnet.x.fc2.com/ch.html\')\\" download=\\"{}\\">downlad</a>"'
    # temp = '"itemSource": "<img src=\'{}\' alt='' />【 {} 】"'
    pl = []
    for n, d in enumerate(L):
        pl.append("{" + '"itemNum": "{}",'.format(n+1)
         # + temp.format(d['image'], d['title']) + "}")
         + temp.format(d['image'], d['title'], d['date'], d['category'], d['detail'], d['torrent'], d['title']) + "}")

    print('[\n' + ',\n'.join(pl) + '\n]')
