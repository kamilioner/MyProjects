import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename

root = tk.Tk()
root.withdraw()

# file_path = filedialog.askopenfilename()
# print(file_path)

name = askopenfilename(initialdir="C:/Users/Kamil/Downloads",
                           filetypes =(("Text File", "*.csv"),("All Files","*.*")),
                           title = "Choose a file."
                           )
print(name)