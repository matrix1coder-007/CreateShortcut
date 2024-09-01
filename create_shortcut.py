"""
Author:             Ishita Katyal
Date created:       06/25/2023
Date last updated:  07/03/2023
Topic:              Create shortcut of a given file/folder
Description:
    1. Take following inputs:
        - Input file location
        - Output file destination
        - Output file name
        - Icon image
    2. Create the shortcut for the given file.
"""


import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk


def call_dialog_box():
    input_file_location = fd.askopenfilename()
    input_file_location.grid()


def call_dialog_box_for_icon(root_frame):
    shortcut_file_icon = tk.getOpenFile(root_frame)
    shortcut_file_icon.grid()


def call_dialog_box_for_final_destination(root_frame):
    output_directory_location = fd.askdirectory(root_frame)
    output_directory_location.grid()


# root-main window
root_window = Tk()
root_window.overrideredirect(True)
root_window.geometry("500x500")


# root-main frame
root_frame = tk.Frame(root_window, height=500, width=500, background="white")
root_frame.grid(row=0, column=0, rowspan=10, columnspan=5)


# menu bar label  background='#0D5BE1',
menu_bar_label = tk.Label(root_frame, background="blue", height=50, width=750)
menu_bar_label.grid(row=0, column=0)


# menu bar image
logo_img = Image.open("icon-1.ico")
logo_img_width, logo_img_height = logo_img.size
menu_bar_logo = ImageTk.PhotoImage(image=logo_img)
menu_bar_logo_frame = tk.Label(
    menu_bar_label, image=menu_bar_logo, height=40, width=50)
menu_bar_logo_frame.grid(row=0, column=0)


# title-bar
title_label = tk.Label(root_frame, text='Create Shortcut', bg="blue",
                       foreground='white', font=('Showcard Gothic', 25))
title_label.grid(row=1, column=1)


# folder options to be given for location
select_file_label = tk.Label(root_frame, text='Select a file ')
select_file_label.grid(row=2, column=0)

input_file_location_button = tk.Button(
    root_frame, text='Click to select the file ', command=call_dialog_box)
input_file_location_button.grid(row=4, column=0)
select_icon_label = tk.Label(root_frame, text='Enter the icon image ')
select_icon_label.grid(row=3, column=0)
select_icon_location_button = tk.Button(
    root_frame, text='Click to select the icon image ', command=call_dialog_box_for_icon)
select_icon_location_button.grid(row=4, column=1)


# final shortcut file
output_directory_label = tk.Label(
    root_frame, text='Select the destination folder ')
output_directory_label.grid(row=5, column=0)
output_dir_location_button = tk.Button(
    root_frame, text='Click to select the destination folder ', command=call_dialog_box_for_final_destination)
output_dir_location_button.grid(row=6, column=0)

shortcut_file_label = tk.Label(
    root_frame, text='Enter the shortcut file name ')
shortcut_file_label.grid(row=7, column=0)
shortcut_file_name = tk.Entry(root_frame, text='Enter the shortcut file name ')
shortcut_file_name.grid(row=8, column=0)


# buttons
ok_button = tk.Button(root_frame, text='OK')
ok_button.grid(row=9, column=0)

cancel_button = tk.Button(root_frame, text='Cancel',
                          command=root_window.destroy)
cancel_button.grid(row=10, column=0)

'iktechserve.007@gmail.com'

# footer-bar
footer_label = tk.Label(root_frame, text='(c) IK TechServe 2023',
                        foreground="white", bg="blue", font=('Showcard Gothic', 10), width=750)
footer_label.grid(row=11, column=0)


# call main loop
root_window.mainloop()
