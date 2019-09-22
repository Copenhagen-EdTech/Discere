"""
Main module for Discere.
"""
import sys
from PDFTextReader import parse_pdf
from Segmentation import segment
from SegmentCleaner import clean_segments
from gensim.corpora import Dictionary
from gensim.models import LdaMulticore

def main():
    """
    Main file for Discere
    """

    if len(sys.argv) < 2 or not isinstance(sys.argv[1], str):
        print("You need to provide a path for a pdf file")

    path = sys.argv[1]
    raw_pdf = parse_pdf(path)
    segments = segment(raw_pdf)
    processed_docs = clean_segments(segments)
    dictionary = Dictionary(processed_docs)
    bow = [dictionary.doc2bow(doc) for doc in processed_docs]
    lda_model = LdaMulticore(bow, num_topics = 20, id2word = dictionary,
                            passes = 10, workers = 2)

    print(lda_model.print_topics())

if __name__ == '__main__':
    main()
