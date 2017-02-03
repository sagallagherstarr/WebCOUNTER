#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 20:33:14 2017

@author: scott
"""

from flask import abort
from flask.ext.marcopolo import (MarcoPolo,
                                 route,
                                 flash_error,
                                 flash_success,
                                 flash_info,
                                 set_cookie,
                                 get_cookie)


class Index(MarcoPolo):
    route_base = "/editors"

    def index(self):
        return self.render()
    
    def SUSHIEndpoints(self):
        return self.render()
