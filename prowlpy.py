# -*- coding: utf-8 -*-
"""
Prowlpy V0.3

Written by Jacob Burch, 7/6/2009

Python module for posting to the iPhone Push Notification service Prowl: http://prowl.weks.net/
"""
__author__ = 'jacobburch@gmail.com'
__version__ = 0.3

import httplib2
import urllib

API_DOMAIN = 'https://prowl.weks.net/publicapi'

class Prowl(object):
    def __init__(self, apikey, username=None, password=None):
        self.apikey = apikey
        self.username = username #Currently not in use
        self.password = password #Currently not in use
        
    def post(self, application=None, event=None, description=None):
        # Create the http object
        h = httplib2.Http(".cache")
        #h.add_credentials(self.username,self.password)
        
        # Set User-Agent
        headers = {'User-Agent': "Prowlpy/%s" % str(__version__)}
        
        # URL-encode and string-ify keywords. Better type/content testing is needed here
        application = urllib.quote(str(application))
        event = urllib.quote(str(event))
        description = urllib.quote(str(description))
        
        verify_resp,verify_content = h.request("%s/verify?apikey=%s" % \
                                                    (API_DOMAIN,self.apikey))
        
        if verify_resp['status'] != '200':
            raise Exception("Invalid API Key %s" % verify_content)
        
        # Perform the request and get the response headers and content
        resp,content = h.request("%s/add?application=%s&event=%s&description=%s&apikey=%s" \
                                    % (API_DOMAIN,application, event, description,self.apikey))
        url = "%s/add?application=%s&event=%s&description=%s&apikey=%s" \
                % (API_DOMAIN,application, event, description,self.apikey)
        
        if resp['status'] == '200':
            return True
        elif resp['status'] == '401': 
            raise Exception("Auth Failed %s" % url)
        else:
            raise Exception("Failed")