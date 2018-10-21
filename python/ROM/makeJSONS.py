# -*- coding: utf-8 -*-

import time
import re
import os
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
# from progressbar import ProgressBar
import sys
import argparse
import json
import string

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', dest='input', type=argparse.FileType('r'), default=sys.stdin,
                    help='input file (json)')
parser.add_argument('-o', '--output', dest='output', nargs='?', type=argparse.FileType('w'), default=sys.stdout,
                    help='output file')
parser.add_argument('-j', '--json', dest='json', default='',
                    help='json file')
parser.add_argument('-d', '--dir', dest='dir', default='~/Desktop/json_rom',
                    help='')
args = parser.parse_args()


if __name__ == '__main__':
    L = []
    for line in args.input:
        if not line.strip():
            continue
        d = {}
        for e in line.strip().split('\t'):
            k, v = e.split(':', 1)
            d.setdefault(k, v)
        L.append(d)


    path = args.dir.replace("~", os.path.expanduser("~"))
    if not os.path.exists(path):
        os.mkdir(path)


    for n, d in enumerate(L):
        file_name = d.get('id')
        if file_name:
            with open(path+'/{}.json'.format(file_name), 'w') as fo:
                e = dict()
                if not d.get('image'):
                    e.setdefault('image', 'http://hentaimagnet.x.fc2.com/ROM/img/no_image.png')
                e.update(d)
                json.dump([e], fo, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
