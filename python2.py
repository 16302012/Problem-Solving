# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 21:22:38 2022

@author: User
"""

#names = [2,7,1,5,8]
#print(sorted(names))

#num = list(range(1,11))
#print(num)

#print(list(range(1,100001)))
#multiples = []
#for value in range(3,31):
#   multiple = value**3
#   multiples.append(multiple)
#print(multiples)

#cube = [value**3 for value in range(1,11)]
#print(cube)


#banned_users = ['mary','sam','rob','smith']
#user = input('User: ')
#if user not in banned_users:
#    print(user.title() + ", You are good to go!")

#car = 'subaru'
#print("is car == 'subaru'? i predict True")
#print(car == 'subaru')

#DICTIONARY
#alien_0={'color':'green','points':10}
#print('You just earned '+ str(alien_0['points']) +' points!')

#msg = 'We can personalize the message for you'
#msg += '\nWhat is your first name?'

#name = input(msg)
#print('Hello!'+ name)


#age = int(input("How old are you? "))

#msg = "Tell me something and I'll repeat it back to you"
#msg += "Enter 'quit' to end the program\n"

#message = ''
#while message != 'quit':
#    message = input(msg)
#    print(message)
    
    
#msg = "Tell me something and I'll repeat it back to you"
#msg += "Enter 'quit' to end the program\n"

#active = True
#while active:
#    message = input(msg)
#    if message == 'quit':
#        break
#    else:
#        print(message)


#current_num = 0
#while current_num<10:
#    current_num+=1
#    if current_num%2 == 0:
#        continue
#    print(current_num)

#unconfirmed_users = ['brian','chloe','karen']
#confirmed_users =[]
#while unconfirmed_users:
#    current_user=unconfirmed_users.pop()
#    print('Verifying users: '+current_user.title())
#    confirmed_users.append(current_user)
    
#print("\nThe followings are confirmed:")
#for confirmed_user in confirmed_users:
#    print(confirmed_user.title())


#FUNCTIONS
#def greet_user():
#    """Display a greeting"""
#    print("Hello!")
#greet_user()

#def greet_user(username):
#    print("Hello"+username.title())
#greet_user(' raisa')

#def favorite_book(title):
#    print("The book I'm reading is: "+title.title())
#favorite_book('alice in wonderland')

#def des_pet(animal_type,name):
#    print("I have a "+animal_type.title())
#    print("My animal's name is "+name.title())
#des_pet('hamster','meemo')
#des_pet('dog','jojo')

#des_pet(animal_type='hamster',name='meemo')"""KEYWORD ARGUMENT"""

#DEFAULT VALUE FOR PARAMETERS
#def des_pet(animal_type='dog',pet_name='jojo'):
#    print("I've a pet "+animal_type)
#    print("My pet's name is "+pet_name.title())
#des_pet()

#RETURN STATEMENT
#def formatted_name(first_name,last_name):
#    full_name=first_name+' '+last_name
#    return full_name.title()
#name=formatted_name('jimi', 'hendrix')
#print(name) 


#num = int(input("Index: "))
#num = int(num)
#if num==0:
#    print("Value: 100")
#elif num==1:
#    print("Value: 200")
#elif num==2:
#    print("Value: 300")
#else:
#    print('tor matha!!')


#def name(f_name,l_name,m_name=""):
#    if m_name:
#        full_name=f_name+' '+m_name+' '+l_name
#    else:
#        full_name=f_name+' '+l_name
#    return full_name.title()
#person=name('Israt','Saheba','Jahan')
#print(person)
#person=name('Raisa','Azad')
#print(person)

#RETURNING A DICTIONARY
#def animals(animal_type,weight,age):
#    animal_list={'Type':animal_type,'Weight':weight,'Age':age}
#    return animal_list
#animal=animals('dog','25','4')
#print(animal)

#def animals(animal_type,weight,age=''):
#    details={'Type':animal_type,'Weight':weight,'Age':age}
#    if age:
#        details['Age']=age
#    return details
#animal=animals('Dog', '37',age=4)
#print(animal)


#def make_album(artist_name,album_title,tracks):
#    details={'Artist name':artist_name,'Album title':album_title,'Total tracks':tracks}
#    return details
#album_detail=make_album('machine gun kelly','Heathens',tracks=8)
#print(album_detail)

#def make_album(artist_name,album_title):
#    details={'Artist name':artist_name,'Album title':album_title}
#    return details
#while True:
#    print("Enter 'q' at any time to quit" )
#    ar_name=input("Name of the artist: ")
#    if ar_name=='q':
#        break
#    al_name=input("Name of the album: ")
#    if al_name=='q':
#        break
#    album_details=make_album(ar_name,al_name)
#    print(album_details)

#RETURNING LIST
#def greet_user(names):
#    for name in names:
#        msg='Hello '+name.title()+'!'
#        print(msg)
#username=['Tyga','Richard','Scot']
#greet_user(username)


#WITHOUT FUNCTIONS
#unprinted_designs=['iphone','robot','dandelions']
#completed_models=[]
#while unprinted_designs:
#    current_design=unprinted_designs.pop()
#    print("Models: "+current_design)
#    completed_models.append(current_design)
#print("\nFollowing models have been printed: ")
#for completed_model in completed_models:
#    print(completed_model)
 
#WITH FUNCTIONS
#def print_models(unprinted_designs,completed_models):
#    while unprinted_designs:
#        current_design=unprinted_designs.pop()
#        print("Models: "+current_design)
#        completed_models.append(current_design)
        
#def show_completed_model(completed_models):
#    print("\nThe following models have been printed: ")
#    for completed_model in completed_models:
#        print(completed_model)
        
#unprinted_designs=['iphone','robot','dandelions']
#completed_models=[]
#print_models(unprinted_designs,completed_models)
#show_completed_model(completed_models)

#PREVENTING A LIST FROM MODIFYING
#def print_models(unprinted_designs,completed_models):
#    while unprinted_designs:
#        current_design=unprinted_designs.pop()
#        print("Model: "+current_design)
#        completed_models.append(current_design)
#def show_completed_model(completed_models):
#    print("\nThe following models have been printed: ")
#    for completed_model in completed_models:
#        print(completed_model)
#unprinted_designs=['iphone','robot','dandelions']
#completed_models=[]
#print_models(unprinted_designs[:],completed_models)
#show_completed_model(completed_models)

#def show_magician(names):
#    for name in names:
#        msg="Hello "+name.title()+"!"
#        print(msg)
#usernames=['hannah','rai','tyga']
#show_magician(usernames)


#def make_pizza(size,*toppings):
#    print("\nMaking a "+str(size)+"-inch pizza with following toppings: ")
#    for topping in toppings:
#        print(" "+str(topping))
    
#make_pizza(12,'pepperoni')
#make_pizza(10,'extra cheese','pepperoni')

#def build_profile(first, last, **user_info):
#    profile = {}
#    profile['first_name'] = first
#    profile['last_name'] = last
#    for key, value in user_info.items():
#        profile[key] = value
#user_profile = build_profile('albert', 'einstein',
#                             location='princeton',
#                             field='physics')
#print(user_profile)

#def make_sandwich(*items):
#    print("\nMaking a sandwich with following items: ")
#    for item in items:
#        print("-"+str(item))
#make_sandwich('cheese','pastrami')
#make_sandwich('bacon','cheddar cheese','pastrami')
#make_sandwich('chicken','cheese','pickle')

#def build_profile(first,last,**user_info):
#    profile={}
#    profile['First name']=first
#    profile['Last name']=last
#    for key,value in user_info.items():
#        profile[key]=value
#user_profile=build_profile('Raisa', 'Azad', 
#                           Department='CSE',
#                           University='CIU',
#                           Location='Chattogram')
#print(user_profile)

#def make_car(manufacturer,model,**options):
#    car_dict={'manufacturer':manufacturer.title(),
#              'model':model.title()}
#    for option,value in options.items():
#        car_dict[option]=value
#        return car_dict
#my_car=make_car('subaru', 'outback', color='blue',tow_package=True)
#print(my_car)
#my_car_2=make_car('bmw', 'accord', year='1991',headlights='popup',color='black')
#print(my_car_2)

#import python3module as p
#p.make_pizza(12,'pastrami')
#p.make_pizza(10, 'extra cheese')

#from python3module import *
#make_pizza(12,'pastrami')
#make_pizza(10, 'extra cheese')

#import python3module as p
#unprinted_designs=['iphone','robot','dandelions']
#completed_models=[]
#p.print_models(unprinted_designs,completed_models)
#p.show_completed_model(completed_models)

#CLASS
#class Dog():
#    def __init__(self,name,age):
#        self.name=name
#        self.age=age
#    def sit(self):
#        print(self.name.title()+" is now sitting")
#    def roll_over(self):
#        print(self.name.title()+" has rolled over!")


#my_dog=Dog('lukas', 6)
#your_dog=Dog('willie',4)
#print("My dog's name is "+my_dog.name.title())
#print("My dog is "+str(my_dog.age)+"years old")
#print("\nYour dog's name is "+your_dog.name.title())
#print("Your dog is "+str(your_dog.age)+"years old")
#my_dog.sit()
#my_dog.roll_over()
#your_dog.sit()
#your_dog.roll_over()

#class Restaurant():
#    def __init__(self,name,cuisine_type):
#        self.name=name
#        self.cuisine_type=cuisine_type
#    def describe_restaurant(self):
#        print(self.name.title()+" has "+self.cuisine_type+"!")
#    def open_restaurant(self):
#        print(self.name.title()+" is now open")
#restaurant_1=Restaurant('raddison', 'lebanese')
#print(restaurant.name.title())
#print(restaurant.cuisine_type.title())
#restaurant_2=Restaurant('Mean Queen', 'japanese')
#restaurant_3=Restaurant('oberoi', 'indian')
#restaurant_1.describe_restaurant()
#restaurant_2.describe_restaurant()
#restaurant_3.describe_restaurant()
#restaurant.open_restaurant()


#class Car():
#    def __init__(self,make,model,year):
#        self.make=make
#        self.model=model
#        self.year=year
#    def descriptive_name(self):
#        details=self.make+' '+self.model+' '+str(self.year)
#        return details.title()
#my_car=Car('audi','a4',2016)
#print(my_car.descriptive_name())

#class Car():
#    def __init__(self,make,model,year):
#        self.make=make
#        self.model=model
#        self.year=year
#        self.odometer=25
#    def descriptive_name(self):
#        details=self.make+' '+self.model+' '+str(self.year)
#        return details.title()
#    def read_odometer(self):
#        print("This car has "+str(self.odometer)+" mile.")
#    def update_odometer(self,mileage):
#        if mileage>=self.odometer:
#            self.odometer=mileage
#        else:
#            print("You can't roll back an odometer!")
#    def increment_odometer(self,miles):
#        self.odometer+=miles
        
#my_car=Car('audi','a4',2016)
#print(my_car.descriptive_name())
#my_car.odometer=23
#my_car.update_odometer(23500)
#my_car.read_odometer()
#my_car.increment_odometer(100)
#my_car.read_odometer()

#class Restaurant():
#    def __init__(self,name,cuisine_type):
#        self.name=name
#        self.cuisine_type=cuisine_type
#        self.number_served=25
#    def describe_restaurant(self):
#        print(self.name.title()+" has "+self.cuisine_type+"!")
#    def open_restaurant(self):
#        print(self.name.title()+" is now open")
#    def customer_no(self):
#        print("This restaurant has served "+str(self.number_served)+" customers.")
#restaurant=Restaurant('raddison', 'lebanese')
#print(restaurant.name.title())
#print(restaurant.cuisine_type.title())
#restaurant.customer_no()

#class Restaurant():
#    def __init__(self,name,cuisine_type):
#        self.name=name
#        self.cuisine_type=cuisine_type
#    def describe_restaurant(self):
#        print(self.name.title()+" has "+self.cuisine_type+"!")
#    def open_restaurant(self):
#        print(self.name.title()+" is now open")
#    def set_number_served(self):
#        self.number_served=number_served
#restaurant=Restaurant('raddison', 'lebanese')
#print(restaurant.name.title())
#print(restaurant.cuisine_type.title())
#restaurant.number_served=25
#print("Number served: "+str(restaurant.number_served))

#class Car():
#    def __init__(self,make,model,year):
#        self.make=make
#        self.model=model
#        self.year=year
#        self.odometer=25
#    def descriptive_name(self):
#        details=self.make+' '+self.model+' '+str(self.year)
#        return details.title()
#    def read_odometer(self):
#        print("This car has "+str(self.odometer)+" mile.")
#    def update_odometer(self,mileage):
#        if mileage>=self.odometer:
#            self.odometer=mileage
#        else:
#            print("You can't roll back an odometer!")
#    def increment_odometer(self,miles):
#        self.odometer+=miles
#    def fill_gas_tank(self):
#        print("This car has a gas tank")
#class Battery():
#    def __init__(self,battery_size=70):
#        self.battery_size=battery_size
#    def describe_battery(self):
#        print("This car has "+str(self.battery_size)+" kWh battery")
#    def get_range(self):
#        if self.battery_size==70:
#            range=240
#        elif self.battery_size==85:
#            range=270
#        msg="This car can go approx. "+str(self.battery_size)+" miles on a full charge"
#        print(msg)
#class ElectricCar(Car):
#    def __init__(self,make,model,year):
#        super().__init__(make, model, year)
#        self.battery=Battery()
#    def describe_battery(self):
#        print("This car has "+str(self.battery_size)+" kWh battery")
#    def fill_gas_tank(self):
#        print("This car doesn't need a gas tank")
#my_tesla=ElectricCar('tesla', 'model S', 2010)
#print(my_tesla.descriptive_name())
#my_tesla.battery.describe_battery()
#my_tesla.fill_gas_tank()
#my_tesla.battery.get_range()

#user_name=input('User name: ')
#password=input('Password: ')
#pass_len=len(password)
#final_pass='*' * pass_len
#print(f'Hi {user_name}! your password {final_pass} is {pass_len} letters long')

#friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

#friends.append('Stanley')
#friends.sort()

#print(friends)

#TERNARY OPERATOR
#is_friend=True
#can_text='message allowed' if is_friend else 'messages are not allowed'

#print(can_text)


#picture = [
#  [0,0,0,1,0,0,0],
#  [0,0,1,1,1,0,0],
#  [0,1,1,1,1,1,0],
#  [1,1,1,1,1,1,1],
#  [0,0,0,1,0,0,0],
#  [0,0,0,1,0,0,0]
#]

#for image in picture:
#    for pixel in image:
#        if pixel==1:
#            print('$',end=' ')
#        else:
#            print(' ', end=' ')
#    print('')

#def checkDriverAge(age):
#    if int(age) < 18:
#        print("Sorry, you are too young to drive this car. Powering off")
#    elif int(age) > 18:
#        print("Powering On. Enjoy the ride!");
#    elif int(age) == 18:
#        print("Congratulations on your first year of driving. Enjoy the ride!")        
#checkDriverAge(18)

#class Cat:
#    species = 'mammal'
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
#cat1= Cat('Milo', 4)
#cat2= Cat('Enzo', 2)
#cat3= Cat('Garfield', 5)
#
#def get_oldest_cat(*args):
#    return max(args)

#print(f"The oldest cat is {get_oldest_cat(cat1.age, cat2.age, cat3.age)} years old.")


#class Toy():
#  def __init__(self, color, age):
#    self.color = color
#    self.age = age
#    self.my_dict = {
#        'name':'Yoyo',
#        'has_pets': False,
#    }

#  def __str__(self):
#    return f"{self.color}"

#  def __len__(self):
#    return 5
#
#  def __del__(self):
#    return "deleted"

#  def __call__(self):
#      return('yes??')

#  def __getitem__(self,i):
#      return self.my_dict[i]
  
#  def __price__(self):
#      return 60
#  def __reduce__(self):
#      return "I am reduced!!"
  


#action_figure = Toy('red', 0)
#print(action_figure.__str__())
#print(str(action_figure))
#print(len(action_figure))
#print(action_figure())
#print(action_figure['name'])
#print(action_figure.__price__())
#print(action_figure.__reduce__())

#class SuperList(list):
#    def __len__(self):
#        return 100
#superlist1= SuperList()
#print(len(superlist1))
#superlist1.append(5)
#print(superlist1[0])


#from functools import reduce
#my_pets = ['sisi', 'bibi', 'titi', 'carla']
#def capitalize(string):
#    return string.upper()
#print(list(map(capitalize, my_pets)))

#my_strings = ['a', 'b', 'c', 'd', 'e']
#my_numbers = [5,4,3,2,1]
#print(list(zip(my_strings,my_numbers)))

#scores = [73, 20, 65, 19, 76, 100, 88]
#
#def is_smart_student(score):
#    return score > 50

#print(list(filter(is_smart_student, scores)))

#def accumulator(acc, item):
#    return acc + item

#print(reduce(accumulator, (my_numbers + scores)))

#a= [(0,2),(4,3),(10,-1),(9,9)]
#a.sort(key=lambda x: x[1])
#print(a)