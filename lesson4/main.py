# weight_lower_limit = 75.5
# weight_higher_limit: float = 100.0

# weight = float(input("Enter your weight: "))

# if weight > weight_higher_limit:
#     if weight_higher_limit > 125.5:
#         print("what the fuck")
#     print("Mindaugas is kebab")
# elif weight < weight_lower_limit:
#     print("Mindaugas is sasyska")
# else:
#     print("Mindaugas is cool")    

# if weight > weight_higher_limit: 
#     print("Mindaugas is kebab")
# print("test is sucsefull")


# list = []
# number1 = 4
# number2 = 6
# number3 = 8
# number4 = 9

# Program takes 3 random numbers as user input. 
# Update lsit and tuple data structures with those values and print it.



# first_nr = input("enter first number: ")
# second_nr = input("enter second number: ")
# third_nr = input("enter third number: ")

# my_list = []
# my_tuple = (first_nr, second_nr, third_nr)
# my_list.append(first_nr)
# my_list.append(second_nr)
# my_list.append(third_nr)

# print(my_list)
# print(my_tuple)


# nr_1 = int(input("Enter 1 no: "))
# nr_2 = int(input("Enter 2 no: "))
# nr_3 = int(input("Enter 3 no: "))
# nr_4 = int(input("Enter 4 no: "))
# nr_5 = int(input("Enter 5 no: "))
# nr_6 = int(input("Enter 6 no: "))
# nr_7 = int(input("Enter 7 no: "))
# nr_8 = int(input("Enter 8 no: "))
# nr_9 = int(input("Enter 9 no: "))
# nr_10 = int(input("Enter 10 no: "))

# my_list = []
# my_tuple_list = []

# if nr_1 < 50:
#     my_list.append(nr_1)
# else:
#     my_tuple_list.append(nr_1)



# user inputs two numbers a & b if nr a is > than b, we print sum of those numbers, otherwise we return multiplication   
# 
# a = input("Enter number: ") 
# b = input("Enter number: ")
# if a > b:
#     print(a+b)
# else:
#     print(a*b) 


# if nr_2 < 50:
#     my_list.append(nr_2)
# else:
#     my_tuple_list.append(nr_2)
# if nr_3 < 50:
#     my_list.append(nr_3)
# else:
#     my_tuple_list.append(nr_3)
# if nr_4 < 50:
#     my_list.append(nr_4)
# else:
#     my_tuple_list.append(nr_4)
# if nr_5 < 50:
#     my_list.append(nr_5)
# else:
#     my_tuple_list.append(nr_5)
# if nr_6 < 50:
#     my_list.append(nr_6)
# else:
#     my_tuple_list.append(nr_6)
# if nr_7 < 50:
#     my_list.append(nr_7)
# else:
#     my_tuple_list.append(nr_7)
# if nr_8 < 50:
#     my_list.append(nr_8)
# else:
#     my_tuple_list.append(nr_8)
# if nr_9 < 50:
#     my_list.append(nr_9)
# else:
#     my_tuple_list.append(nr_9)
# if nr_10 < 50:
#     my_list.append(nr_10)
# else:
#     my_tuple_list.append(nr_10)


# print(my_list)
# print(tuple(my_tuple_list))

# print(max(my_list) - min(my_list))
# print(sum(my_tuple_list))

# nr_1 = 25
# nr_2 = 5 
# print((nr_1)/(nr_2))
# a = 5
# b = 25 
# c = float(a + b)
# d = a * b
# e = a / b
# f = b // a
# g = a % b 
# h = a ** b
# print(c, d, e, f, g, h)

# name = "Code Academy"
# print(name.upper())

# greeting = "Hello, my name is"
# name = "Tom"
# completed_greeting = f"{greeting} {name}"
# print(completed_greeting)

# greeting = "Hello, my name is"
# name = "Tom"
# completed_greeting = greeting + " " + name
# print(completed_greeting)

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print(f"Your name is {name}, you are {age} years old")

# my_list = []
# name = "Tom"
# my_list.append(name)
# print(my_list)

# my_list = [1, 2, 3, 4]
# print(my_list.count(2)) # 2

# my_list = [1, 2, 3]
# my_list[2] = 5
# print(my_list)

# my_list = [1, 2, 3]
# for item in my_list:
#     print(item + 20)

# empty_tuple = ()
# tuple_single_item = (1,)
# another_tuple = (1, 2, 3)

# my_list = ["name", 123, None, True]
# print(len(my_list)) #4

# my_list = [23, 56, 2, -99]
# print(min(my_list))


# Create a program, which takes 10 random numbers as user inputs.
# The program should produce list of input values what are less than 50 and tuple of all other values.
# After input is done, program should return the the mathematicaldiffernce between the highest and lowest number from non primary numbers, 
# and sum of primary numbers from tuple.


# a = 50 
# b = int(input("enter the number: "))
# if b >= a:
#   print(b)
# else:
#   print(a)



# a = int(input("enter nr: "))
# b = int(input("enter nr: "))
# c = int(input("enter nr: "))
# d = int(input("enter nr: "))
# if a < b and b < c:
#   print(f"first condition met: {b}")
# elif a > c:
#   print(f"second condition met: {a}")
# else:
#   print(f"third condition met. First number:{a}, second number:{b}, third number:{c}, fourth number:{d}") 

# name = input("Enter name: ")
# surename = input("Enter surename: ")
# age = int(input("Enter your age: "))
# age_cap = 21
# if age >= age_cap: 
#   print(f"than age is greater than 21: you're allowed")
# else:
#   print(f"than age is lower than 21: you're not allowed")

# import random
# random_number = random.randint(1, 10)
# guess_number = int(input("Guess the number from 1 to 10: "))
# if guess_number == random_number:
#   print(f"You've guessed it! It is {random_number}")
# else:
#   print(f"You haven't guessed, the right asnwer is: {random_number}")
  

"atnaujinimas"
