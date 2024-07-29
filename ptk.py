from PyPDF2 import PdfReader
import sys
from gtts import gTTS
from deep_translator import GoogleTranslator
from goslate import Goslate
import re
import time
from langdetect import detect
import ctk


def get_Content(reader, n=0):
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
    page = reader.pages[n]
    content = clean(page.extract_text().strip())
    if not content:
        ctk.label.configure("That page is blank. Try again")
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
    
#def str_to_textbox(str, name, pagenum):
    '''
    Creates new text file and appends string
   
    :param str: string 
    :type str: str
    :return: 
    :rtype: boolean
    '''
    try:
        with open(f'{name}.txt', 'x') as f:
            f.write(str)
            f.write(f'\n{pagenum}\n')
    except FileExistsError:
         pass

def is_eng(str):
    '''
    Checks if the text is in English
   
    :param str: string 
    :type str: str
    :return: 
    :rtype: boolean
    '''
    gs = Goslate()
    try:
         if detect(str)=='en':
             return True
    except:
        return False
    return False

def get_file(f):
    global window
    '''
    Ensures file is in memory 
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
        ctk.invalid()

def clean(str):
    '''
    Takes a string as input and cleans it up
    :param str: string input
    :type str: str
    :return: clean string
    :rtype: str
    '''
    str = re.sub(r'[^\w\s:.,]','', str)
    str = re.sub(r'^.+', '.', str)
    return re.sub(r'_','', str)




