class Animal:
    def __init__(self, name):
        self.__name = name
    def set_name(self, name):
        self.__name = name
    @property
    def name(self):
        return self.__name
    def make_sound(self):
        print(f"{self.__name} makes a sound.")
    def eat(self):
        print(f"{self.__name} is eating.")

class Lion(Animal):
    def make_sound(self):
        print(f"{self.name} roars loudly!")
    def eat(self):
        print(f"{self.name} eats fresh meat.")
    @property
    def get_make_sound(self):
        return f"{self.name} roars loudly!"
    @property
    def get_eat(self):
        return f"{self.name} eats fresh meat."

class Elephant(Animal):
    def make_sound(self):
        print(f"{self.name} trumpets!")
    def eat(self):
        print(f"{self.name} eats grass and fruits.")
    @property
    def get_make_sound(self):
        return f"{self.name} trumpets!"
    @property
    def get_eat(self):
        return f"{self.name} eats grass and fruits."

class Monkey(Animal):
    def make_sound(self):
        print(f"{self.name} chatters!")
    def eat(self):
        print(f"{self.name} eats bananas.")
    @property
    def get_make_sound(self):
        return f"{self.name} chatters!"
    @property
    def get_eat(self):
        return f"{self.name} eats bananas."

lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

print("----------------------")
print(lion.get_make_sound)
print(lion.get_eat)

print("----------------------")
print(elephant.get_make_sound)
print(elephant.get_eat)

print("----------------------")
print(monkey.get_make_sound)
print(monkey.get_eat)
print("----------------------")