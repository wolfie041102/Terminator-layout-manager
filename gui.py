#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
from backend import get_layouts

first_time = False
def changeState(button_pressed, uuid):
    global first_time, last_pressed, root, last_frame, main_frame
    state = button_pressed['state']
    
    frames = {
        0: home(root),
        1: layouts(root),
        2: settings(root)
        }
    
    if str(state) == 'normal':
        main_frame = frames.get(uuid)
        main_frame.grid(column=0, row=1, sticky="NESW")
        button_pressed['state'] = tk.DISABLED
        if not first_time:
            first_time = True
            last_pressed = button_pressed
            last_frame = main_frame
        else:
            last_pressed['state'] = tk.NORMAL
            last_frame.destroy
            last_pressed = button_pressed

def nav_menu(container):

    frame = ttk.Frame(container)
    

    # grid layout for the input frame
    frame.columnconfigure((0, 1, 2), weight=1)
    frame.rowconfigure(0, weight=1)
    
    home = ttk.Button(frame, command=lambda:[changeState(home, 0), ], text='Home')
    home.grid(column=0, row=0, sticky="NESW")
    
    layouts = ttk.Button(frame, command=lambda:[create_layouts_list(), changeState(layouts, 1)], text='Layouts')
    layouts.grid(column=1, row=0, sticky="NESW")
    
    settings = ttk.Button(frame, command=lambda:[changeState(settings, 2)], text='Settings')
    settings.grid(column=2, row=0, sticky="NESW")

    return frame

def home(container):

    frame = ttk.Frame(container)

    # grid layout for the input frame
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)
    
    frame.columnconfigure(1, weight=1)
    home = ttk.Button(frame, command=lambda:[changeState(home)], text='Home')
    home.grid(column=0, row=0, sticky="NESW")
    
    
    return frame

def create_layouts_list():
    global all_layouts
    all_layouts = get_layouts()
    all_layouts = list(all_layouts.keys())

def layouts(container):
    global all_layouts
    frame = ttk.Frame(container)

    # grid layout for the input frame
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=6)
    frame.rowconfigure(0, weight=1)
    
    layouts_var = tk.StringVar(value=all_layouts)
    listbox = tk.Listbox(
        frame,
        listvariable=layouts_var,
        height=10,
        selectmode='browse')
    listbox.grid(column=0, row=0, sticky="NESW")
    
    label = tk.Label(frame, bg='green', text='This is a label')
    label.grid(column=1, row=0, sticky="NESW")

    
    return frame

def settings(container):

    frame = ttk.Frame(container)

    # grid layout for the input frame
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.rowconfigure(0, weight=1)
    
    return frame

def create_main_window():
    global root
    root = tk.Tk()
    root.geometry("1000x400")
    root.title('Terminator Layout manager')
    root.configure(bg="red")


    # layout on the root window
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=5)
                      
    nav_frame = nav_menu(root)
    nav_frame.grid(column=0, row=0, sticky="NESW")
    
    root.mainloop()

