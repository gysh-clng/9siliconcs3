class Publication: # Creates Publication class

    def __init__(self, title, author): # Initializes the title and author
        self.__title = title
        self.__author = author

    def get_title(self): # Returns publication's title
        return self.__title

    def get_author(self): # Returns publication's author
        return self.__author

    def set_title(self, title): # Changes publication's title
        self.__title = title

    def set_author(self, author): # Changes publication's author
        self.__author = author

class Book(Publication): # Makes Book class and inherits title and author from Publication

    def __init__(self, title, author, number_of_pages): # Initializes book's title, author, and number of pages
        super().__init__(title, author)
        self.set_number_of_pages(number_of_pages)

    def set_number_of_pages(self, number_of_pages): # Updates number of pages and determines whether inputted value is valid
        if number_of_pages <= 0:
            print("The number of pages must be positive.")
            self.__number_of_pages = 0
        else:
            self.__number_of_pages = number_of_pages

    def get_number_of_pages(self): # Returns no. of pages
        return self.__number_of_pages      

class Magazine(Publication): # Creates Magazine class and also inherits title and author from Publication

    def __init__(self, title, author, issue_number): # Initializes magazine's title, author, and issue numbeer
        super().__init__(title, author)
        self.set_issue_number(issue_number)

    def set_issue_number(self, issue_number): # Updates issue number and checks whether value is valid
        if issue_number <= 0:
            print("The issue number must be positive.")
            self.__issue_number = 0
        else:
            self.__issue_number = issue_number
        
    def get_issue_number(self): # Returns issue number
        return self.__issue_number

# Asks for the info of both publications
title = input("Enter Publication 1 title: ")
author = input("Enter Publication 1 author: ")
title2 = input("Enter Publication 2 title: ")
author2 = input("Enter Publication 2 author: ")

# Creates two publication objects
pub1 = Publication(title, author)
pub2 = Publication(title2, author2)

# Asks for the info of both books
book_title = input("Enter Book 1 title: ")
book_author = input("Enter Book 1 author: ")
number_pages = int(input("Enter Book 1's number of pages: "))
book_title2 = input("Enter Book 2 title: ")
book_author2 = input("Enter Book 2 author: ")
number_pages2 = int(input("Enter Book 2's number of pages: "))

# Creates two book objects
book1 = Book(book_title, book_author, number_pages)
book2 = Book(book_title2, book_author2, number_pages2)

# Asks for the info of both magazines
mgzn_title = input("Enter Magazine 1 title: ")
mgzn_author = input("Enter Magazine 1 author: ")
issue_number = int(input("Enter Magazine 1's issue number: "))
mgzn_title2 = input("Enter Magazine 2 title: ")
mgzn_author2 = input("Enter Magazine 2 author: ")
issue_number2 = int(input("Enter Magazine 2's issue number: "))

# Creates two magazine objects
magazine1 = Magazine(mgzn_title, mgzn_author, issue_number)
magazine2 = Magazine(mgzn_title2, mgzn_author2, issue_number2)

# Displays all gathered info
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

# ChatGPT aided me in doing this FA.
# I asked for the task breakdown, as well as the rechecking of my code to determine whether I have inputted the right details.