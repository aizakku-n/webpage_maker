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
            D.setdefault(d.get('title'), 1)

    L = []
    keys = ['title','category','detail','size','date','torrent','magnet','image']
    for line in args.input:
        values = line.strip('\n').split('\t')
        if values[0] in D:
            continue
        L.append(dict(zip(keys, values)))

    temp = '"idx":{},"title":"{}","category":"{}","detail":"{}","size":"{}","date":"{}","torrent":"{}","magnet":"{}","image":"{}"'
    pl = []
    for n, d in enumerate(L + dl):
        pl.append('{'+temp.format(n,d.get('title','None'),d.get('category','None'),
                d.get('detail','None'),d.get('size','None'),d.get('date','None'),
                d.get('torrent','None'),d.get('magnet','None'),d.get('image','None'))
                +'}')
    print('[\n' + ',\n'.join(pl) + '\n]')
