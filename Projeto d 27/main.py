from  tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


my_label = Label(text=" I am a Label", font=("Arial",24, ))
my_label.pack()

my_label["text"] = " New Text"
my_label.config(text="New Text")


def button_clicked():
    my_label["text"] = input.get()




button = Button(text="Click Me", command=button_clicked)
button.pack()

#input

input = Entry()
input.pack()
print(input)






window.mainloop()