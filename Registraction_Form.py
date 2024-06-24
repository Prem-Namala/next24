from tkinter import *

form = Tk()
form.title("Registration Form")
form.geometry("400x500")


Label(form, text = " ").grid(row=0)
Label(form, text = "Registration Form", font = ("Arial", 24, "bold")).grid(row = 1,columnspan = 2, padx = 60)


Label(form, text = " ").grid(row=2)
Label(form, text = " ").grid(row=3)
Label(form, text = "NAME : ").grid(row = 4, column= 0, sticky='e')
name = Entry(form)
name.grid(row=4, column= 1, sticky= 'w')
Label(form, text = " ").grid(row=5)
Label(form, text = "EMAIL : ").grid(row = 6, column= 0, sticky='e')
email = Entry(form)
email.grid(row=6, column= 1, sticky= 'w')
Label(form, text = " ").grid(row=7)
Label(form, text = "PASSWORD : ").grid(row = 8, column= 0, sticky='e')
password = Entry(form, show="*")
password.grid(row=8, column= 1, sticky= 'w')
Label(form, text = " ").grid(row=9)
var = StringVar()
var.set(False)
Label(form, text = "Gender : ").grid(row = 10, column= 0, sticky='e')
Radiobutton(form, text = "Male", variable = var, value="Male").grid(row=10, column= 1, sticky= 'w')
Radiobutton(form, text = "Female", variable = var, value="Female").grid(row=11, column= 1, sticky= 'w')
Radiobutton(form, text = "Others", variable = var, value="Others").grid(row=12, column= 1, sticky= 'w')
Label(form, text = " ").grid(row=13)
Label(form, text = "AGE : ").grid(row = 14, column= 0, sticky='e')
age = Entry(form)
age.grid(row=14, column= 1, sticky= 'w')
Label(form, text = " ").grid(row=15)
Label(form, text = "ADDRESS : ").grid(row = 16, column= 0, sticky='e')
address = Entry(form)
address.grid(row=16, column= 1, sticky= 'w')

def clear():
    name.delete(0, END)
    email.delete(0, END)
    password.delete(0, END)
    var.set(False)
    age.delete(0, END)
    address.delete(0, END)


Label(form, text="").grid(row=17)
Label(form, text="").grid(row=18)

Button(form, text = "SUBMIT", command = clear).grid(row=19, columnspan=2)


form.mainloop()