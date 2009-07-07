# -*- coding: utf-8 -*-
"""
Prowlpy V0.2

Written by Jacob Burch, 7/6/2009

Python module for posting to the iPhone Push Notification service Prowl: http://prowl.weks.net/

from prowlpy import Prowl
"""

import httplib2
import urllib
__author__ = 'jacobburch@gmail.com'
__version__ = 0.2

class Prowl(object):
    def __init__(self,username,password):
        self.username = username
        self.password = password
    
    def post(self,application=None,event=None,description=None):
        # Create the http object
        h = httplib2.Http(".cache")
        h.add_credentials(self.username,self.password)
        
        # Set User-Agent
        headers = {'User-Agent': "ProwlScriptPy/%s" % str(VERSION)}
        
        # URL-encode and string-ify keywords. Better type/content testing is needed here
        application = urllib.quote(str(application))
        event = urllib.quote(str(event))
        desciption = urllib.quote(str(description))
        
        # Perform the request and get the response headers and content (Content should be blank for now)
        resp,content = h.request("https://prowl.weks.net/api/add_notification.php?application=%s&event=%s&description=%s" \
                                    % (application, event, description))
        
        if(resp['status']=='200'):
            return = True
        elif(resp['status']=='401'): 
            raise Exception("Auth Failed")
        else:
            raise Exception("Failed")