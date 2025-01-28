from tkinter import *
from tkinter import messagebox

class CopyController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def new_shamsi_georgian_copy_operation(self, source_path, destination_path):
        result = self.model.copy_and_organize_files_shamsi_order_with_georgian_years(source_path, destination_path)
        if not result:
            self.error_message(title="Operation Failed", msg="Failed to copy and organize files in Shamsi order.")
    
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

    def update_progress_bar(self, value):
        self.view._progress_state(value)

    def delete_files_after_copy(self, source):
        result = self.model.delete_files_after_copy(source)
        if result[0]:
            messagebox.showinfo(title=result[1], message=result[2])
        else:
            CopyController.error_message(title=result[1], msg=result[2])

    @staticmethod
    def error_message(title, msg):
        messagebox.showerror(title=title, message=msg)
