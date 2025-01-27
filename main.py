from tkinter import Tk
from view.gui import GUIArchitect
from customtkinter import CTk

def main():
    root = CTk()
    GUIArchitect(root)
    root.mainloop()

main()