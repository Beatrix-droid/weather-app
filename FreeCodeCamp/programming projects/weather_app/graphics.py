import tkinter as tk
import tkinter.font
from tkinter import *
import customtkinter
from main import *
from PIL import Image
from PIL import ImageTk

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")
app = customtkinter.CTk()
app.title("")
app.geometry("700x600")


canvas1 = customtkinter.CTkCanvas(app, width=700, height=400)

canvas1.pack()

#styling up the background:
image = Image.open("background.png")
image = image.resize((700, 600), Image.ANTIALIAS)

background_img =ImageTk.PhotoImage(image)
background = Label(app, image=background_img)
background.place(x=0, y=0)





#defining the text that will appear on the app and how it will be spaced
title_app = customtkinter.CTkLabel(app, text="A Weather App", padx =100, corner_radius=188)
API_key = customtkinter.CTkLabel(app, text="Please input your API key here:", anchor="center", padx=10)
prompt_question = customtkinter.CTkLabel(app, text="Enter the name of the city you wish to get the weather of:", padx=10)

canvas1.create_window(350, 45, window=title_app)
canvas1.create_window(350, 125, window=API_key)
canvas1.create_window(350, 225, window=prompt_question)




#styling up text:
#Title_font = tkinter.font.Font(family="Comic Sans MS", size=20, weight="bold")
#title_app.configure(font=Title_font)

#input_fonts = tkinter.font.Font(family="Comic Sans MS", size=16)
#API_key = API_key.configure(font=input_fonts)
#prompt_question = prompt_question.configure(font=input_fonts)


#prompting users for their API key
API_key = customtkinter.CTkEntry(app)
canvas1.create_window(350, 175, window=API_key)



#prompting users to enter the city they want to see the weather of.
city_entry = customtkinter.CTkEntry(app)
canvas1.create_window(350, 275, window=city_entry)



#displaying the current weather
def show_weather():
	global weather_today
	city = city_entry.get()
	key = API_key.get()
	weather_today = customtkinter.CTkLabel(app, text=get_current_weather(city, key), bg="white", bd=2, relief=RAISED)
	weather_today.place(x=390, y=490)
	canvas1.create_window(350, 392, window=weather_today, anchor="center")


Search_button = customtkinter.CTkButton(app, text="Search", hover_color="GreenYellow",command=show_weather)
Search_button.place(x=300, y=490)
def clear_text():
		weather_today.destroy()



Delete_button = customtkinter.CTkButton(app, text="Delete Text",fg_color="Orange", hover_color="Gold",command=clear_text)
Delete_button.place(x=150, y=490)



#closing the program
quit = customtkinter.CTkButton(app, text="QUIT",fg_color="Red",
hover_color="OrangeRed", command=quit)
quit.place(x=450, y=497)


app.mainloop()
