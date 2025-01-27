from tkinter import Tk, Frame
from tkinter.filedialog import askdirectory
from view.gui import GUIArchitect

def main():
    root = Tk()
    architect = GUIArchitect(root)
    root.mainloop()

main()