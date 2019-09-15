"""
Main module for Discere.
"""
import sys
from PDFTextReader import parse_pdf
from Segmentation import segment
from SegmentCleaner import clean_segments

def main():
    """
    Main file for Discere
    """

    if len(sys.argv) < 2 or not isinstance(sys.argv[1], str):
        print("You need to provide a path for a pdf file")

    path = sys.argv[1]
    raw_pdf = parse_pdf(path)
    segments = segment(raw_pdf)
    clean_segments(segments)

if __name__ == '__main__':
    main()
