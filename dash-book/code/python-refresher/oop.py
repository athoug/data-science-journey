# -------- Object-Oriented Programming --------
'''
At the heart of object-oriented Python are classes. Classes are blueprints for creating objects. A class description tells you what an object looks like and what it can do, respectively known as the object’s data and functionality. The data is defined in attributes, which are variables associated with a given object. The functionality is defined in methods, which are functions associated with the given object. Let’s see these concepts in action using Harry Potter examples. First we’ll make a class with attributes but no methods. Here we create a Muggle class and make two Muggle objects from it:
'''


class Muggle:
    def __init__(self, age, name, liking_person):
        self.age = age
        self.name = name
        self.likes = liking_person


vernon = Muggle(52, "Vernon", None)
petunia = Muggle(49, 'Petunia', vernon)
