from tkinter import *
from tkinter import messagebox
from customtkinter import *
from tkinter.filedialog import askdirectory
import logging
from view.gui_logger import TextHandler

class GUIArchitect():
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.SOURCE_PATH = StringVar()
        self.DESTINATION_PATH = StringVar()
        self.COMBOBOX_VALUE = StringVar()
        self.CHECKBOX_VALUE = IntVar()
        self.CHECKBOX_VALUE.trace_add("write", lambda *args: self._check_box_change_tracker())
        self.SOURCE_PATH.trace_add("write", self._check_operation_validity)
        self.DESTINATION_PATH.trace_add("write", self._check_operation_validity)
        self.COMBOBOX_VALUE.trace_add("write", self._check_operation_validity)
        self.OPERATION_MODES = ["Simple Bulk Copy","Copy & Organize (Shamsi)", "Copy & Organize (Shamsi with Georgian Years)", "Copy & Organize (Georgian)"]
        self.main_window_builder()

    def _check_operation_validity(self, *args):
        if self.origin_entry.get().strip() and self.destination_entry.get().strip() and self.operation_mode.get().strip():
            self.start_button.configure(state='enabled')
        else:
            self.start_button.configure(state="disabled")

    def _check_box_change_tracker(self, *args):
        if self.CHECKBOX_VALUE.get():
            sure_to_delete = messagebox.askyesno(title="Sure to delete files?", message="Are you sure you want to delete the files after copy?")
            if sure_to_delete:
                self.CHECKBOX_VALUE.set(1)
                self.delete_files_checkbox.select()
            else:
                self.CHECKBOX_VALUE.set(0)
                self.delete_files_checkbox.deselect()
        else:
            self.CHECKBOX_VALUE.set(0)
            self.delete_files_checkbox.deselect()

    def _origin_picker(self, source_entry):
        origin = askdirectory(title="Choose the source folder")
        self.SOURCE_PATH = origin
        source_entry.delete(0, 'end')
        source_entry.insert(0, self.SOURCE_PATH)

    def _destination_picker(self, destination_entry):
        destination = askdirectory(title="Choose the destination folder")
        self.DESTINATION_PATH = destination
        destination_entry.delete(0, 'end')
        destination_entry.insert(0, self.DESTINATION_PATH)

    def _progress_state(self, state):
        self.progress_label.configure(text = f"%{(state * 100):.0f}")
        self.progressbar.set(state)
        self.root.update_idletasks()
        if state == 1:
            messagebox.showinfo("Success", "All files and folders copied and organized successfully.")


    def _copy_ignite(self):
        if self.COMBOBOX_VALUE.get().strip() == self.OPERATION_MODES[2]:
            self.controller.new_shamsi_georgian_copy_operation(source_path=self.SOURCE_PATH, destination_path=self.DESTINATION_PATH)
        elif self.COMBOBOX_VALUE.get().strip() == self.OPERATION_MODES[3]:
            self.controller.new_georgian_copy_operation(source_path=self.SOURCE_PATH, destination_path=self.DESTINATION_PATH)
        elif self.COMBOBOX_VALUE.get().strip() == self.OPERATION_MODES[1]:
            self.controller.new_shamsi_copy_operation(source_path=self.SOURCE_PATH, destination_path=self.DESTINATION_PATH)
        elif self.COMBOBOX_VALUE.get().strip() == self.OPERATION_MODES[0]:
            self.controller.new_bulk_copy(source_path=self.SOURCE_PATH, destination_path=self.DESTINATION_PATH)

        if self.CHECKBOX_VALUE.get():
            self.controller.delete_files_after_copy(self.SOURCE_PATH)

    def main_window_builder(self):
        self.root.title("Organizer Script")
        # self.root.wm_iconbitmap('assets\\icon\\folder.ico')
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        
        self.root.minsize(700, 500)
        self.root.maxsize(600, 400)
        
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
        frame.rowconfigure(3, weight=1, pad=15)
        frame.rowconfigure(4, weight=1, pad=15)
        frame.rowconfigure(5, weight=1, pad=15)
        frame.rowconfigure(6, weight=1, pad=15)
        frame.rowconfigure(7, weight=1, pad=15)
        frame.columnconfigure(0, weight=1, pad=10)
        frame.columnconfigure(1, weight=2, pad=10)
        frame.columnconfigure(2, weight=2, pad=10)
        frame.columnconfigure(3, weight=1, pad=40)
        
        empty_label1 = CTkLabel(frame, text='', height=2, font=CTkFont(size=5))
        empty_label1.grid(row=0)

        origin_label = CTkLabel(frame, text="Origin:")
        origin_label.grid(row=1, column=0, sticky="W", padx=10)
        self.origin_entry = CTkEntry(frame, textvariable=self.SOURCE_PATH, width=300)
        self.origin_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
        choose_origin_btn = CTkButton(frame, text="Browse", width=15, command=lambda: self._origin_picker(self.origin_entry))
        choose_origin_btn.grid(row=1, column=3)
        
        destination_label = CTkLabel(frame, text="Destination:")
        destination_label.grid(row=2, column=0, sticky="W", padx=10)
        self.destination_entry = CTkEntry(frame, textvariable=self.DESTINATION_PATH, width=300)
        self.destination_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
        choose_destination_btn = CTkButton(frame, text="Browse", width=15, command=lambda: self._destination_picker(self.destination_entry))
        choose_destination_btn.grid(row=2, column=3)

        operation_mode_label = CTkLabel(frame, text="Mode:")
        operation_mode_label.grid(row=3, column=0, sticky="W", padx=10)
        self.operation_mode = CTkComboBox(frame,
                                     variable=self.COMBOBOX_VALUE,
                                     values=self.OPERATION_MODES,
                                     state='readonly',
                                     width=205)
        self.operation_mode.grid(row=3, column=1, sticky="W")
        
        self.delete_files_checkbox = CTkCheckBox(frame, text="Delete files after copy", variable=self.CHECKBOX_VALUE)
        self.delete_files_checkbox.grid(row=3, column=2)
        
        empty_label2 = CTkLabel(frame, text='', height=4, font=CTkFont(size=5))
        empty_label2.grid(row=4)

        self.start_button = CTkButton(frame, text="Copy!", command=self._copy_ignite, fg_color='darkred', hover_color='#4E0707', state='disabled')
        self.start_button.grid(row=5, column=1, columnspan=2)

        progressbar_label = CTkLabel(frame, text="Progress:")
        progressbar_label.grid(row=6, column=0, sticky="W", padx=10)
        self.progressbar = CTkProgressBar(frame, width=350)
        self.progressbar.grid(row=6, column=1, columnspan=2)
        self.progressbar.set(0)
        self.progress_label = CTkLabel(frame, text="%0")
        self.progress_label.grid(row=6, column=3, sticky="W", padx=10)

        empty_label2 = CTkLabel(frame, text='', height=2, font=CTkFont(size=5))
        empty_label2.grid(row=7)

    def output_frame_config(self, frame: CTkFrame):
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=0)

        self.log_text = Text(frame, wrap='none', height=frame.winfo_height(), bg="black", foreground='white', font=15)
        self.log_text.grid(row=1, column=0, sticky="nsew")
        self.log_text.insert(END, "Logs:\n")

        y_scrollbar = CTkScrollbar(frame, command=self.log_text.yview)
        y_scrollbar.grid(row=1, column=1, sticky="ns")
        self.log_text.config(yscrollcommand=y_scrollbar.set)

        x_scrollbar = CTkScrollbar(frame, command=self.log_text.xview, orientation='horizontal')
        x_scrollbar.grid(row=2, column=0, sticky="ew")
        self.log_text.config(xscrollcommand=x_scrollbar.set)

        self.log_text.tag_configure('timestamp', foreground='cyan')
        self.log_text.tag_configure('operationmode', foreground='red')
        self.log_text.tag_configure('filename', foreground='yellow')
        self.log_text.tag_configure('to', foreground='red')
        self.log_text.tag_configure('destination', foreground='yellow')

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        text_handler = TextHandler(self.log_text)
        self.logger.addHandler(text_handler)