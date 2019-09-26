from tika import parser
from bs4 import BeautifulSoup as bso
import pdftotree
#pdfminer
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LTTextBoxHorizontal

#pypdf2
from PyPDF2 import PdfFileReader

def parse_pdf(path):
    """
    Parses a pdf to string. Reads the pdf from the given path
    """
    raw = parser.from_file(path, xmlContent=True)
    soup = bso(raw['content'], 'lxml')
    pages = soup.find_all('div', attrs={'class': 'page'})
    print(pages)
    return pages

def tree_pdf(path):
    tree = pdftotree.parse(path)
    print(tree)

def mine_pdf(path):
    processed_pages = []
    # Open a PDF file.
    with open(path, 'rb') as fp:
        document = open(path, 'rb')
        #Create resource manager
        rsrcmgr = PDFResourceManager()
        # Set parameters for analysis.
        laparams = LAParams()
        # Create a PDF page aggregator object.
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.get_pages(document):
            interpreter.process_page(page)
            #receive the LTPage object for the page.
            layout = device.get_result()
            for element in layout:
                if isinstance(element, LTTextBoxHorizontal):
                    element.analyze()
                    print(element.get_text())

def pypdf2_parse(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        print('Info')
        print(info)

        page = pdf.getPage(1)
        print(page.extractText())

if __name__ == '__main__':
    mine_pdf('deep.pdf')
