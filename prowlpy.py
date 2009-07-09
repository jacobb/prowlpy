# -*- coding: utf-8 -*-
"""
Prowlpy V0.4

Written by Jacob Burch, 7/6/2009

Python module for posting to the iPhone Push Notification service Prowl: http://prowl.weks.net/
"""
__author__ = 'jacobburch@gmail.com'
__version__ = 0.4

import httplib2
import urllib

httplib2.debuglevel = 4
API_DOMAIN = 'https://prowl.weks.net/publicapi'

class Prowl(object):
    def __init__(self, apikey, username=None, password=None):
        self.apikey = apikey
        self.username = username #Currently not in use
        self.password = password #Currently not in use
        
    def post(self, application=None, event=None, description=None):
        
        # Create the http object
        h = httplib2.Http(".cache")
        
        # Set User-Agent
        headers = {'User-Agent': "Prowlpy/%s" % str(__version__)}
        
        # URL-encode and string-ify keywords. Better type/content testing is needed here
        application = urllib.quote(str(application))
        event = urllib.quote(str(event))
        description = urllib.quote(str(description))
        
        
        # Perform the request and get the response headers and content
        data = {
            'application': application,
            'event': event,
            'description': description,
            'apikey': self.apikey
        }
        headers["Content-type"] = "application/x-www-form-urlencoded"
        
        resp,content = h.request("%s/add/" % API_DOMAIN, "POST", headers=headers, body=urllib.urlencode(data))
        if resp['status'] == '200':
            return True
        elif resp['status'] == '401': 
            raise Exception("Auth Failed: %s" % content)
        else:
            raise Exception("Failed")
        
    def add(self, application=None, event=None, description=None):
        """
        Alias for the post function
        Will become the default namespace for adding events by version 1.0
        """
        return self.post(application=application,event=event,description=description)
    
    def verify_key(self):
        h = httplib2.Http(".cache")
        headers = {'User-Agent': "Prowlpy/%s" % str(__version__)}
        verify_resp,verify_content = h.request("%s/verify?apikey=%s" % \
                                                    (API_DOMAIN,self.apikey))
        if verify_resp['status'] != '200':
            raise Exception("Invalid API Key %s" % verify_content)
        else:
            return True