#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 19:26:05 2017

@author: scott
"""
import datetime

from mongoengine import *

class BaseModel(Document):
    meta = {
        'abstract': True,
    }

class SchemaVersion(Document):
    schema_version_id = StringField()
    
    # allows us to find the most recent revision
    revision_date_time = DateTimeField(default=datetime.datetime.now())