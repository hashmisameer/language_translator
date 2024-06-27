import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from googletrans import Translator
from tkinter import messagebox
import os

# UI is developed using Tkinter library
root = tk.Tk()
root.title('Language Translator')
root.geometry('1060x660')
root.maxsize(1060, 660)
root.minsize(1060, 660)

# Title bar icon image used in Tkinter GUI
title_bar_icon = PhotoImage(file="resources/icons/translation.png")
root.iconphoto(False, title_bar_icon)
cl = ''
output = ''

# For Performing Main Translation Function
def translate():
    language_1 = t1.get("1.0", "end-1c")
    global cl
    cl = choose_language.get()

    if language_1 == '':
        messagebox.showerror('Language Translator', 'Please fill the Text Box for Translation')
    else:
        t2.delete(1.0, 'end')
        translator = Translator()
        global output

        src_lang = auto_detect.get()
        if src_lang == 'Auto Detect':
            src_lang = 'auto'
        else:
            src_lang = lang_dict[src_lang]

        dest_lang = lang_dict[cl]
        output = translator.translate(language_1, src=src_lang, dest=dest_lang)
        output = output.text
        t2.insert('end', output)

# For Clearing Textbox Data
def clear():
    t1.delete(1.0, 'end')
    t2.delete(1.0, 'end')

# Background Image settings using Tkinter
img = ImageTk.PhotoImage(Image.open('translator.png'))
label = Label(image=img)
label.place(x=0, y=0)

# Language dictionary for language code mapping
lang_dict = {
    'Auto Detect': 'auto',
    'Arabic': 'ar',
    'English': 'en',
    'Hindi': 'hi',
    'Kannada': 'kn',
    'Urdu': 'ur',
}

# Combobox for from-language selection
a = tk.StringVar()
auto_detect = ttk.Combobox(root, width=20, textvariable=a, state='readonly', font=('Corbel', 20, 'bold'))
auto_detect['values'] = list(lang_dict.keys())
auto_detect.place(x=50, y=140)
auto_detect.current(0)

l = tk.StringVar()
# Combobox for to-language selection
choose_language = ttk.Combobox(root, width=20, textvariable=l, state='readonly', font=('Corbel', 20, 'bold'))
choose_language['values'] = list(lang_dict.keys())[1:]  # Exclude 'Auto Detect' for destination languages
choose_language.place(x=600, y=140)
choose_language.current(0)

# Load and resize the icon images for buttons
translate_text_icon_img = Image.open("resources/icons/documents.png")
resized_translate_text_icon = translate_text_icon_img.resize((32, 32), Image.Resampling.LANCZOS)
translate_text_icon = ImageTk.PhotoImage(resized_translate_text_icon)

clear_text_icon_img = Image.open("resources/icons/eraser.png")
resized_clear_text_icon = clear_text_icon_img.resize((32, 32), Image.Resampling.LANCZOS)
clear_text_icon = ImageTk.PhotoImage(resized_clear_text_icon)

# Text Widget settings used in Tkinter GUI
t1 = Text(root, width=45, height=13, borderwidth=0, relief=RIDGE, font=('Calibri', 16))
t1.place(x=20, y=200)
t2 = Text(root, width=45, height=13, borderwidth=0, relief=RIDGE, font=('Calibri', 16))
t2.place(x=550, y=200)

# Button settings used in Tkinter GUI
translate_button = Button(root, text=" Translate Text ", image=translate_text_icon, compound="right", relief=RIDGE,
                          borderwidth=0, font=('Corbel', 20, 'bold'), cursor="hand2",
                          command=translate, bg="#ffffff")
translate_button.place(x=40, y=565)

clear_button = Button(root, text=" Clear ", image=clear_text_icon, compound="right", relief=RIDGE, borderwidth=0,
                      font=('Corbel', 20, 'bold'), cursor="hand2",
                      command=clear, bg="#ffffff")
clear_button.place(x=270, y=565)


root.mainloop()
