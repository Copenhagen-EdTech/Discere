from tika import parser
from bs4 import BeautifulSoup as bso

def parse_pdf(path):
    """
    Parses a pdf to string. Reads the pdf from the given path
    """
    raw = parser.from_file(path, xmlContent=True)
    soup = bso(raw['content'], 'lxml')
    pages = soup.find_all('div', attrs={'class': 'page'})
    print(pages)
    return pages

if __name__ == '__main__':
    parse_pdf('course_Book.pdf')
