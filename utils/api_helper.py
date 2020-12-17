import logging
import pdb
import json
import requests
import utils.custom_logger as cl
class ApiHelper():
    log=cl.customLogger(logging.DEBUG)
    def __init__(self,apikey):
        self.apikey=apikey

    def get(self,uri,params=None,header=None):
        try:
            if not header:
                header={}
                header["Content-Type"]="application/json"
                header["Authorization"]=self.apikey
            response=requests.get(url=uri,params=params,headers=header)
            if(response.status_code==200):
                return response.json()
            else:
                self.log.info("the requested url is not successful please check the url and params " + uri + " " + str(params))
                self.log.info("response received is " + res.json())
        except:
            self.log.error("unable to perform get call for url " + uri + " params " + str(params))

    def post(self,uri,payload=None,header=None):
        try:
            if not header:
                header = {}
                header["Content-Type"] = "application/json"
                header["Authorization"] = self.apikey
                header['Accept']= 'text/plain'
            res = requests.post(url=uri,json=payload,headers=header)
            #here ideally it should be 201 status code
            if(res.status_code==200):
                self.log.info("the requested url is successful")
                return res.json()
            else:
                self.log.info("the requested url is not successful please check the url and params " + uri + " " + str(payload))
                self.log.info("response received is "+res.json())
        except Exception as e:
            self.log.error("unable to perform post call bcoz of "+e)

    def put(self,uri,payload=None,header=None):
        try:
            if not header:
                header = {}
                header["Content-Type"] = "application/json"
                header["Authorization"] = self.apikey
                header['Accept']= 'text/plain'
            res = requests.put(url=uri,json=payload,headers=header)
            #here ideally it should be 201 status code
            if(res.status_code==200):
                self.log.info("the requested url is successful")
                return res.json()
            else:
                self.log.info("the requested url is not successful please check the url and params " + uri + " " + str(payload))
                self.log.info("response received is " + res.json())
        except Exception as e:
            self.log.error("unable to perform post call bcoz of "+e)

