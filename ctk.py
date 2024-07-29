
import customtkinter as ctk
import tkinter.font as tkfont
from PIL import Image, ImageTk
from customtkinter import CTkImage
import ptk
import pygame
from audioplayer import AudioPlayer
global window,frame, label, entry, image, quote, quote2, button, file, cin, box, image_label, page_num
ctk.set_appearance_mode("light")  # Modes: system (default), light, dark
#ctk.set_default_color_theme("dark-blue") # Themes: blue (default), dark-blue, green
##f6eee3 eee7d7	e5decf e5cbba d9bda5
pygame.mixer.init()
def play(page_num):
    pygame.mixer.music.load(f'{page_num}.mp3')
    pygame.mixer.music.play(loops=0)

def get_content(file, page_num):
    content = ptk.get_Content(file, page_num)
    if not ptk.is_eng(content):
        content=ptk.translate(content)
        translation(file,content, page_num)
    ptk.str_to_voice(content, page_num)
    play_button=ctk.CTkButton(frame, text="Play", command=lambda:play(page_num))
    play_button.grid(row=8, column=5, sticky='nsew', columnspan=2)
    pause_button=ctk.CTkButton(frame, text="Pause", command=lambda: pygame.mixer.music.pause())
    pause_button.grid(row=8, column=8, sticky='nesw', columnspan=2)


def translation(file, content, page_num):
    frame.unbind("<Configure>")
    image_label.destroy()
    label.destroy()
    entry.destroy()
   
    button.configure(text="Next Page", command= lambda: get_content(file, page_num+1))
    button.grid(row=8, column=1, columnspan=2)
    box=ctk.CTkTextbox(frame, font= ('Calibri', 18), bg_color='#d9bda5' )
    box.grid(row=1, column=1, columnspan=8, rowspan=7, sticky='nsew')
    box.insert('end', text=content)


def some():
    file = ptk.get_file(cin.get())
    if file:
        third_page(file)

def is_valid_page(file):
    try:
        get_content(file, int(cin.get()))
    except ValueError:
       label.configure(text="Invalid page number")
    except IndexError:
       label.configure(text="Invalid page number")

def image_resize(event):
    global ctk_image, image_label
    ctk_image = CTkImage(dark_image=image, light_image=image,  size=(event.width , event.height/3))
    image_label=ctk.CTkLabel(frame, text="", image=ctk_image, anchor="nw" )
    image_label.grid(row=0, column=0, columnspan=9, rowspan=3, sticky='nsew', )


def second_page():
    entry.grid(row=4, column=1, sticky='ew', columnspan=7)
    button.configure(text="Continue", command=some)
    label.grid(row=3, column=1, sticky='nsew', columnspan=7)
    quote.destroy()
    quote2.destroy()
    
def first_page():
    #image_label.grid(row=0, column=0, columnspan=9, rowspan=3, sticky='nsew')
    button.grid(row=5, column=3, sticky='nsew', columnspan=3)
    quote.grid(row=7, column=0, columnspan=9, rowspan=1)
    quote2.grid(row=8, column=0, columnspan=9, rowspan=1)
    frame.bind('<Configure>', image_resize)

def third_page(file):
    label.configure(text= "What page would you like to start with")
    try:
        button.configure(command=lambda: is_valid_page(file))
    except ValueError:
        pass
    

def invalid():
    label.configure(text="Invalid book. Try again")


window= ctk.CTk()
window.title("Audio reader")
window.geometry("600x600")
frame= ctk.CTkCanvas(window, background='white' )
frame.rowconfigure((0,1,2,3,4,5,6,7,8), uniform='a', weight=1)
frame.columnconfigure((0,1,2,3,4,5,6,7,8), uniform='a', weight=1)
frame.pack(expand=True, fill='both' )
image=Image.open("Logo2.jpg")
cin=ctk.StringVar()


entry= ctk.CTkEntry(frame, textvariable=cin)
label=ctk.CTkLabel(frame, text='Enter the name of the book', anchor="center", font=("Calibri", 24))
button=ctk.CTkButton(frame, text="Start Here", command=second_page)
quote=ctk.CTkLabel(frame, text='"A reader lives a thousand lives before he dies....', anchor="center", font=("Calibri", 24))
quote2=ctk.CTkLabel(frame, text='The man who never reads lives only one."', anchor="center", font=("MS Serif", 24))
first_page()

window.mainloop()



