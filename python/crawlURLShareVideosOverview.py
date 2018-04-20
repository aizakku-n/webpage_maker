# -*- coding: utf-8 -*-

import time
import re
# from selenium import webdriver
import requests
from bs4 import BeautifulSoup
# from progressbar import ProgressBar
import sys
import argparse

parser = argparse.ArgumentParser()
# parser.add_argument('-i', '--input', dest='input', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                    # help='input file')
# parser.add_argument('-o', '--output', dest='output', nargs='?', type=argparse.FileType('w'), default=sys.stdout,
                    # help='output file')
parser.add_argument('-', '--', dest='', default='',
                    help='')
args = parser.parse_args()


START, END = 1, 2 # 終了地点は4000 @ 2017/01/25
# P = ProgressBar(START, END)


def scraping(url):
    # Selenium settings
    # driver = webdriver.PhantomJS()
    # get a HTML response
    # driver.get(url)
    # html = driver.page_source.encode('utf-8')  # more sophisticated methods may be available
    # parse the response
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    return soup


if __name__ == '__main__':
    URL = "http://share-videos.se/view/new?uid=13&page={}"


    for i in range(START, END):
        # P.update(i)

        url = URL.format(i)
        soup = scraping(url)

        print(soup)

        # flag = False
        # for tr_obj in soup.find_all('tr'):
        #     t = tr_obj.text
        #     if 'No.' in tr_obj.text:
        #         flag = True
        #     elif ('次へ' in t and ">>" in t) or ('前へ' in t and '<<' in t):
        #         final_line = t
        #     elif flag:
        #         L = [x.text for x in tr_obj.find_all('td')]
        #         log_url = tr_obj.find('a')
        #         idx = L[0]
        #         L.append("http://ruru-jinro.net/" + log_url['href'])
        #         print("\t".join(L), file=args.output)
        #
        # if idx == -1 or ("前へ" in final_line and not "次へ" in final_line):
        #     break
        #
        # time.sleep(0.5)
