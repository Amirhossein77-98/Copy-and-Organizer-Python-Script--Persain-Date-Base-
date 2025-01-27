from tkinter import *
from tkinter import Tk
from models.copy_model import CopyModel


class GUIArchitect():
    def __init__(self, root):
        self.root = root
        self.main_window_builder()

    def main_window_builder(self):
        self.root.title("Organizer Script")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.minsize(600, 400)
        self.root.maxsize(600, 400)
        input_frame = Frame(self.root)
        input_frame.grid(column=0, row=0)
        self.add_labels(input_frame)
        self.add_buttons(input_frame)
        output_frame = Frame(self.root, bg="black")
        output_frame.grid(column=0, row=1)
        title = Label(output_frame, text="Copy Script")
        title.grid(sticky="EW")

    def add_labels(self, frame):
        title = Label(frame, text="Copy Script")
        title.grid(sticky="EW")

    def add_buttons(self, frame):
        choose_origin_btn = Button(frame, text="Choose Source", command=CopyModel.origin_picker)
        choose_origin_btn.grid(sticky="EW")
        choose_destination_btn = Button(frame, text="Choose Destination", command=CopyModel.destination_picker)
        choose_destination_btn.grid(sticky="EW")
        start_button = Button(frame, text="Start")
        start_button.grid(sticky="EW")

