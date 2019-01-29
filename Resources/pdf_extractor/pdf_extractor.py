import PyPDF2 
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

    try:
        # Extract text from each page
        for page_num in range(0, page_count):
            pageObj = pdfReader.getPage(page_num)

            pdfText += pageObj.extractText()
    except Exception as e:
        print ("Could not read PDF: {0}".format(e))
        pdfFileObj.close()
        return None

    
    # Close file
    pdfFileObj.close()

    # Return PDF text
    return pdfText

# Generate a list of file paths for PDFs in a directory
def generate_list_of_pdfs(dir_path):
    return list(Path(dir_path).rglob("*.[pP][dD][fF]"))

# Create a set of keywords from text file
def create_keywords_list(file_path):
    kFile = open(file_path, 'r')

    # Return a set of keywords
    return set([keyword.lower().strip() for keyword in kFile.readlines()])


# Output PDFs that contain keyword
# [keyword]
# <PDF file path>
# <PDF file path>
def pretty_print_file(file_dict, filename):
    pdf_file = open(filename, 'w')

    # For each key value pair in dictonary
    for key, values in file_dict.items():
        # Write key heading
        pdf_file.write( "[{0}]\n".format(key) )

        # Write values under heading
        for value in values:
            pdf_file.write( "{0}\n".format(value) )

        # New line spacing between headers
        pdf_file.write( "\n\n")

    # Close file
    pdf_file.close()


def add_pdf_to_dict(keyword, pdfText, file_dict, pdf_file_path):
    if keyword in pdfText: 
        print ("[+] Added {0} to [{1}] section".format(str(pdf_file_path), keyword))

        # Add PDF file path to dict
        # If keyword exists
        if keyword in file_dict:
            file_dict[keyword].append( str(pdf_file_path) )
        else:
            file_dict[keyword] = [str(pdf_file_path)]

def search_pdfs(file_dict, list_of_pdfs, keyword_set):
     for pdf_file_path in list_of_pdfs:
        print (pdf_file_path)

        # Extract test from PDF
        pdfText = extract_text(pdf_file_path)

        # If pdfTest is None then move to next file
        if pdfText == None:
            continue
        
        # Make sure all the text is lowercase
        pdfText = pdfText.lower()

        # Iterate over keywords and see if keyword exists in PDFtext
        for keyword in keyword_set:
            add_pdf_to_dict(keyword, pdfText, file_dict, pdf_file_path)


def main():
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--path", required=True, help="Path to PDFs")
    ap.add_argument("-f", "--file", required=True, help="File containing keywords")
    ap.add_argument("-o", "--output",required=True, help="Output file")
    args = vars(ap.parse_args())
    
    # Print path of PDF directory
    print ("PDF directory: {0}".format(args['path']))

    # Key words
    keyword_set = create_keywords_list(args['file'])
    
    # Generate a list of PDFs in directory
    list_of_pdfs = generate_list_of_pdfs(args['path'])
    
    # Create file_dict
    file_dict = dict()

    # Iterate all PDFs for keywords
    search_pdfs(file_dict, list_of_pdfs, keyword_set)
    
    # Output filedict contents to txt
    pretty_print_file(file_dict, args['output'])

main()