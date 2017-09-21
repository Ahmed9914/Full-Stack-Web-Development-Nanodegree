# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 23:25:35 2017

@author: Ravi Jain
"""
import os
import urllib

def read_text():
    
    quotes = open("movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)
    
def check_profanity(text_to_check):
    address = "http://www.wdylike.appspot.com/?q=" + text_to_check
    print(address)
    connection = urllib.request.urlopen(address)
    output = connection.read()
    print(output)
    connection.close()
    if "true" in output:
        print("Profinity Alert!!!")
    elif "false" in output:
        print("This doc has no curse words")
    else:
        print("Could not scan the document properly")
    
read_text()