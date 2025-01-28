from tkinter import *
from tkinter import messagebox

class CopyController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def new_shamsi_copy_operation(self, source_path, destination_path):
        result = self.model.copy_and_organize_files_shamsi_order(source_path, destination_path)
        if not result:
            self.error_message(title="Operation Failed", msg="Failed to copy and organize files in Shamsi order.")

    def new_georgian_copy_operation(self, source_path, destination_path):
        result = self.model.copy_and_organize_files_georgian_order(source_path, destination_path)
        if not result:
            self.error_message(title="Operation Failed", msg="Failed to copy and organize files in Georgian order.")
    
    def new_bulk_copy(self, source_path, destination_path):
        result = self.model.simple_bulk_copy(source_path, destination_path)
        if not result:
            self.error_message(title="Operation Failed", msg="Failed to perform bulk copy.")

    @staticmethod
    def error_message(title, msg):
        messagebox.showerror(title=title, message=msg)