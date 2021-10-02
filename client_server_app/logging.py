# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 19:43:18 2021

@author: danie
"""

#Import libraries
from datetime import datetime

#Define classes
def log(logs):
    now = datetime.now().strftime("%H:%M:%S")
    print("{} || {}".format(now, logs))