"""
Module for segmenting text streams into documents based on headers
"""

def segment(text):
    """
    Segments the text file at the given path
    """
    segments = text.split('\n\n\n')
    print("Segments length: " + str(len(segments)))
    return segments
