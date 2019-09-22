#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:19:31 2019

@author: younessubhi
"""

# from PDFTextReader.py import parse_pdf
# import some sort of text

# from freecodecamp.org

# import libraries
import math
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import matplotlib.pyplot as plt

# computeTF computes the term frequency (TF) score for each word in the corpus
# by document
def computeTF(wordDict, bow):
    tfDict = {}
    bowCount = len(bow)
    for word, count in wordDict.items():
        tfDict[word] = count/float(bowCount)
    return tfDict

# computeIDF computes the IDF score of every word in the corpus
def computeIDF(docList):
    import math
    idfDict = {}
    N = len(docList)
    
    idfDict = dict.fromkeys(docList[0].keys(), 0)
    for doc in docList:
        for word, val in doc.items():
            if val > 0:
                idfDict[word] += 1
    
    for word, val in idfDict.items():
        idfDict[word] = math.log10(N / float(val))
        
    return idfDict

# computeTFIDF computes the TF-IDF score for each word,
# by multiplying the TF and IDF scores

def computeTFIDF(tfBow, idfs):
    tfidf = {}
    for word, val in tfBow.items():
        tfidf[word] = val*idfs[word]
    return tfidf

#can also be done using scikit and sklearn
# initialise the
#vectorizer = TfidfVectorizer()
#response = vectorizer.fit_transform([S1, S2])
#tbc
    

### SAMPLE RUN ###
    
docA = "Anden Verdenskrig begyndte i 1939"
docB = 'Hitler startede Anden Verdenskrig'

bowA = docA.split(' ')
bowB = docB.split(' ')

wordSet = set(bowA).union(set(bowB))

wordDictA = dict.fromkeys(wordSet, 0)
wordDictB = dict.fromkeys(wordSet, 0)

for word in bowA:
    wordDictA[word] += 1
    
for word in bowB:
    wordDictB[word] += 1

df_words = pd.DataFrame([wordDictA, wordDictB])

tfBowA = computeTF(wordDictA, bowA)
tfBowB = computeTF(wordDictB, bowB)

idfs = computeIDF([wordDictA, wordDictB])


tfidfBowA = computeTFIDF(tfBowA, idfs)
tfidfBowB = computeTFIDF(tfBowB, idfs)

df_tfidf = pd.DataFrame([tfidfBowA, tfidfBowB])

print(df_tfidf)