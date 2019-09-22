"""
Script for cleaning text before clustering.
Like removing stop words, stemming if necessary, etc.
"""
from nltk.stem import PorterStemmer, WordNetLemmatizer
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS

def __lemmatize_token(token):
    """
    Stems nouns and verbs
    """
    stemmer = PorterStemmer()
    return stemmer.stem(WordNetLemmatizer().lemmatize(token, pos='v'))

def __preprocess_gensim(text):
    """
    Tokenizes text and removes stop words
    """
    result = []
    for token in set(simple_preprocess(text)):
        if token not in STOPWORDS and len(token) > 3:
            result.append(token)

    return result

def clean_segments(segments):
    """
    Removes all stop words from a list of text segments.
    The stop_words are defined in the file stop_words.txt with a new line between each stop word.
    After stop word cleaning the remaining words are tokenized and returned as an array.
    """
    return [__preprocess_gensim(s) for s in segments]
