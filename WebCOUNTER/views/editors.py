#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 20:33:14 2017

@author: scott
"""

import logging
logger = logging.getLogger(__name__)

from autologging import traced, logged

from flask import abort
from flask.ext.marcopolo import (MarcoPolo,
                                 route,
                                 flash_error,
                                 flash_success,
                                 flash_info,
                                 set_cookie,
                                 get_cookie)

@traced
@logged(logger)
class Editors(MarcoPolo):
    def index(self):
        return self.render()
    
    def sushi(self):
        return self.render()
