#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 12:19:15 2020

@author: yousefnami
"""

def finder(target,input_list):
    for current in input_list:
        if current == target:
            return target
        else:
            return "Target not found"