from tkinter import *
from customtkinter import *
from tkinter import Tk, PhotoImage
from tkinter.filedialog import askdirectory
from models.copy_model import CopyModel
from view.gui_logger import TextHandler
import logging

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

    def copy_ignite(self):
        CopyModel.copy_files(self.SOURCE_PATH, self.DESTINATION_PATH)

    def main_window_builder(self):
        self.root.title("Organizer Script")
        photo = PhotoImage(file="assets\\icon\\folder.png")
        self.root.iconphoto(False, photo)
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        
        self.root.minsize(700, 500)
        # self.root.maxsize(600, 400)
        
        title_frame = CTkFrame(self.root, bg_color='transparent')
        title_frame.grid(column=0, row=0, pady=0)
        input_frame = CTkFrame(self.root)
        input_frame.grid(column=0, row=1)
        output_frame = CTkFrame(self.root)
        output_frame.grid(column=0, row=2, sticky="nsew")
        
        self.title_frame_config(title_frame)
        self.input_frame_config(input_frame)
        self.output_frame_config(output_frame)

    def title_frame_config(self, frame: CTkFrame):
        title = CTkLabel(frame, text="Copy Script", font=("Times New Roman", 25))
        title.grid(sticky="EW")

    def input_frame_config(self, frame: CTkFrame):
        frame.rowconfigure(0, weight=1, pad=15)
        frame.rowconfigure(1, weight=1, pad=15)
        frame.rowconfigure(2, weight=1, pad=15)
        frame.columnconfigure(0, weight=1, pad=10)
        frame.columnconfigure(1, weight=1, pad=10)
        frame.columnconfigure(2, weight=1, pad=10)
        
        origin_label = CTkLabel(frame, text="Origin:")
        origin_label.grid(row=0, column=0)
        origin_entry = CTkEntry(frame, textvariable=self.SOURCE_PATH)
        origin_entry.grid(row=0, column=1, sticky="EW")
        choose_origin_btn = CTkButton(frame, text="Browse", command=lambda: self.origin_picker(origin_entry))
        choose_origin_btn.grid(row=0, column=2)
        
        destination_label = CTkLabel(frame, text="Destination:")
        destination_label.grid(row=1, column=0)
        destination_entry = CTkEntry(frame, textvariable=self.DESTINATION_PATH)
        destination_entry.grid(row=1, column=1, sticky="EW")
        choose_destination_btn = CTkButton(frame, text="Browse", command=lambda: self.destination_picker(destination_entry))
        choose_destination_btn.grid(row=1, column=2)
        
        start_button = CTkButton(frame, text="Copy!", command=self.copy_ignite)
        start_button.grid(row=2, column=1)

    def output_frame_config(self, frame: CTkFrame):
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=0)

        self.log_text = Text(frame, wrap='none', height=frame.winfo_height(), bg="black", foreground='white', font=15)
        self.log_text.grid(row=1, column=0, sticky="nsew")
        self.log_text.insert(END, "Log will appear here\n")

        scrollbar = CTkScrollbar(frame, command=self.log_text.yview)
        scrollbar.grid(row=1, column=1, sticky="ns")
        self.log_text.config(yscrollcommand=scrollbar.set)

        self.log_text.tag_configure('timestamp', foreground='cyan')
        self.log_text.tag_configure('operationmode', foreground='red')
        self.log_text.tag_configure('filename', foreground='yellow')
        self.log_text.tag_configure('to', foreground='red')
        self.log_text.tag_configure('destination', foreground='yellow')

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        text_handler = TextHandler(self.log_text)
        self.logger.addHandler(text_handler)