class Journalist:
    def __init__(self, Name, Field, Availability, writtenArticles):
        self.Name = Name
        self.Field = Field
        self.Availability = Availability
        self.__writtenArticles = writtenArticles

    def writeArticle(self):
        self.__writtenArticles += 1

    def submitArticle(self):
        print(self.Name, "submitted an article.")

    def coverArticle(self, topic):
        self.Field = topic

    def getWrittenArticles(self):
        return self.__writtenArticles


# Object 1
journalist1 = Journalist("Veigne", "News-Feature", True, 10)

# Object 2
journalist2 = Journalist("Abel", "Editorial", True, 5)


# Initial situation
print("--- BEFORE ---")
print("Journalist 1:", journalist1.Name, journalist1.Field,
      journalist1.Availability, journalist1.getWrittenArticles())

print("Journalist 2:", journalist2.Name, journalist2.Field,
      journalist2.Availability, journalist2.getWrittenArticles())


# To change Object No. 1 only
print("\nWriting an article for Journalist 1...")
journalist1.writeArticle()


# Updated situation
print("\n--- AFTER ---")
print("Journalist 1:", journalist1.Name, journalist1.Field,
      journalist1.Availability, journalist1.getWrittenArticles())

print("Journalist 2:", journalist2.Name, journalist2.Field,
      journalist2.Availability, journalist2.getWrittenArticles())