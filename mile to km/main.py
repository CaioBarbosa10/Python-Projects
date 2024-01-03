from tkinter import *

window = Tk()
window.title("Mile to Km")

def mile_to_km():
    mile = float(miles_input.get())
    km = round(1.609 * mile)
    value_label.config(text= f"{km}")



miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to" , padx=20)
is_equal_to_label.grid(column=0, row=1)


value_label = Label(text='0', padx=20)
value_label.grid(column=1, row=1)


km_label = Label(text="Km", padx=20)
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command = mile_to_km  )
calculate_button.grid(column=1,row=2, padx=10, pady=10)





window.mainloop()
