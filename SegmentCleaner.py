"""
Script for cleaning text before clustering.
Like removing stop words, stemming if necessary, etc.
"""

import string
import re
from nltk.stem import PorterStemmer
from nltk import word_tokenize
from nltk import corpus

def __tokenize_text(text, stem=True):
    """ Tokenize text and stem words removing punctuation """
    text = text.translate(string.punctuation)
    tokens = word_tokenize(text)
    if stem:
        stemmer = PorterStemmer()
        tokens = [stemmer.stem(t) for t in tokens]
    return tokens

def __remove_stop_words(text):
    s_words = corpus.stopwords.words('danish')
    regex = re.compile('('+'|'.join(s_words) + ')')
    return regex.sub("", text)

def clean_segments(segments):
    """
    Removes all stop words from a list of text segments.
    The stop_words are defined in the file stop_words.txt with a new line between each stop word.
    After stop word cleaning the remaining words are tokenized and returned as an array.
    """
    c_seg = [__remove_stop_words(s) for s in segments]
    tokens = [__tokenize_text(cs, False) for cs in c_seg if cs]
    return tokens
