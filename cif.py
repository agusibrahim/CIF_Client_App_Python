#!/usr/bin/env python
__author__ = 'Don'

import requests
import json


def query(host, key, data):
    """
    :param data: This is the information that will be searched
     for in the request
    :return: The data will return a json formatted set of data
    :param key: This is the API key to access the HTTP API of CIF
    :param host: This is the CIF host

    Requests, using the get method returns a list of json formatted strings from the CIF server
    The results of the returned text are split on the newline (\n) character into a list called array
    The array is iterated through where each item is converted using json.loads. The individual key:value
    pairs can then be called
    """
    headers = {'accept': 'application/json'}
    url = ('%sapi?apikey=%s&q=%s' % (host, key, data))
    print url
    results = requests.get(url, verify=False, headers=headers)
    array = results.text.split('\n')
    for result in array:
        if result:
            r = json.loads(result)
            print r['detecttime']


if __name__ == '__main__':

    host = 'https://cif.laelapssecurity.net/'
    key = 'f079399a-28f8-4874-8bc3-b916fb1cd16c'
    data = 'example.com'

    query(host, key, data)