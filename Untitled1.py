#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests

sender= input("whats your message?/n")
bot_message=""

while bot_message !="bye":
    message = input("whats your message ?\n")
    
    print("sending message now..")
    
    r= request.post('http://localhost:5002/webhooks/rest/webhook',  json={"sender":sender,"message":messasge})
    
    print("bot says ",end="")
    for i in r.json():
        bot_message=i['text']
        print(f"{i['text']}"")

