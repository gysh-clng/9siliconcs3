# Advanced Class Relationships
## Previous Activities
[classAttrib](classAttributesMethods.md)
[classRel](classRelationships.md)

## Existing System Description:
The existing system is based on the Journalist class and the Article class. The former class has attributes like Name, Field, Availability, and writtenArticles. Moreover, it also has methods for writing, submitting, and covering articles. The said classes share this one-to-many relationship since one Journalist could be assigned or associated with zero or more Article objects (Article assignments if we correlate it IRL). In connection to OOPAct 4, this seeks to improve the ongoing system by adding an inheritance and aggregation relationship.
## Inheritance Relationship
Campus Journalist
IS-A
Journalist
Parent: Journalist
Child: Campus Journalist
Explanation: A Campus Journalist is a type of the parent Journalist because campus journalists perform their duties like professional ones, but not beyond their campus vicinities. 

## Inheritance UML
![Inheritance](images/inheritanceDiagram.png)

## Composition/Aggregation
Relationship: Aggregation --- Journalist HAS-A Article
Explanation: The Journalist and Article classes have an aggregtion relationship because a Journalist can be correlated with many Article objects, while the Article objects can exist as indepedent facets. The Article objects were created separately and added to the Journalist's `articles` list using `addArticle()`. Thus, the Article objects aren't dependent on the Journalist's existence.

## Advanced UML Diagram
![Advanced UML](images/advancedClassDiagram.png)

## Python Implementation
[Source Code](advancedRelationships.py)

## Test Run
![Test](images/advancedTestRun.png)

## Object Diagram
![Objects](images/advancedObjectDiagram.png)

## Reflection
Answers:
### 1. Why did you choose your inheritance relationship?
I chose inheritance because a CampusJournalist is a type of Journalist, so it shares the same characteristics and behaviors of the Journalist class. The only difference is that a CampusJournalist serves the student body and not the general masses. A CampusJournalist can use the attributes and methods already defined in the Journalist class while also having its own attribute, which is Campus. This makes inheritance appropriate because the child class is an IS-A type of the parent.

### 2. How did inheritance reduce duplicate code?
Inheritance reduces duplicate code because I didn't have to rewrite the attributes and methods of the Journalist class inside CampusJournalist. The latter class can inherit the available features from Journalist, and add the information that is solely specific to campus journalism. This makes the code more efficient and organized.

### 3. Why is your HAS-A relationship Composition or Aggregation?
My Journalist-Article classes relationshop is Aggregation since the Article objects can exist independently from the Journalist object. The Article objects are made separately and then added to the Journalist's `articles` list by utilizng `addArticle()`. Therefore, if the Journalist object is removed, then the Article objects can still independently exist.

### 4. What is the difference between Association from Part III and the advanced relationship you implemented?
The Association relationship in Part III described the correlation between Journalist and Article, where one Journalist can be connected with zero or more Articles. In this new activity, the relationship is further identified as Aggregation as the Article objects can exist independently and are connected to the Journalist as contained objects. Aggregation gives it more information about the lifecycle and ownership of the objects than the genersl Association relationship.

### 5. How does your design follow the DRY principle? 
My design follows the DRY principle by using inheritance instead of rewriting the same features found in Journalist into CampusJournalist. The common attributes and methods are defined once in the Journalist class and inherited by CampusJournalist. This makes the program easier to maintain since changes to shared parent class behavior do not adhere to duplication in the child class. 
