# https://pynative.com/python-object-oriented-programming-oop-exercise/#h-oop-exercise-1-create-a-class-with-instance-attributes

# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed= max_speed
        self.mileage=mileage

# Create a Vehicle class without any variables and methods
class Vehicle:
   pass

# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        print('in car class')

class Car(Vehicle):
            pass

# Create a Bus class that inherits from the Vehicle class.
# Give the capacity argument of Bus.seating_capacity() a default value of 50.

# Use the following code for your parent Vehicle class.

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    # super().__init__()

    def seating_capacity(self, capacity=50):
        return super().seating_capacity(50)

# Define a property that must have the same value for every class instance (object)
# Define a class attribute ”color” with a default value white. I.e., Every Vehicle should be white.
#
# Use the following code for this exercise.

class Vehicle:
    color='white'

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


    def property(self):
        print("Color: {}, Vehicle name: {}, Speed: {}, Mileage: {}".format(Vehicle.color, self.name, self.max_speed, self.mileage))

class Bus(Vehicle):
    def property(self):
        print("Color: {}, Vehicle name: {}, Speed: {}, Mileage: {}".format(Vehicle.color, self.name, self.max_speed, self.mileage))

    pass

class Car(Vehicle):
    def property(self):
        print("Color: {}, Vehicle name: {}, Speed: {}, Mileage: {}".format(Vehicle.color, self.name, self.max_speed, self.mileage))
    pass

# bus =Bus('Volvo', 180, 12)
# bus.property()
# car =Car('Audi', 240, 12)
# car.property()


# Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is
# seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge.
# So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

#
# Note: The bus seating capacity is 50. so the final fare amount should be 5500. You need to override the fare() method of a Vehicle class in Bus class.
#
# Use the following code for your parent Vehicle class. We need to access the parent class from inside a method of a child class.

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def __init__(self,name, mileage, capacity, price):
        self.price = price
        super().__init__(name, mileage, capacity)
    def fare(self):
        amount_veh = super().fare()
        amount = amount_veh  * (10/100)
        return amount_veh + amount
    pass

# School_bus = Bus("School Volvo", 12, 50, 20000)
# print("Total Bus fare is:", School_bus.fare())

# Write a program to determine which class a given Bus object belongs to.


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass



School_bus = Bus("School Volvo", 12, 50)
print(isinstance(School_bus, Bus))
print(type(School_bus))

 # Determine if School_bus is also an instance of the Vehicle class

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
print(isinstance(School_bus, Vehicle))