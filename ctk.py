
import customtkinter as ctk
import tkinter.font as tkfont
from PIL import Image, ImageTk
from customtkinter import CTkImage
from file_to_voice import get_file

ctk.set_appearance_mode("light")  # Modes: system (default), light, dark
#ctk.set_default_color_theme("dark-blue") # Themes: blue (default), dark-blue, green

##f6eee3 eee7d7	e5decf e5cbba d9bda5
window= ctk.CTk()
window.title("Audio reader")
window.geometry("600x600")
frame= ctk.CTkCanvas(window, background='#e5decf' )

image=Image.open("Logo2.jpg")
cin=ctk.StringVar()
entry= ctk.CTkEntry(frame, textvariable=cin)

frame.rowconfigure((0,1,2,3,4,5,6,7,8), uniform='a', weight=1)
frame.columnconfigure((0,1,2,3,4,5,6,7,8), uniform='a', weight=1)

label=ctk.CTkLabel(frame, text='Enter the name of the book', anchor="center", font=("Calibri", 24))


def second_page():
    entry.grid(row=4, column=1, sticky='ew', columnspan=7)
    button.configure(text="Continue", command= lambda: get_file(cin.get()))
    label.grid(row=3, column=1, sticky='nsew', columnspan=7)
    quote.destroy()
    quote2.destroy()
    
    
    
    
    

button=ctk.CTkButton(frame, text="Start Here", command=second_page)

quote=ctk.CTkLabel(frame, text='"A reader lives a thousand lives before he dies....', anchor="center", font=("Calibri", 24))
quote2=ctk.CTkLabel(frame, text='The man who never reads lives only one."', anchor="center", font=("MS Serif", 24))



button.grid(row=5, column=3, sticky='nsew', columnspan=3)

quote.grid(row=7, column=0, columnspan=9, rowspan=1)
quote2.grid(row=8, column=0, columnspan=9, rowspan=1)


frame.pack(expand=True, fill='both' )






# ensures image is always in the same resolution

def image_resize(event):
    global ctk_image, image
    ctk_image = CTkImage(dark_image=image, light_image=image,  size=(event.width, event.height/3))
    imagel=ctk.CTkLabel(frame, text="", image=ctk_image, anchor="nw" )
    imagel.grid(row=0, column=0, columnspan=9, rowspan=3, sticky='nsew')
    

    
frame.bind('<Configure>', image_resize)


window.after(10*1000, window.quit)
window.mainloop()