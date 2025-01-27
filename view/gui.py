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
        self.root.rowconfigure(2, weight=1)
        self.root.minsize(600, 400)
        self.root.maxsize(600, 400)
        title_frame = Frame(self.root)
        title_frame.grid(column=0, row=0, pady=0)
        input_frame = Frame(self.root)
        input_frame.grid(column=0, row=1)
        output_frame = Frame(self.root, bg="black")
        output_frame.grid(column=0, row=2)
        self.title_frame_config(title_frame)
        self.input_frame_config(input_frame)
        self.output_frame_config(output_frame)

    def title_frame_config(self, frame):
        title = Label(frame, text="Copy Script", font=("Times New Roman", 25))
        title.grid(sticky="EW")

    def input_frame_config(self, frame):
        choose_origin_btn = Button(frame, text="Choose Source", command=CopyModel.origin_picker)
        choose_origin_btn.grid(sticky="EW")
        choose_destination_btn = Button(frame, text="Choose Destination", command=CopyModel.destination_picker)
        choose_destination_btn.grid(sticky="EW")
        start_button = Button(frame, text="Start")
        start_button.grid(sticky="EW")

    def output_frame_config(self, frame):
        title = Label(frame, text="Output Frame")
        title.grid(sticky="EW")