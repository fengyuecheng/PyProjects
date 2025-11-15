
import tkinter as tk

from tkinter import ttk

def hover_effect(label):

    def on_entry(event):

        label.config(background="lightgrey")

    def on_leave(event):

        label.config(background="SystemButtonFace")

    label.bind("<Enter>", on_entry)

    label.bind("<Leave>", on_leave)

def check_row(parent, row):

    for widget in parent.winfo_children():

        info = widget.grid_info()

        if info and info.get('row') == row:

            return widget

    return None

def scrollable_frame(parent):

    canvas = tk.Canvas(parent)

    frame = tk.Frame(canvas)

    canvas.create_window((0, 0), window = frame, anchor = 'nw')

    frame.bind("<Configure>",
               lambda e: canvas.configure(scrollregion = canvas.bbox("all")))

    scrollbar = ttk.Scrollbar(parent, orient = "vertical", command = canvas.yview)

    canvas.configure(yscrollcommand = scrollbar.set)

    canvas.pack(side = "left", fill = "both", expand = True)

    scrollbar.pack(side = "right", fill = "y")

    def on_mousewheel(event):

        if event.delta:

            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        elif event.num == 4:

            canvas.yview_scroll(-1, "units")

        elif event.num == 5:

            canvas.yview_scroll(1, "units")

    def linux_up_mousewheel(event):

        canvas.yview_scroll(-1, "units")

    def linux_down_mousewheel(event):

        canvas.yview_scroll(1, "units")

    canvas.bind_all("<MouseWheel>", on_mousewheel)

    canvas.bind_all("<Button-4>", linux_up_mousewheel)

    canvas.bind_all("<Button-5>", linux_down_mousewheel)

    return canvas, frame

