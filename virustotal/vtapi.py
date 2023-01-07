import requests
import json
import datetime
import datetime
import threading
from cache import cache
import concurrent.futures

class Vtapi:
    baseurl = "https://www.virustotal.com/api/v3/"
    urlurl = baseurl+"urls"
    urlanal = baseurl+"analyses"
    
    def __init__(self, urls:list,apikey:str,scan:bool):
        self.__urls = urls
        self.__apikey = apikey
        self.__scan = scan
        self.lock = threading.Lock()
        
    def __str__(self):
        return f'urls {self.__urls}  apikey {self.__apikey}  scan {self.__scan} '
         
    
    def lock_decorator(func):
        def wrapper(self,*args, **kwargs):
            b = None
            self.lock.acquire()
            try: 
                b = func(self,*args, **kwargs)
            finally:
                self.lock.release()
                return b
        return wrapper
    @lock_decorator
    @cache(filename='cache.pkl', ttl=3600)
    def get_reputation(self,url_index)->dict:
        payload = 'url='+self.__urls[url_index] 

        headers = {
            "X-Apikey": self.__apikey,
            "accept": "application/json",
            "content-type": "application/x-www-form-urlencoded"
        }
 
        response = requests.post(Vtapi.urlurl,data=payload,headers=headers)
        resp = {}
        if(response.status_code != 200):
            return resp 
            
        textjson = json.loads(response.text)
        resptype = textjson.get("data").get("type")
        respid = textjson.get("data").get("id")

        scanurl = f'{Vtapi.urlanal}/{respid}'
        #print("scanurl: "+scanurl)
        response2 = requests.get(scanurl,headers=headers)
        if(response2.status_code != 200):
            return resp 
        text2json = json.loads(response2.text)
        resp['reputation'] = text2json.get("data").get("attributes").get("stats")
        return resp
        
   
    def run_as_threads(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            results = [executor.submit(self.get_reputation, i) for i in range(len(self.__urls))]
        
        executor.shutdown()
        for f in concurrent.futures.as_completed(results):
            print(f.result())