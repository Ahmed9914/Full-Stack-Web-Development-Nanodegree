# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 22:38:17 2017

@author: Ravi Jain
"""

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACc2428161980599d05156a64ba4f8b004"
# Your Auth Token from twilio.com/console
auth_token  = "48baeab577e5d15d9d3dc8ab6e9e3074"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+918289021216", 
    from_="+15593777445",
    body="Hello from Python!")

print(message.sid)