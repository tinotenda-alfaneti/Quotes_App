from tkinter import *
import requests
import pygame
from pygame import mixer
from pygame.locals import *


def background_music():
    
    mixer.init()

    # playing music
    mixer.music.load("backg.wav")
    mixer.music.play(-1)


def get_quote():
    
    '''Process a get request to get the quote '''
    
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    
    # writing the quote on the GUI
    canvas.itemconfig(quote_text, text=quote)

    background_music()

# creating GUI

window = Tk()
window.title("Kanye Says...")


window.config(padx=20, pady=20)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)

quote_text = canvas.create_text(150, 207, text="KANYE Quote", width=250, font=("Arial", 25, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()
