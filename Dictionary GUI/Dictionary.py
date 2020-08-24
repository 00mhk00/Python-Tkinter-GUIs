# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:33:00 2020

@author: HP/MHK
"""

from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import output as output
import translator as translator
import white as white
from PIL import ImageTk, Image
from PyDictionary import PyDictionary
from googletrans import Translator

root = tk.Tk()
root.title('Dictionary')
root.geometry('600x300')
root['bg'] = 'white'
frame = Frame(
    root, width=200, height=300, borderwidth=1, relief=RIDGE)
frame.grid(sticky="W")


def get_meaning():
    dictionary = PyDictionary()
    get_word = entry.get()
    languages = language.get()

    if get_word == "":
        messagebox.showerror('Dictionary', 'please write the word')
       elif languages == 'English-to-English':
          d = dictionary.meaning(get_word)


            output.insert('end', d['Noun'])

      elif languages == 'English-to-Hindi':\
    translator = Translator()
t =translator.translate(get_word, dest='hi')
output.insert('end', t.text)


def quit():
    root.destroy()


img =
ImageTk.PhotoImage(IMage.open('E:\TKINTER series\Dictionary GUI\dict.png'))
pic = Label(root, image=img)
pic.place(x=40, y=70)
word = Label(root, text="Enter
Word",bg="white",font=('verdana',10,'bold'))
word.place(x=250, y=23)
a = tk.StringVar()
language = ttk.Combobox(root, width=20, textvariable=a, stage='readonly', font=('verdana', 10, 'bold'), )

language['values'] = (
    'English-to-English',
    'English-to-Hindi',
)
language.place(x=380, y=10)
language.current(0)