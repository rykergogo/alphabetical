"""

App designed by Ryker Gogolkiewicz

"""


from os import close, error
import tkinter as tk
from tkinter import PhotoImage, filedialog, Text, messagebox
import webbrowser
from tkinter.ttk import *

files = []

#Ascending function
def asc(list):
    return sorted(list)

#Descending function
def des(list):
    return sorted(list, reverse=True)

#Handles the actual organizing of the files
def org(btn_press):
    MsgBox = tk.messagebox.askquestion('Warning','This will overwrite the existing files, do you want to proceed?',icon = 'warning')
    if MsgBox == 'yes':
        try:
            for file in files:
                text = open(file)
                words = text.read()
                text.close()
                words = words.split()
                if btn_press == 'asc':
                    words = asc(words)
                elif btn_press == 'dsc':
                    words = des(words)
                new = open(file, 'w')
                for i in range(len(words)):
                    if i == len(words) - 1:
                        new.write(words[i])
                    else:
                        new.write(words[i] + '\n')
                new.close()
            completed = tk.messagebox.showinfo('Done!','All files were sorted successfully.',icon = 'info')
        except:
            err = tk.messagebox.showerror('Oops','Something went wrong',icon = 'error')
            root.destroy()

#Opens file and prints location to frame.
def openFile():
    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir="/%USERPROFILE%/", title='Select File', filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    files.append(filename)

    for file in files:
        #This if statement gets rid of empty strings in files caused by clicking "cancel"
        if file == "":
            files.remove(file)
            continue
        label = tk.Label(frame, text=file, bg="gray")
        label.pack()

#Opens my website in default web browser
def callback(url):
    webbrowser.open_new(url)


#Credit function
def credits():
    callback('https://www.rykergogo.com')


root = tk.Tk()

root.title('Text File Organizer')

root.resizable(False, False)




#Background Color
canvas = tk.Canvas(root, height=500, width=500, bg="#C2E87D")
canvas.pack()

#Background
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.5, relheight=0.5, relx=0.1, rely=0.1)

#Pushes files to the frame for display.
openFiles = tk.Button(root, text="Add Text File", padx=10, pady=5, fg='white', bg="black", command=openFile)
openFiles.pack()
openFiles.place(relx=0.7, rely=0.1)

#Ascending Button
asc_btn = tk.Button(root, text="Ascending", padx=10, pady=5, fg='white', bg="black", command=lambda btn_press='asc': org(btn_press))
asc_btn.pack()
asc_btn.place(relx=0.73, rely=0.53)

#Descending Button
dsc_btn = tk.Button(root, text="Descending", padx=10, pady=5, fg='white', bg="black", command=lambda btn_press='dsc': org(btn_press))
dsc_btn.pack()
dsc_btn.place(relx=0.72, rely=0.43)

#Credits Button
credit = tk.Button(root, text="Credits", padx=10, pady=5, fg='white', bg="black", command=credits)
credit.pack()
credit.place(relx=0.73, rely=0.20)



root.mainloop()