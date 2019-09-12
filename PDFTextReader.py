#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: younessubhi
"""

from tika import parser

## insert document pathname
raw = parser.from_file('/Users/younessubhi/Documents/GitHub/Discere/pdf files/deep-image-reconstruction-human-brain.pdf')
print(raw['content'])
