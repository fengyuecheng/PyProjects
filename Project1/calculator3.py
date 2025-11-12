

import tkinter as tk

from tkinter import ttk


expression = ""

status = 0

def button_event(event):

    global expression

    global status

    item = event.widget.cget("text")

    if item in "<=C":

        if item == 'C':

            expression = ""

            status = 0

        elif item == '<':

            expression = expression[:-1]

        elif item == '=':

            try:
                expression = f"{eval(expression)}"
            except Exception as e:

                expression = "error"

            status = 3

    elif status == 0 or status == 3:

        if item in "1234567890.":

            expression = ""

            label.config(text=expression)

            expression += item

            status = 1


        elif item in "+-*/%" and status == 3:

            expression += item

            status = 2

    elif status == 2 and item in "+-*/=":

        return

    else:
        expression += item

        if item in "+-*/%":

            status = 2

        else:

            status = 1

    label.config(text = expression)

root = tk.Tk()

root.title("calculator")

root.geometry("300x400")

root.columnconfigure(0, weight = 1)

root.rowconfigure(1, weight = 1)

up_frame = ttk.Frame(root, padding = "10")

up_frame.grid(row = 0, column = 0, sticky = "nsew")

up_frame.columnconfigure(0, weight=1)

label = ttk.Label(up_frame, font = ("Arial", 24), text = expression, padding = "10", anchor = 'e')

label.grid(row = 0, column = 0, sticky = "ew")

down_frame = ttk.Frame(root, padding = "10")

down_frame.grid(row = 1, column = 0, sticky = "nsew")

down_frame.rowconfigure((0, 1, 2, 3, 4), weight = 1)

down_frame.columnconfigure((0, 1, 2, 3), weight = 1)

buttons = [
    ('C', 0, 0), ('/', 0, 1), ('*', 0, 2), ('<', 0, 3),
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('-', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('+', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('=', 3, 3),
    ('%', 4, 0), ('0', 4, 1), ('.', 4, 2)
]
button_refs = {}

for text, row, col in buttons:

    button = ttk.Button(down_frame, text = text)

    if text == '=':

        button.grid(row = row, column = col, rowspan = 2, sticky = "nsew")

    else:
        button.grid(row = row, column = col, sticky = "nsew")

    button_refs[text] = button

    button.bind("<Button-1>", button_event)

root.mainloop()