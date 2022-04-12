from tkinter import *
from page import *

class CollectingDataGUI:
    def __init__(self, parent):
        root_frame = Frame(parent)
        root_frame.grid(row=0, column=0, sticky="news")
        root_frame.columnconfigure(0, weight=1)
        root_frame.rowconfigure(0, minsize=50)
        root_frame.rowconfigure(1, weight=1)

        # navigation frame
        # TODO: pink isnt guaranteed to be a system color
        # maybe we can check programatically and default to some other light color
        nav_frame = Frame(root_frame, bg="pink")
        nav_frame.grid(sticky="news")
        nav_frame.columnconfigure(0, weight=1)
        nav_frame.rowconfigure(0, weight=1)
        
        self.page_label = Label(nav_frame, bg="pink")
        self.page_label.grid(row=0, column=0, sticky="nws")
        self.action_buttons_frame = Frame(nav_frame)
        self.action_buttons_frame.grid(row=0, column=1, padx=(0, 5))

        self.content_frame = Frame(root_frame)
        self.content_frame.grid(row=1, column=0)

        self.state = {}
        self.nav_to_page(PAGES[0])

    def update_nav_frame(self):
        self.page_label["text"] = self.page.get_page_title()
        # clear buttons
        for button in self.action_buttons_frame.winfo_children():
            button.destroy()
        c = 0
        for page_class in PAGES:
            # TODO: should probably not do an instance check, but a direct class type check
            if not isinstance(self.page, page_class):
                # python is quirky
                x = page_class
                Button(self.action_buttons_frame, text=page_class.get_page_action_name(), command=lambda: self.nav_to_page(x)).grid(row=0, column=c)
                c = c + 1

    def nav_to_page(self, page_class):
        # clear content
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        self.page = page_class(self.content_frame, self.state)
        self.update_nav_frame()

if __name__ == "__main__":
    root = Tk()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    CollectingDataGUI(root)
    root.mainloop() 