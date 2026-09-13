# Class Relationships

## Previous Class
[View Previous Class Design](classObjectUML.md)

## Relationship Design
The previous class I had created was the Journalist class, and now, its related class is Article. This is because one journalist can write or compose multiple articles, depending on how immense their workload is. In alignment with their actual work, a one-to-many relationship is observed between the two said classes.

## Relationship
**Journalist #1: 0..* Article**

In this code, A Journalist can have zero or more Articles. The Journalist class stores the related Article objects in a list named "articles".

## Class Relationship Diagram
![Class Relationship Diagram](images/crDiagram.png)

## Python Code
[View Python Source](classRelationships.py)

## Test Run
![Relationship Test Run](images/testrun.png)

## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipdiagram.png)

## Analysis

### What is the association between your two classes?
The association between my Journalist and Article classes is that a Journalist writes and the Article is what they produce --- that is the appropriate relationship they uphold. Additionally, one Journalist can be referred with multiple Article objects because their workload is not limited to only one write-up.

### What multiplicity did you choose and why?
I chose the 1 to 0..* multiplicity because it indicates that my Journalist can have zero or more Articles. This is an appropriate setting as the Journalist may have no Articles yet or may be associated with many Articles, depending on which field they specialize in.

### How did you implement the relationshop in Python?
I implemented the relationship in Python by utilizing an `articles` list within the Jounralist class. The `addArticle()` method adds an Article object to the said list. Three Article objects were added to the Journalist object, and their info was displayed in the terminal.

### Why did you store an object reference instead of copying its data?
I stored the Article objects in the `articles` list instead of copying their data into the Journalist class. This allows the latter object to maintain a consistent relationship with per Article object. Moreover, it allows the program to access the Article object's attributes and methods with ease.

### If your relationship uses many, why is a list appropriate?
A list is appropriate because one Journalist can be correlated with multiple Article objects. As I have mentioned in the previous questions, the `articles` list is able to simultaneously hold different Article instances. And in my program, it comprises the three Articles that were supplied to the Journalist object.