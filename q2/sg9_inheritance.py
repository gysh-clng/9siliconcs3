class Publication:

    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

class Book(Publication):

    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.set_number_of_pages(number_of_pages)

    def set_number_of_pages(self, number_of_pages):
        if number_of_pages <= 0:
            print("The number of pages must be positive.")
            self.__number_of_pages = 0
        else:
            self.__number_of_pages = number_of_pages

    def get_number_of_pages(self):
        return self.__number_of_pages      

class Magazine(Publication):

    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.set_issue_number(issue_number)

    def set_issue_number(self, issue_number):
        if issue_number <= 0:
            print("The issue number must be positive.")
            self.__issue_number = 0
        else:
            self.__issue_number = issue_number
        
    def get_issue_number(self):
        return self.__issue_number

title = input("Enter Publication 1 title: ")
author = input("Enter Publication 1 author: ")
title2 = input("Enter Publication 2 title: ")
author2 = input("Enter Publication 2 author: ")

pub1 = Publication(title, author)
pub2 = Publication(title2, author2)

book_title = input("Enter Book 1 title: ")
book_author = input("Enter Book 1 author: ")
number_pages = int(input("Enter Book 1's number of pages: "))
book_title2 = input("Enter Book 2 title: ")
book_author2 = input("Enter Book 2 author: ")
number_pages2 = int(input("Enter Book 2's number of pages: "))

book1 = Book(book_title, book_author, number_pages)
book2 = Book(book_title2, book_author2, number_pages2)

mgzn_title = input("Enter Magazine 1 title: ")
mgzn_author = input("Enter Magazine 1 author: ")
issue_number = int(input("Enter Magazine 1's issue number: "))
mgzn_title2 = input("Enter Magazine 2 title: ")
mgzn_author2 = input("Enter Magazine 2 author: ")
issue_number2 = int(input("Enter Magazine 2's issue number: "))

magazine1 = Magazine(mgzn_title, mgzn_author, issue_number)
magazine2 = Magazine(mgzn_title2, mgzn_author2, issue_number2)

print("\nPublication 1")
print(f"Title: {pub1.get_title()}")
print(f"Author: {pub1.get_author()}")

print("\nPublication 2")
print(f"Title: {pub2.get_title()}")
print(f"Author: {pub2.get_author()}")

print("\nBook 1")
print(f"Title: {book1.get_title()}")
print(f"Author: {book1.get_author()}")
print(f"Number of pages: {book1.get_number_of_pages()}")

print("\nBook 2")
print(f"Title: {book2.get_title()}")
print(f"Author: {book2.get_author()}")
print(f"Number of pages: {book2.get_number_of_pages()}")

print("\nMagazine 1")
print(f"Title: {magazine1.get_title()}")
print(f"Author: {magazine1.get_author()}")
print(f"Issue number: {magazine1.get_issue_number()}")

print("\nMagazine 2")
print(f"Title: {magazine2.get_title()}")
print(f"Author: {magazine2.get_author()}")
print(f"Issue number: {magazine2.get_issue_number()}")

# ChatGPT aided me in doing this FA
# I asked for the task breakdown, as well as the rechecking of my code to determine whether I have inputted the right details.