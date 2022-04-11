from tkinter import *

class CollectingDataGUI:
    def __init__(self, parent):
        root_frame = Frame(parent)
        root_frame.grid()

if __name__ == "__main__":
    root = Tk()
    CollectingDataGUI(root)
    root.mainloop() 