# -*- coding: utf-8 -*-
"""
Prowlpy V0.4.1

Written by Jacob Burch, 7/6/2009

Python module for posting to the iPhone Push Notification service Prowl: http://prowl.weks.net/
"""
__author__ = 'jacobburch@gmail.com'
__version__ = 0.41

import httplib2
import urllib

API_DOMAIN = 'https://prowl.weks.net/publicapi'

class Prowl(object):
    def __init__(self, apikey):
        """
        Initialize a Prowl instance.
        """
        self.apikey = apikey
        
        # Aliasing
        self.add = self.post
        
    def post(self, application=None, event=None, description=None,priority=0):
        # Create the http object
        h = httplib2.Http()
        
        # Set User-Agent
        headers = {'User-Agent': "Prowlpy/%s" % str(__version__)}
        
        # Perform the request and get the response headers and content
        data = {
            'apikey': self.apikey,
            'application': application,
            'event': event,
            'description': description,
            'priority': priority

        }
        headers["Content-type"] = "application/x-www-form-urlencoded"
        resp,content = h.request("%s/add/" % API_DOMAIN, "POST", headers=headers, body=urllib.urlencode(data))
        
        if resp['status'] == '200':
            return True
        elif resp['status'] == '401': 
            raise Exception("Auth Failed: %s" % content)
        else:
            raise Exception("Failed")
        
    
    def verify_key(self):
        h = httplib2.Http()
        headers = {'User-Agent': "Prowlpy/%s" % str(__version__)}
        verify_resp,verify_content = h.request("%s/verify?apikey=%s" % \
                                                    (API_DOMAIN,self.apikey))
        if verify_resp['status'] != '200':
            raise Exception("Invalid API Key %s" % verify_content)
        else:
            return True