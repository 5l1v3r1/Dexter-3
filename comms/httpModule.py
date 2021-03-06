# httpModule.py
# HTTP client communications module for Dexter.
#


import urllib.request
import string
import socket
import sys
import binascii
import argparse
import json

# Dexter specific imports
from Dexter.comms import commTemplate


class commClass(commTemplate.commTemplate):
    # Init function
    def __init__(self, server, port):
        self.server = server
        self.port = port
        pass

    # Function to query for tasking
    def checkIn(self, dexterData):
        payload = json.dumps(dexterData)
    
        # HTTP POST request setup
        url = 'http://' + str(self.server) + ':' + str(self.port) + '/dexter.html'
        headers = {'User-Agent' : 'Dexter 1.0',
                   'Accept-Encoding' : 'json',
                   'Connection' : 'Close'}
                   
        try:
            req = urllib.request.Request(url, bytes(payload, 'ascii'), headers)
            page = urllib.request.urlopen(req, timeout=20)
            data = page.read()
            response = json.loads(str(data, 'utf-8'))
        except:
            response = {'Status' : 'Failed'}
            
        return response


if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('server', help='address of server')
    parser.add_argument('port', type=int, help='port number of server')
    args = parser.parse_args()
    
    mod = commClass(args.server, args.port)
    response = mod.checkIn({'DEXTERID' : 'TESTTESTTEST'})
    print(response)
    

    pass	