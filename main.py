from view.copy_view import GUIArchitect
from models.copy_model import CopyModel
from controllers.copy_controller import CopyController
from customtkinter import CTk
import os
import sys

def main():
    root = CTk()
    # Get the base path for the executable or script
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    # Define the path to the icon
    icon_path = os.path.join(base_path,"assets", "icon", "folder.ico")
    root.wm_iconbitmap(icon_path)
    
    controller = CopyController(None, None)
    model = CopyModel(controller)
    controller.model = model
    view = GUIArchitect(root, controller)
    controller.view = view
    root.mainloop()

if __name__ == '__main__':
    main()