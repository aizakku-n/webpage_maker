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
    D = {}
    dl = []
    if args.json:
        f = open(args.json, 'r')
        dl = json.load(f)
        for d in dl:
            if d.get('title'):
                D.setdefault(d.get('title'), 1)

    RL = []
    keys = ['title','category','detail','size','date','torrent','magnet','image']
    for line in args.input:
        values = line.strip('\n').split('\t')
        if values[0] in D:
            continue
        RL.append(dict(zip(keys, values)))

    temp = '"idx":{},"title":"{}","category":"{}","detail":"{}","size":"{}","date":"{}","torrent":"{}","magnet":"{}","image":"{}"'
    idx = 0
    pl = []
    for d in RL + dl:
        pl.append('{'+temp.format(idx,d['title'],d['category'],d['detail'],d['size'],d['date'],d['torrent'],d['magnet'],d['image'])+'}')
        idx += 1

    print('[\n' + ',\n'.join(pl) + '\n]')
