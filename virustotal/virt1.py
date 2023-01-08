#!/usr/bin/env python
import argparse
import vtapi
import json

default_api_key = "e643d32a0acc90e5377d797b2a788d83e4b5953d22ece0d0929896cae4722c02"

parser = argparse.ArgumentParser()

parser.add_argument('urls', nargs='+', help='List of urls to be scanned')
parser.add_argument('-s', '--scan', action='store_true', help='Scan')
parser.add_argument('-apikey', help='API KEY')

args = parser.parse_args()
print(args)

    
urls = args.urls
toscan = args.scan
apikey = args.apikey

if(apikey==None):
    apikey = default_api_key

#print('urls: '+str(urls)+' toscan: '+str(toscan) + ' apikey: '+str(apikey))
vt = vtapi.Vtapi(urls,apikey,toscan)

resp = vt.get_reputation(0)
json_string = json.dumps(resp, indent=4)
print(json_string)
