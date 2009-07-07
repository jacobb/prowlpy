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
        h = httplib2.Http(".cache")
        h.add_credentials(self.username,self.password)
        headers = {'User-Agent': "ProwlScriptPy/%s" % str(VERSION)}
        
        application = urllib.quote(str(application))
        event = urllib.quote(str(event))
        desciption = urllib.quote(str(description))
        
        resp,content = h.request("https://prowl.weks.net/api/add_notification.php?application=%s&event=%s&description=%s" \
                                    % (application, event, description))

        if(resp['status']=='200'):
            print "Success!"
        elif(resp['status']=='401'): 
            print "Auth Failed"
        else:
            print "Failed"