from tkinter import *
from tkinter import Tk
from tkinter import messagebox

class CopyController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def new_shamsi_copy_operation(self, source_path, destination_path):
        self.model.copy_and_organize_files_shamsi_order(source_path, destination_path)

    def new_georgian_copy_operation(self, source_path, destination_path):
        self.model.copy_and_organize_files_georgian_order(source_path, destination_path)
    
    def new_bulk_copy(self, source_path, destination_path):
        self.model.simple_bulk_copy(source_path, destination_path)

    @staticmethod
    def error_message(title, msg):
        messagebox.showerror(title=title, message=msg)