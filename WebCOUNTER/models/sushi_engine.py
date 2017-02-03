#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 19:28:59 2017

@author: scott
"""

import datetime

from mongoengine import *

from base_model import *

class SUSHIEngine(BaseDocument):
    schema_revision =    ReferenceField(SchemaVersion)
    
    entry_name =         StringField(unique=True)
    
    vendor_name =        StringField(required)
    
    wsdl_url =           URLField(default="http://google.com/", required=True, verbose_name="WSDL URL")
    requestor_id =       StringField(default="", verbose_name="Requestor ID")
    requestor_email =    EmailField(required=False, verbose_name="Requestor Email")
    requestor_name =     StringField(default="", verbose_name="Requestor Name")
    customer_reference = StringField(default="", verbose_name="Customer Reference")
    customer_name =      StringField(default="", verbose_name="Customer Name")
    reports_available =  SortedListField(StringField(default=""), verbose_name="COUNTER Reports Available")
    release =            StringField(default="R4", choices=("R3", "R4"), verbose_name="COUNTER Release")
    
