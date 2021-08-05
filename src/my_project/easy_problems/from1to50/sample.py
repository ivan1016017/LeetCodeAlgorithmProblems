class Animal():
    def __init__(self, type):
        self.type = type
        print("I am an animal")



class Dog(Animal):
    def __init__(self, name):
        self.name = name


    def walk(self, name):
        print("{0} is running ".format(name))

    def bark(self, name):
        print("{0} is barking ".format(name))

class Bird(Animal):
    def __init__(self, type, name, weight):
        Animal.__init__(self,type)
        self.name = name
        self.weight = weight


animal = Animal("terrestrial")
print(animal.type)

dog = Dog(animal)
dog.walk("Sasha")
print(dog.name.type)



my_bird = Bird("aerial", "rio", "light")
print(my_bird.type)
print(my_bird.name)
print(my_bird.weight)

class Eagle():

    def __init__(self, name ):
        self._name = name


    @property
    def name(self):
        print("getter of Eagle called")
        return self._name

    @name.setter
    def name(self,value):
        print("setter of name called")
        self._name = value

sample = Eagle("Sample")
print(sample.name)
sample.name = "Golden Eagle"

variable = sample.name
print(sample.name)

sample.name("blabla")
print(sample.name)




