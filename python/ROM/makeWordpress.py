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

url_base = 'http://hentaimagnet.x.fc2.com/ROM/?id={}'
alpha = re.compile('[a-zA-Z]')
kakko = re.compile('\(.*\)')

if __name__ == '__main__':
    T = dict()
    I = ''
    for line in args.input:
        if not line.strip():
            continue
        d = {}
        for e in line.strip().split('\t'):
            k, v = e.split(':', 1)
            d.setdefault(k, v)
        T.setdefault(kakko.sub('', d['title']).strip().replace('-','').replace('  ',' '), d['title'])
        inital = d['title'][0]
        if alpha.match(inital) and not I != inital:
            I = inital

        print('<a href="{}">{}</a><br>'.format(url_base.format(d['id']), d['title']))


    print('\nGame Boy Advance\n')
    print('Download retro video games rom, iso, or zip. Our site listed up many kinds of rom on NES, SNES, N64, GBA, PS, PSP, and so on.\n')
    seo_key = 'snes,スーファミ,スーパーファミコン,gba,game boy advance,rom,iso,free,donwload,rar,torrent,zip,{}'
    print(seo_key.format(','.join(T.keys())))
