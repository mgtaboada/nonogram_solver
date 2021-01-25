#!/bin/env python3
from bs4 import BeautifulSoup
from urllib.request import urlopen,URLopener
import urllib
import os
import sys
import time
import re
def open_url(url):
    req = urllib.request.Request(
    url,
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36'
    }
    )
    f = urllib.request.urlopen(req)
    time.sleep(1)
    return f.read().decode('utf-8')
def retrieve_url(image_url,filename):

    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)
    # calling urlretrieve function to get resource
    urllib.request.urlretrieve(image_url, filename)
def get_nonogram(url):
    html = open_url(url)
    r  = r"var task = '([^']*)' *;"
    m = re.search(r,html)
    hints_str = ""
    if m:
        hints_str = m[1].split("/")
    dim = len(hints_str)/2
    cols_str = hints_str(hints_str[:dim])
    rows_str = hints_str(hints_str[dim:])
    cols_hints = [[int(i) for i in x.split(".")] for x in cols_str]
    rows_hints = [[int(i) for i in x.split(".")] for x in rows_str]
    return dim,cols_hints,rows_hints
