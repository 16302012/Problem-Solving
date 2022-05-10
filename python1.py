# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 16:06:26 2022

@author: User
"""
#RECEIVING INPUT
#age = input('Hi, how old are you? ')
#print('Oh! so you are ' + age + ' years old')

#TYPE CONVERSION
#birth_year  = input('Enter your birth year: ')
#age = 2022 - int(birth_year)
#print(age)

#salary = input('Enter your monthly salary: ')
#cost = input('Enter your monthly cost: ')
#Saving = float(salary) - float(cost)
#print(Saving)

#first_num = input('First: ')
#second_num = input('Second: ')
#sum = float(first_num) + float(second_num)
#print('Sum:' + str(sum))


#STRINGS
#course = ('python for beginners')
#print(course.find('f'))
#print(course.find('F'))
#print(course.replace('for', 'is a punmara for'))
#print('python' in course)

#ARITHMATIC OPERATORS
#x = 23
#x += 3
#print(x)

#LOGICAL OPERATORS
#price = 45
#print(not price>30)

#IF STATEMENT
#weight = input('Weight: ')
#input_type = input('(K)g or (L)bs: ')
#if input_type == 'K':
#    unit = float(weight) * 2.20462
#    print('Weight in Lbs: ' + str(unit))

#else:
#    unit = float(weight) / 2.20462
#    print('Weight in Kg: '+ str(unit))

#WHILE LOOPS
#i=1
#while i<=10:
#    print(i*'*')
#    i=i+1

#LISTS
#names = ['john','bob','smith','rob']
#names[2] = 'baal'
#print(names[0:2])
#print(names)

#LIST METHODS
#numbers = [1,2,3,4,5,6,7]
#numbers.append(8)
#numbers.insert(7, 8)
#numbers.remove(5)
#numbers.clear()
#print(len(numbers))
#print(1.5 in numbers)


#FOR LOOPS
#numbers = (1,2,3,4,5)
#for item in numbers:
#    print(item)

#RANGE() FUNCION
#numbers = range(10)
#numbers = range(2,10)
#numbers = range(2,10,2)
#print(numbers)
#for item in numbers:
#for item in range(5):
#    print(item)




#EXERCISE: FIZZ_BUZZ
#fizz_buzz = input( )
#if int(fizz_buzz)%3 == 0:
#    print('Fizz')
#elif int(fizz_buzz)%5 == 0:
#    print('Buzz')
#elif int(fizz_buzz)%3==0 and (fizz_buzz)%5==0:
#    print('FizzBuzz')
#else:
#    print(fizz_buzz)



#num={'0':'100',
#     '1':'200',
#     '2':'300'}

#for value in num.values():
#    print("\nIndex: "+key)
#    print("Value: "+str(value))

#places={}
#active=True
#while active:
#    name=input("What's your name? ")
#    place=input("If you could go to one place, where would you go? ")
    
#    places[name]=place

#    repeat=input("Do you have another place? ")
#    if repeat=='no':     
#        active=False
#print("Results")
#for name,place in places.items():
#    print(name+" would like to go to "+place)


#class Restaurant():
#    """A class representing a restaurant."""

#    def __init__(self, name, cuisine_type):
#        """Initialize the restaurant."""
#        self.name = name.title()
#        self.cuisine_type = cuisine_type
#        self.number_served = 0

#    def describe_restaurant(self):
#        """Display a summary of the restaurant."""
#        msg = f"{self.name} serves wonderful {self.cuisine_type}."
#        print(f"\n{msg}")

#    def open_restaurant(self):
#        """Display a message that the restaurant is open."""
#        msg = f"{self.name} is open. Come on in!"
#        print(f"\n{msg}")

#    def set_number_served(self, number_served):
#        """Allow user to set the number of customers that have been served."""
#        self.number_served = number_served
#
#    def increment_number_served(self, additional_served):
#        """Allow user to increment the number of customers served."""
#        self.number_served += additional_served
#
#class IceCreamStand(Restaurant):
#    def __init__(self,name,cuisine_type='ice cream'):
#        super().__init__(name, cuisine_type)
#        self.flavors=[]
#    def show_flavors(self):
#        print("The following flavors are available: ")
#        for flavor in self.flavors:
#            print(flavor.title())
#icecream=IceCreamStand('Radisson')
#icecream.flavors=['vanilla','chocolate','strawberry']
#icecream.describe_restaurant()
#icecream.show_flavors()
            

#class User():
#    def __init__(self, first_name, last_name, username, email, location):
#        self.first_name = first_name.title()
#        self.last_name = last_name.title()
#        self.username = username
#        self.email = email
#        self.location = location.title()
#        self.login_attempts = 0
#
#    def describe_user(self):
#        print(self.first_name+self.last_name)
#        print("Username:"+self.username)
#        print("Email:"+self.email)
#        print("Location:"+self.location)
#
#    def greet_user(self):
#        print(f"\nWelcome back, {self.username}!")
#
#    def increment_login_attempts(self):
#        self.login_attempts += 1

#    def reset_login_attempts(self):
#        self.login_attempts = 0
#
#class Admin(User):
#    def __init__(self, first_name, last_name, username, email, location):
#        super().__init__(first_name, last_name, username, email, location)
#        self.privileges = Privileges()

#class Privileges():
#    def __init__(self, privileges=[]):
#        self.privileges = privileges
#
#    def show_privileges(self):
#        print("\nPrivileges:")
#        if self.privileges:
#            for privilege in self.privileges:
#                print(f"- {privilege}")
#        else:
#            print("- This user has no privileges.")
#

#eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
#eric.describe_user()
#
#eric.privileges.show_privileges()
#
#print("\nAdding privileges...")
#eric_privileges = [
#    'can reset passwords',
#    'can moderate discussions',
#    'can suspend accounts',
#    ]
#eric.privileges.privileges = eric_privileges
#eric.privileges.show_privileges()

#class Car():
#    """A simple attempt to represent a car."""

#    def __init__(self, manufacturer, model, year):
#        """Initialize attributes to describe a car."""
#        self.manufacturer = manufacturer
#        self.model = model
#        self.year = year
#        self.odometer_reading = 0
        
#    def get_descriptive_name(self):
#        """Return a neatly formatted descriptive name."""
#        long_name = f"{self.year} {self.manufacturer} {self.model}"
#        return long_name.title()
#    
#    def read_odometer(self):
#        """Print a statement showing the car's mileage."""
#        print(f"This car has {self.odometer_reading} miles on it.")
        
#    def update_odometer(self, mileage):
#        """
#        Set the odometer reading to the given value.
#        Reject the change if it attempts to roll the odometer back.
#        """
#        if mileage >= self.odometer_reading:
#            self.odometer_reading = mileage
#        else:
#            print("You can't roll back an odometer!")
    
#    def increment_odometer(self, miles):
#        """Add the given amount to the odometer reading."""
#        self.odometer_reading += miles

#class Battery():
#    """A simple attempt to model a battery for an electric car."""

#    def __init__(self, battery_size=75):
#        """Initialize the batteery's attributes."""
#        self.battery_size = battery_size

#    def describe_battery(self):
#        """Print a statement describing the battery size."""
#        print(f"This car has a {self.battery_size}-kWh battery.")

#    def get_range(self):
#        """Print a statement about the range this battery provides."""
#        if self.battery_size == 75:
#            range = 260
#        elif self.battery_size == 100:
#            range = 315
            
#        message = f"This car can go approximately {range}"
#        message += " miles on a full charge."
#        print(message)

#    def upgrade_battery(self):
#        """Upgrade the battery if possible."""
#        if self.battery_size == 75:
#            self.battery_size = 100
#            print("Upgraded the battery to 100 kWh.")
#        else:
#            print("The battery is already upgraded.")
    
        
#class ElectricCar(Car):
#    """Models aspects of a car, specific to electric vehicles."""

#    def __init__(self, manufacturer, model, year):
#        """
#        Initialize attributes of the parent class.
#        Then initialize attributes specific to an electric car.
#        """
#        super().__init__(manufacturer, model, year)
#        self.battery = Battery()


#print("Make an electric car, and check the range:")
#my_tesla = ElectricCar('tesla', 'roadster', 2019)
#my_tesla.battery.get_range()

#print("\nUpgrade the battery, and check the range again:")
#my_tesla.battery.upgrade_battery()
#my_tesla.battery.get_range()


#def hello(func):
#    func()
#def greet():
#    print("still here!!")
#a=hello(greet)
#print(a)

#HIGHER ORDER FUNCTION
#def greet(func):
#    func()
        
#def greet2():
#    def func():
#        return 50
#    return func

#DECORATOR







