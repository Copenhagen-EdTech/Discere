"""
Script for cleaning text before clustering.
Like removing stop words, stemming if necessary, etc.
"""

import string
from nltk.stem import PorterStemmer
from nltk import word_tokenize

def process_text(text, stem=True):
    """ Tokenize text and stem words removing punctuation """
    text = text.translate(string.punctuation)
    tokens = word_tokenize(text)
 
    if stem:
        stemmer = PorterStemmer()
        tokens = [stemmer.stem(t) for t in tokens]
 
    return tokens
