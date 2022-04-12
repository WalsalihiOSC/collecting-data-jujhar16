from tkinter import *

# TODO: inherit `Page` class :)
class CollectingPage:
    def __init__(self, parent, state):
        self.state = state

        Label(parent, text="First name").grid(sticky="nws")
        self.first_name_entry = Entry(parent)
        self.first_name_entry.grid(sticky="news")

        Label(parent, text="Age").grid(sticky="nws")
        self.age_entry = Entry(parent)
        self.age_entry.grid(sticky="news")

        Label(parent, text="Do you have a mobile phone?").grid(sticky="nws")
        self.mobile_phone_var = Variable(parent)
        self.mobile_phone_var.set(False)
        Radiobutton(parent, text="Yes", variable=self.mobile_phone_var, value=True).grid(sticky="nws")
        Radiobutton(parent, text="No", variable=self.mobile_phone_var, value=False).grid(sticky="nws")

        Button(parent, text="Enter Data", command=self.submit_data).grid(sticky="news", padx=5, pady=5)

    def submit_data(self):
        self.state[self.first_name_entry.get()] = {
            "age": int(self.age_entry.get()),
            "has_mobile_phone": self.mobile_phone_var.get()
        }

    def get_page_action_name():
        return "Add New Person"

    def get_page_title(self):
        return "Collecting People Data"

class DisplayingPage:
    def __init__(self, parent, state):
        self.people = list(state.items())
        self.current_person_index = 0
        if len(self.people) == 0:
            Label(parent, text="No people to display!").grid()
            return

        Label(parent, text="First Name").grid(row=0, column=0, sticky="nws")
        self.first_name_label = Label(parent, text="")
        self.first_name_label.grid(row=0, column=1, sticky="nes")

        Label(parent, text="Age").grid(row=1, column=0, sticky="nws")
        self.age_label = Label(parent, text="")
        self.age_label.grid(row=1, column=1, sticky="nes")

        Label(parent, text="Has Mobile Phone").grid(row=2, column=0, sticky="nws")
        self.has_mobile_phone = Label(parent, text="")
        self.has_mobile_phone.grid(row=2, column=1, sticky="nes")

        self.previous_button = Button(parent, text="Previous", command=self.go_to_previous_person)
        self.previous_button.grid(row=3, column=0)
        self.next_button = Button(parent, text="Next", command=self.go_to_next_person)
        self.next_button.grid(row=3, column=1)

        self.update()

    def go_to_previous_person(self):
        self.current_person_index = self.current_person_index - 1
        self.update()

    def go_to_next_person(self):
        self.current_person_index = self.current_person_index + 1
        self.update()

    def update(self):
        (name, person) = self.people[self.current_person_index]
        self.first_name_label["text"] = name
        self.age_label["text"] = person["age"]
        self.has_mobile_phone["text"] = "Yes" if person["has_mobile_phone"] else "No"
        
        self.previous_button["state"] = "disabled" if self.current_person_index == 0 else "normal"
        self.next_button["state"] = "disabled" if self.current_person_index + 1 == len(self.people) else "normal"

    def get_page_action_name():
        return "Show All"

    def get_page_title(self):
        return "Displaying People Data"

PAGES = [CollectingPage, DisplayingPage]