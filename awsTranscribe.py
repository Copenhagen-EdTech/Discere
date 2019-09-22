# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 19:28:30 2019

@author: August
"""

import boto3


s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
        print(bucket.name)