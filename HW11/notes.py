# class car(object):
#     def __init__(
#         self, make="Ford", model="Explorer", year="2019", mileage="2812", color="blue"
#     ):
#         self.__make = make
#         self.__model = model
#         self.__year = year
#         self.__mileage = mileage
#         self.__color = color

#     def getModel(self):
#         return self.__model


# myCar = car()
# print(myCar.getModel())


# class User(object):
#     def __init__(self,firstname):
#         self.firstname=firstname
    
#     @property
#     def returnName(self):
#         return self.firstname

# class Animal(object):
#     pass

# class Fox(Animal):
#     name="Fox"

# class Bear(Animal):
#     name="Bear"

# print(User("Animal").firstname)
# print(Fox().name)
# print(Bear().name)

class Mammal:
    def __init__(self,species):
        self.__species=species
    
    def show_species(self):
        print("I am a ",self.__species)
    
    def make_sound(self):
        print('Grrrr')

class Dog(Mammal):
    def __init__(self):
        Mammal.__init__(self,'Dog')
    
    def make_sound(self):
        print('Woof Woof')
    
class Cat(Mammal):
    def __init__(self):
        Mammal.__init__(self,'Cat')
    
    def make_sound(self):
        print('Meow')

def showMammalInfo(creature):
    if isinstance(creature,Mammal):
        creature.show_species()
        creature.make_sound()
    else:
        print("This is not a Mammal")

def main():
    mamamalObject = Mammal('regular animal')
    dog = Dog()
    cat=Cat()

    showMammalInfo(mamamalObject)
    showMammalInfo(dog)
    showMammalInfo(cat)
    showMammalInfo("String")

main()
    