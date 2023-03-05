#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk, Menu

first_time = False
def changeState(button_pressed, uuid):
    global first_time, last_pressed, root
    state = button_pressed['state']
    
    frames = {
        0: home(root),
        1: layouts(root),
        2: layouts(root)
        }
    
    if str(state) == 'normal':
        main_frame = frames.get(uuid)
        main_frame.grid(column=0, row=1, sticky="NESW")
        button_pressed['state'] = tk.DISABLED
        if not first_time:
            first_time = True
            last_pressed = button_pressed
        else:
            last_pressed['state'] = tk.NORMAL
            last_pressed = button_pressed

def nav_menu(container):

    frame = ttk.Frame(container)
    

    # grid layout for the input frame
    frame.columnconfigure((0, 1, 2), weight=1)

    home = ttk.Button(frame, command=lambda:[changeState(home, 0), ], text='Home')
    home.grid(column=0, row=0, sticky="NESW")
    
    layouts = ttk.Button(frame, command=lambda:[changeState(layouts, 1)], text='Layouts')
    layouts.grid(column=1, row=0, sticky="NESW")
    
    Settings = ttk.Button(frame, command=lambda:[changeState(Settings, 2)], text='Settings')
    Settings.grid(column=2, row=0, sticky="NESW")

    for widget in frame.winfo_children():
        widget.grid(padx=0, pady=0)

    return frame

def home(container):

    frame = ttk.Frame(container)

    # grid layout for the input frame
    frame.columnconfigure(0, weight=1)
    
    frame.columnconfigure(1, weight=1)
    home = ttk.Button(frame, command=lambda:[changeState(home)], text='Home')
    home.grid(column=0, row=0, sticky="NESW")
    
    return frame

def layouts(container):

    frame = ttk.Frame(container)

    # grid layout for the input frame
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    
    return frame

def settings(container):

    frame = ttk.Frame(container)

    # grid layout for the input frame
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    
    return frame

def create_main_window():
    global root
    root = tk.Tk()
    root.geometry("1000x400")
    root.title('Terminator Layout manager')


    # layout on the root window
    root.columnconfigure(0, weight=1)

    nav_frame = nav_menu(root)
    nav_frame.grid(column=0, row=0, sticky="NESW")
    
    root.mainloop()


if __name__ == "__main__":
    create_main_window()
