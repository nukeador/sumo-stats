#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
title:          sumo-report.py
description:    Returns translated locales for a given list of SUMO articles
usage:          python sumo-report.py >> file.csv
license:        MPL 2.0
'''

import requests, json
import config

articles = config.articles
apiURL = config.apiURL

# File headers
output = '"Article", "Locales"\n'

for a in articles:
    slug = a.replace('https://support.mozilla.org/en-US/kb/','').replace('/','')
    output += '"' + slug + '",'

    jsonURL = apiURL + slug
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0'}

    jsonData = requests.get(jsonURL, headers=headers)

    try:
        jsonData = jsonData.json()
    except:
        jsonData = None

    if jsonData:
        output += '"' + str(jsonData['locale']) + '",'
    output += '\n'

print output
