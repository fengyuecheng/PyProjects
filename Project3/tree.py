
import os

import tk_kit

from tkinter import ttk

def get_tree(p1, p2, p3, p4):

    root_path = p1

    parent = p2

    depth = p3

    row = p4

    if frame := tk_kit.check_row(parent, row):

        frame.grid_remove()

    else:

        frame = ttk.Frame(parent)

        frame.grid(row = row, column = 0, sticky='ew')

        tree(root_path, frame, depth)

def tree(root_path, parent, depth = None):

    if depth is None:

        depth = 1

        parent.rowconfigure(0, weight=0)

        label = ttk.Label(parent, text = os.path.basename(root_path), font=("Arial", 10), anchor='w')

        label.grid(row = 0, column = 0, sticky = 'ew')

    try:

        files = os.listdir(root_path)

    except PermissionError:

        print("")

        return

    parent.columnconfigure(0, weight=1)

    row = 1

    prefix = "├     " * (depth - 1) + "├── "

    for file in files:

        full_path = os.path.join(root_path, file)

        text = prefix + file

        if os.path.isdir(full_path):

            text = text + ' /'

        label = ttk.Label(parent, text=text, font=("Arial", 10), anchor = 'w')

        label.grid(row=row, column=0, sticky="ew")

        parent.rowconfigure(row, weight=0)

        tk_kit.hover_effect(label)

        row += 1

        if os.path.isfile(full_path):

            pass

        elif os.path.isdir(full_path):

            parent.rowconfigure(row, weight=0)

            label.bind("<Double-Button-1>",
                       lambda event,
                              p1 = os.path.join(root_path, file),
                              p2 = parent,
                              p3 = depth+1,
                              p4 = row: get_tree(p1, p2, p3, p4)
                       )

            row += 1

        else:

            pass