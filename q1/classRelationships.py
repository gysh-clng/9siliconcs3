class Journalist:
    def __init__(self, Name, Field, Availability, writtenArticles):
        self.Name = Name
        self.Field = Field
        self.Availability = Availability
        self._writtenArticles = writtenArticles
        self.articles = []

    def writeArticle(self):
        self._writtenArticles+=1
    def submitArticle(sefl):
        print(self.Name, "submitted an article!")
    def coverArticle(self, topic):
        self.Field = topic
    def addArticle(self, article):
        self.articles.append(article)

class Article:
    def __init__(self, title, topic):
        self.title = title
        self.topic = topic
    def displayinfo(self):
        print(self.title, "=", self.topic)

journalist = Journalist("Veigne", "News-Feature", True, 10)
firstarticle = Article("Campus Events", "News-Feature")
secondarticle = Article("Suspension Updates", "News-Feature")
thirdarticle = Article("Bulletin Patches", "News-Feature")

print("--- BEFORE RELATIONSHIP (wow) ---")
print("Journalist:", journalist.Name)
print("Articles:", len(journalist.articles))

print("\n--- BUILDING RELATINSHIP (ayie) ---")
journalist.addArticle(firstarticle)
journalist.addArticle(secondarticle)
journalist.addArticle(thirdarticle)

print("Articles added.")

print("\n--- AFTER RELATIONSHIP ---")
print("Journalist:", journalist.Name)

for article in journalist.articles:
    article.displayinfo()