from view.copy_view import GUIArchitect
from models.copy_model import CopyModel
from controllers.copy_controller import CopyController
from customtkinter import CTk

def main():
    root = CTk()
    model = CopyModel()
    controller = CopyController(model, None)
    view = GUIArchitect(root, controller)
    controller.view = view
    root.mainloop()

if __name__ == '__main__':
    main()