from tkinter.filedialog import askdirectory

class CopyModel:
    @staticmethod
    def origin_picker(self):
        origin = askdirectory(title="Choose the source folder")
        return origin

    staticmethod
    def destination_picker(self):
        destination = askdirectory(title="Choose the destination folder")
        return destination