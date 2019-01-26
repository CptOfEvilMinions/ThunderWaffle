import PyPDF2 
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from pathlib import Path
import argparse

def extract_text(filename):
    # Open allows you to read the file
    pdfFileObj = open(filename,'rb')

    page_count = int()
    pdfReader = None

    try:
        # The pdfReader variable is a readable object that will be parsed
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        # Get PDF page count
        page_count = pdfReader.numPages
        
    except Exception as e:
        print ("Could not read PDF: {0}".format(e))
        pdfFileObj.close()
        return None

    pdfText = str()

    # Extract text from each page
    for page_num in range(0, page_count):
        pageObj = pdfReader.getPage(page_num)
        pdfText += pageObj.extractText()

    
    # Close file
    pdfFileObj.close()

    # Return PDF text
    return pdfText

def main():
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--path", required=True, help="Path to PDFs")
    ap.add_argument("-k", "--keyword", required=True, help="keyword to search for")
    args = vars(ap.parse_args())

    print ("Path: {0}".format(args['path']))
    print ("Keyword: {0}".format(args['keyword']))

    # Generate a list of PDFs in directory
    result = list(Path(args['path']).rglob("*.[pP][dD][fF]"))

    # Create filehandle
    keyword_file = open('{0}.txt'.format(args['keyword']), 'w')

    for filename in result:
        print (filename)
        pdfText = extract_text(filename)

        if (pdfText != None) and (args['keyword'] in pdfText):
            keyword_file.write(str(filename) + '\n')

    # Close file
    keyword_file.close()
        

main()