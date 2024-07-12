import pyttsx3, PyPDF2
from PyPDF2 import PdfReader
import sys
'''
1) Program extracts relevant data. Shows the title, author, creator, produv
2) If language used is not English, convert the book to English and return a pdf version
3) Create audio files for each page
'''
'''
pdf= PyPDF2.PDFFileReader(open('book.pdf', 'rb'))
speaker= pyttsx3.init()
for page_num in range(pdfreader.numPages):
    text=pdf.getPage(page_num).extractText()
    clean_text= text.strip().replace('\n', ' ')
    print(clean)
'''
def main():
    if len(sys.argv)>1:
         file_name=sys.argv[1]+".pdf"
    else:
         file_name=(input("Enter your file name ")).strip()+".pdf"
    val = int(input("Skip to preface? 1:yes 2: no"))
    if val==1:
        x= find_preface(file_name)
        if x==-1:
            print("Preface not found")
            print(get_Content(file_name))
        else:
            print(get_Content(file_name, x))
    else:
        print(get_Content(file_name))

def get_Content(f, pagenum=0):
    '''
    Extracts text on the specific page number highlighted
    Returns the text found on said page

    :param f: Name of file
    :type f: str
    :param pagenum: Page requested
    :type pagenum: integer
    :sys.exit if FileNotFoundError 
    :return: Text found on pagenumber pagenum
    :rtype: str
    '''
    reader = get_file(f)
    page = reader.pages[pagenum]
    return (page.extract_text()) 

def get_Info(f):
    '''
    Prints metadata related to the file excluding creation date
    :param f: Name of file
    :type f: str
    :sys.exit if FileNotFoundError 
    :return: None
    :rtype: None
    '''
    reader = get_file(f)
    book_data = reader.metadata
    del(book_data["/CreationDate"])
    print(book_data)

def find_preface(f):
    '''
    finds the preface of the book 
    Returns the page number for where the preface is located

    :param f: Name of file
    :type f: str
    :sys.exit if FileNotFoundError 
    :return: page number where preface located
    :rtype: integer
    '''
    count=0
    reader = get_file(f)
    for i in range(len(reader.pages)):
        page = reader.pages[i]
        if "Preface" in page.extract_text():
            count+=1
            if count==2:
                return i
    return -1

def get_file(f):
    '''
    Ensures file is in .... and 
    Returns the read file if valid 
   
    :param f: Name of file
    :type f: str
    :sys.exit if FileNotFoundError 
    :return: read file
    :rtype: PyPDF2 object
    '''
    try:
        return PdfReader(f)
    except FileNotFoundError:
        sys.exit("File not found. Try again")


if __name__ =="__main__":
    main()


