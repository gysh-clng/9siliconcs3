class Publication:

    def __init__(self, title, author):
        self.__title = title
        self.__author = author

class Book(Publication):

    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.__number_of_pages = number_of_pages

class Magazine(Publication)
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = issue_number