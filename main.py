"""
Main module for Discere.
"""
import sys
from PDFTextReader import parse_pdf

def main():
    """
    Main file for Discere
    """

    if len(sys.argv) < 2 or not isinstance(sys.argv[1], str):
        print("You need to provide a path for a pdf file")

    path = sys.argv[1]
    raw_pdf = parse_pdf(path)
    print(raw_pdf)

if __name__ == '__main__':
    main()
