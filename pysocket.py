#!/usr/bin/env python 
# -*- coding: utf-8 -*-
""" 
A simple echo server 
""" 
from flask import jsonify
import os
import json
import httplib
import socket

host = '10.1.1.21' 
port = 50000 
backlog = 5 
size = 2048 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port)) 
s.listen(backlog) 

while 1: 
    client, address = s.accept() 
    print('Connected by',address)
    data = client.recv(size) 
    print(data)
#"""------send GCM----------------------------------------------------------------------------------"""

    API_KEY = ''

    params = {}

    # put the data you want to send to device
    params['data']={ 'message': data}

    # get registration id, this registration id will be mapped to a device.
    regId = ["", "", .................]

    params['registration_ids']=regId
    params = json.JSONEncoder().encode(params)

    headers = { "Content-type": "application/json","Authorization": "key="+API_KEY}

    conn = httplib.HTTPSConnection("android.googleapis.com") 

    # method,url,body,header
    conn.request('POST','/gcm/send', params, headers)
    res = conn.getresponse()

    conn.close() 
    result = {'msg':res.status}
       
    print(result)

    client.close()


