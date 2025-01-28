from view.copy_view import GUIArchitect
from models.copy_model import CopyModel
from controllers.copy_controller import CopyController
from customtkinter import CTk

def main():
    root = CTk()
    controller = CopyController(None, None)
    model = CopyModel(controller)
    controller.model = model
    view = GUIArchitect(root, controller)
    controller.view = view
    root.mainloop()

if __name__ == '__main__':
    main()