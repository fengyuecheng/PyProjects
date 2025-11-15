
import tkinter as tk

from tk_kit import scrollable_frame

import os

import tree

root = tk.Tk()

root.title("files manager")

root.geometry("800x600+600+200")

root.rowconfigure(0, weight=1)

root.columnconfigure(0, weight=1)

canvas, frame = scrollable_frame(root)

tree.tree("D:\\Download", frame)

root.mainloop()