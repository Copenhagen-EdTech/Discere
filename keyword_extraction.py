#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:16:15 2019

@author: younessubhi
"""

import pandas as pd
import numpy as np
import PyPDF2
import textract
import re

filename = 'deep.pdf'

# open and read file
pdfFileObj = open(filename,'rb')

# equal to parse_pdf
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# discerning the number of pages will allow to parse through all the pages
num_pages = pdfReader.numPages

count = 0
text = ''

# while loop to read each page
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count += 1
    text += pageObj.extractText()
    
# check if above returned words (in case PDF wasn't readable)
# otherwise use textract to analyse

if text != '':
    text = text
else:
    text = textract.process('http://bit.ly/epo_keyword_extraction_document',
                            method='tesseract', language='eng')

# now we have a text variable which contains all the text derived from the PDF

### EXTRACTING KEYWORDS ###
    
keywords = re.findall(r'[a-zA-Z]\w+',text)
# total keywords in document
len(keywords)

# df with unique keywords to avoid repetition in rows
df = pd.DataFrame(list(set(keywords)),columns=['keywords'])

## CALCULATING WEIGHTAGE OF KEYWORDS ##
# we use TD-IDF again...
def weightage(word, text, number_of_documents=1):
    word_list = re.findall(word,text)
    number_of_times_word_appeared = len(word_list)
    tf = number_of_times_word_appeared/float(len(text))
    idf = np.log((number_of_documents)/float(number_of_times_word_appeared))
    tf_idf = tf*idf
    return number_of_times_word_appeared, tf, idf, tf_idf

df['number_of_times_word_appeared'] = df['keywords'].apply(lambda x: weightage(x,text)[0])
df['tf'] = df['keywords'].apply(lambda x: weightage(x,text)[1])
df['idf'] = df['keywords'].apply(lambda x: weightage(x,text)[2])
df['tf_idf'] = df['keywords'].apply(lambda x: weightage(x,text)[3])

