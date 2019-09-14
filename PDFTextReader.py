from tika import parser

def parse_pdf(path):
    """
    Parses a pdf to string. Reads the pdf from the given path
    """
    raw = parser.from_file(path)
    return raw['content']
