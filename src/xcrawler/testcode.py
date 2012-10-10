# -*- coding:utf-8 -*-
import urllib
import sys
import chardet
from chardet.universaldetector import UniversalDetector

def test_website(website):
    preaddr="http://"
    if not preaddr in website:
        website=preaddr+website 
    try:
        sock = urllib.urlopen(website)
    except:
        return None
    detector = UniversalDetector()
    for line in sock.readlines():
        detector.feed(line)
        if detector.done:
            break
    detector.close()
    sock.close()
    result = detector.result
    return result['encoding']
 
def test_files(self,filenames):
    try:
        f = open(filenames)
    except:
        return None
    detector = UniversalDetector()
    for line in f.readlines():
        detector.feed(line)
        if detector.done:
            break
    detector.close()
    f.close()
    result = detector.result
    return result['encoding']

