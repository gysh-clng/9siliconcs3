class Journalist:
    def __init__(self, Name, Field, Availability, writtenArticles):
        self.Name = Name
        self.Field = Field
        self.Availability = Availability
        self._writtenArticles = writtenArticles
        self.articles = []

    def writeArticle(self):
        self._writtenArticles += 1
    def submitArticle(self):
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

class CampusJournalist(Journalist):
    def __init__(self, Name, Field, Availability, writtenArticles, Campus):
        super().__init__(Name, Field, Availability, writtenArticles)
        self.Campus = Campus

campusJournalist = CampusJournalist(
    "Veigne",
    "News-Feature",
    True,
    10,
    "PSHS-BRC"
)

article1 = Article("Campus Events", "News-Feature")
article2 = Article("Suspension Updates", "News-Feature")
article3 = Article("Bulletin Patches", "News-Feature")

print("--- INHERITANCE TEST ---")
print("Name:", campusJournalist.Name)
print("Field:", campusJournalist.Field)
print("Campus:", campusJournalist.Campus)

campusJournalist.writeArticle()

print("Article Count:", campusJournalist._writtenArticles)

print("\n--- AGGREGATION TEST ---")
print("Journalist:", campusJournalist.Name)
print("Articles before:", len(campusJournalist.articles))

campusJournalist.addArticle(article1)
campusJournalist.addArticle(article2)
campusJournalist.addArticle(article3)

print("Articles after:", len(campusJournalist.articles))

for article in campusJournalist.articles:
    article.displayinfo()