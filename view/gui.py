from tkinter import *
from tkinter import Tk
from tkinter.filedialog import askdirectory

class GUIArchitect():
    def __init__(self, root):
        self.root = root
        self.SOURCE_PATH = StringVar()
        self.DESTINATION_PATH = StringVar()
        self.main_window_builder()

    
    def origin_picker(self, source_entry):
        origin = askdirectory(title="Choose the source folder")
        self.SOURCE_PATH = origin
        source_entry.delete(0, 'end')
        source_entry.insert(0, self.SOURCE_PATH)

    def destination_picker(self, destination_entry):
        destination = askdirectory(title="Choose the destination folder")
        self.DESTINATION_PATH = destination
        destination_entry.delete(0, 'end')
        destination_entry.insert(0, self.DESTINATION_PATH)

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

    def title_frame_config(self, frame: Frame):
        title = Label(frame, text="Copy Script", font=("Times New Roman", 25))
        title.grid(sticky="EW")

    def input_frame_config(self, frame: Frame):
        frame.rowconfigure(0, weight=1, pad=15)
        frame.rowconfigure(1, weight=1, pad=15)
        frame.rowconfigure(2, weight=1, pad=15)
        frame.columnconfigure(0, weight=1, pad=10)
        frame.columnconfigure(1, weight=1, pad=10)
        frame.columnconfigure(2, weight=1, pad=10)
        
        origin_label = Label(frame, text="Origin:")
        origin_label.grid(row=0, column=0)
        origin_entry = Entry(frame, textvariable=self.SOURCE_PATH)
        origin_entry.grid(row=0, column=1, sticky="EW")
        choose_origin_btn = Button(frame, text="Browse", command=lambda: self.origin_picker(origin_entry))
        choose_origin_btn.grid(row=0, column=2)
        
        destination_label = Label(frame, text="Destination:")
        destination_label.grid(row=1, column=0)
        destination_entry = Entry(frame, textvariable=self.DESTINATION_PATH)
        destination_entry.grid(row=1, column=1, sticky="EW")
        choose_destination_btn = Button(frame, text="Browse", command=lambda: self.destination_picker(destination_entry))
        choose_destination_btn.grid(row=1, column=2)
        
        start_button = Button(frame, text="Start!")
        start_button.grid(row=2, column=1)

    def output_frame_config(self, frame: Frame):
        title = Label(frame, text="Output Frame")
        title.grid(sticky="EW")