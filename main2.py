#importing required module
from tkinter import *
import tkinter as tk
from gtts import gTTS

# this module helps to
# play the converted audio
import os

# create tkinter window
root = Tk()

# give a title
root.title("Tony starck")



root.geometry("650x550")

# styling the frame which helps to
# make our background stylish
frame1 = Frame(root,
			bg = "white",
			height = "150")

# place the widget in gui window 
frame1.pack(fill = X)


frame2 = Frame(root,
			bg = "#eddfe2",
			height = "550")
frame2.pack(fill=X)



# styling the label which show the text
# in our tkinter window
label = Label(frame1, text = "Hai, Tony Enter your Text :)",
			font = "Calibri, 30",
			bg = "white")

label.place(x = 180, y = 70)



# entry is used to enter the text
entry = Entry(frame2, width = 45,
			bd = 4, font = 14)

entry.place(x = 80, y = 52)
entry.insert(0, "")

# define a function which can
# get text and convert into audio
def play():

	# Language in which you want to convert
	language = "en"



# Passing the text and language,
# here we have slow=False. Which tells
# the module that the converted audio should
# have a high speed

	myobj = gTTS(text = entry.get(),
				lang = language,
				slow = False)



	# give the name as you want to
	# save the audio
	myobj.save("convert.wav")
	os.system("convert.wav")

# create a button which holds
# our play function using command = play
btn = Button(frame2, text = "SUBMIT",
			width = "15", pady = 15,
			font = "bold, 15",
			command = play, bg='#c3e3cd')

btn.place(x = 250,
		y = 130)



# start the gui
root.mainloop()








