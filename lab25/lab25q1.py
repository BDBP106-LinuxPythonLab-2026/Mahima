class Car:
    showroom="NewAge"
    def __init__(self,make,model,year,color):
        self.started=False
        self.speed=0
        self.max_speed=200
        self._make=make
        self.model=model
        self.year=year
        self.color=color

    def __str__(self):
        return f"{self.make} {self.model} {self.color} ({self.year})"

    @property
    def make(self):
        return self._make
    @classmethod
    def change_showroom(cls,value):
        cls.showroom=value

    @staticmethod
    def show_intro_message():
        print("This is a class that handles information about cars.")


#1st instance
toyota_camry=Car("Toyota","Camry","2022","Red")
print(toyota_camry.make)
print(toyota_camry.model)
print(toyota_camry.year)
print(toyota_camry.color)

ford_mustang=Car("Ford","Mustang","2022","Black")
print(ford_mustang.make)
print(ford_mustang.model)
print(ford_mustang.year)
print(ford_mustang.color)
print(ford_mustang.speed)
print(ford_mustang.max_speed)
print(ford_mustang.started)

print(Car.make)  #we get an attribute error stating that make is not an attribute of Car
#to fix this we can define a getter function which will allow us to access the attribute as an class attribute instead of an instance attribute
#however it will return an property object as an output when not defined
print(toyota_camry.make)
print(Car.__dict__) #the result is all the functions and attributes associated with the class
print(Car.showroom)
print(Car.__dict__) #the class attribute showroom is also present along with change showroom in addition to the previously shown attributes and methods
print(toyota_camry.__dict__) #the output shows the instance attributes such as make, speed, year, etc with their value as a dict

print(str(toyota_camry))

Car.show_intro_message()
print(toyota_camry.showroom)