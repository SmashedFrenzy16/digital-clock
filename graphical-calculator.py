from time import strftime

from tkinter import Label

from tkinter import Tk

 

window = Tk()

window.title("")

window.geometry("225x100")

window.configure(bg="blue")

window.resizable(False, False)

 

clock_label = Label(window, bg="blue", fg="white", font = ("Arial", 30, 'bold'), relief='flat')

clock_label.place(x = 20, y = 20)

 

def update_label():

    current_time = strftime('%H: %M: %S')

    clock_label.configure(text = current_time)

    clock_label.after(80, update_label)

 

update_label()

window.mainloop()
