#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 01:12:49 2018

@author: jprieto
"""

import json, urllib


dataset = 'S6'
GPSstart = 825155213   # start of S5
GPSend   = 825232014   # end of S5
detector = 'H1'

urlformat = 'https://losc.ligo.org/archive/links/{0}/{1}/{2}/{3}/json/'
url = urlformat.format(dataset, detector, GPSstart, GPSend)
print "Tile catalog URL is ", url

r = urllib.urlopen(url).read()    # get the list of files
tiles = json.loads(r)             # parse the json

print tiles['dataset']
print tiles['GPSstart']
print tiles['GPSend']

output_list = open('files', 'w')
for file in tiles['strain']:
    if file['format'] == 'hdf5':
        print "found file from ", file['UTCstart']
        print>>output_list, file['url']

output_list.close()