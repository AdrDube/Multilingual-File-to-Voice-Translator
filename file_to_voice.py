
from PyPDF2 import PdfReader
import sys
from gtts import gTTS
from deep_translator import GoogleTranslator
from goslate import Goslate
import time
from langdetect import detect

def main():
    if len(sys.argv)>1:
         file_name=sys.argv[1]+".pdf"
    else:
         file_name=(input("Enter your file name ")).strip()+".pdf"
    num=int(input("Enter the page you would like to start with "))
    page=get_Content(file_name, num)
    str_to_voice(page, f'{file_name[:-4]}{num}')


def get_Content(f, n=0):
    '''
    Extracts text on the specific page number highlighted
    Returns the text found on said page as str.
    If page in another language, translation is also created as a txt file
    :param f: Name of file
    :type f: str
    :param n: Page number requested
    :type n: integer
    :sys.exit if FileNotFoundError 
    :return: Text found on pagenumber page
    :rtype: str
    '''
    reader = get_file(f)
    page = reader.pages[n]
    content = page.extract_text().strip()
    
    if not content:
        return None
    if not is_eng(content):
        content= translate(content)
        str_to_text(content,f[:-4], n )

    return content

    

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


# def jump_preface(f):
    '''
    finds the preface of the book and asks if user wants to skip to it.
    Returns prefix index or 0

    :param f: Name of file
    :type f: str
    :sys.exit if FileNotFoundError 
    :return: prefix index or 0
    :rtype: integer
    '''
    count=0
    reader = get_file(f)
    

def str_to_voice(str, audio_name):
    '''
    Takes string and audio name as parameter and outputs audio file
    :param str: Name of string
    :type str: str
    :param audio_name: Name of audio file to be created
    :type str: str
    :return: audio_name.mp3
    '''
    
    tts = gTTS(str,  tld='com.ng')
    tts.save(f'{audio_name}.mp3')

def translate(str):
    '''
    Takes string and outputs translation as a string
    :param str: Name of string
    :type str: str
    :return: translated text
    :rtype: string
    '''
    gs = Goslate(service_urls=['http://translate.google.de'])
    return GoogleTranslator().translate(str)
    

def str_to_text(str, name, pagenum):
    try:
        with open(f'{name}.txt', 'x') as f:
            f.write(str)
            f.write(f'\n{pagenum}\n')
    except FileExistsError:
         pass


def is_eng(str):
     gs = Goslate()
     if detect(str)=='en':
         return True
     return False
     '''
     if gs.detect(str)=='en':
         return True
     return False
     '''

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

def midpoint(f):
    return len(get_file(f).pages) // 2



if __name__ == '__main__':
    main()