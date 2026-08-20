# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
Encapsulation can be utilized by placing a product's data (e.g., name, price, stock quantity) inside a Product class. To add, the class can use methods such as `add_stock()` and `remove_stock` to control how stocks change over time. This maintains the product's system organized while ensuring the program prevents itself from changing the data incorrectly.
### 2. Abstraction

Abstraction can be used by hiding the inessential details of how the inventory system works internally. For example, a method such as `sell_product()` could handle the stock checking and reducing the quantity without demanding the user to know every step. This makes the program easier to use and understand.

### 3. Inheritance

Inheritance can be used if the store has a vast variety of products that share similar properties. Sample classes like  `SolidFoodProducts` and `DrinkProducts` could inherit simple properties from a general `Products` class. This makes the inventory easier to work with as it avoids repeated code.
### 4. Polymorphism

Polymorphism can allow product types' system to experience more flexibility. It promotes flexibility by having it responded differently to the same provided prompt. For example, both `SolidFoodProducts` and `DrinkProducts` could have a `display_info()` method, but each class could display information specific to that type of product.
## Reflection

I believe Encapsulation would be the most useful and utilized pillar for improving the sari-sari store inventory system. It would gather and safekeep each product's information --- name, price, and stock --- organized within a Product object. It would also allow certain methods to manipulate how the inventory is changed over time, reducing the possibility of incorrect data. This would make the inventory system easier to manage and monitor as the product amount increases.