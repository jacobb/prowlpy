#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Copyright (c) 2009, Jaccob Burch
# Copyright (c) 2010, Olivier Hervieu
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
#
# * Neither the name of the University of California, Berkeley nor the
# names of its contributors may be used to endorse or promote products
# derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE REGENTS AND CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 
"""
Prowlpy V0.42 originally written by Jacob Burch, modified by Olivier Hervieu.
 
Python Prowlpy is a python module that implement the public api of Prowl to
send push notification to iPhones.
 
See http://prowl.weks.net for information about Prowl.
 
The prowlpy module respect the API of prowl. So prowlpy provides a Prowl class
which implements two methods :
- post, to push a notification to an iPhone,
- verify_key, to verify an API key.
"""

__author__ = 'Jacob Burch'
__author_email__ = 'jacoburch@gmail.com'
__maintainer__ = 'Olivier Hervieu'
__maintainer_email__ = 'olivier.hervieu@gmail.com'
__version__ = 0.42

from httplib import HTTPSConnection as Https
from urllib import urlencode

API_DOMAIN = 'prowl.weks.net'

class Prowl(object):
    def __init__(self, apikey, providerkey = None):
        """
        Initialize a Prowl instance.
        """
        self.apikey = apikey
       
        # Set User-Agent
        self.headers = {'User-Agent': "Prowlpy/%s" % str(__version__),
                        'Content-type': "application/x-www-form-urlencoded"}

        # Aliasing
        self.add = self.post
        
    def post(   self, application=None, event=None, 
                description=None,priority=0, providerkey = None):
        """
        Post a notification..
         
        You must provide either event or description or both.
        The parameters are :
        - application ; The name of your application or the application
          generating the event.
        - providerkey (optional) : your provider API key.
          Only necessary if you have been whitelisted.
        - priority (optional) : default value of 0 if not provided.
          An integer value ranging [-2, 2] representing:
             -2. Very Low
             -1. Moderate
              0. Normal
              1. High
              2. Emergency (note : emergency priority messages may bypass
                            quiet hours according to the user's settings)
        - event : the name of the event or subject of the notification.
        - description : a description of the event, generally terse.
        """

        # Create the http object
        h = Https(API_DOMAIN)
        
        # Perform the request and get the response headers and content
        data = {
            'apikey': self.apikey,
            'application': application,
            'event': event,
            'description': description,
            'priority': priority
        }

        if providerkey is not None:
            data['providerkey'] = providerkey

        h.request(  "POST",
                    "/publicapi/add",
                    headers = self.headers,
                    body = urlencode(data))
        response = h.getresponse()
        request_status = response.status

        if request_status == 200:
            return True
        elif request_status == 401: 
            raise Exception("Auth Failed: %s" % response.reason)
        else:
            raise Exception("Failed")
        
    def verify_key(self, providerkey = None):
        """
        Verify if the API key is valid.
         
        The parameters are :
        - providerkey (optional) : your provider API key.
          Only necessary if you have been whitelisted.
        """
        h = Https(API_DOMAIN)

        data = {'apikey' : self.apikey}

        if providerkey is not None:
            data['providerkey'] = providerkey

        h.request( "GET",
                    "/publicapi/verify?"+ urlencode(data),
                    headers=self.headers)

        request_status = h.getresponse().status

        if request_status != 200:
            raise Exception("Invalid API Key %s" % self.apikey)
