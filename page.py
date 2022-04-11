# TODO: inherit `Page` class :)
class CollectingPage:
    def __init__(self):
        pass

    def get_page_action_name():
        return "Add New Person"

    def get_page_title(self):
        return "Collecting People Data"

class DisplayingPage:
    def __init__(self):
        pass

    def get_page_action_name():
        return "Show All"

    def get_page_title(self):
        return "Displaying People Data"

PAGES = [CollectingPage, DisplayingPage]