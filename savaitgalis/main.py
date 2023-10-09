
# number = input("Enter the number with minimum 3 digits after point: ")
# no_check_dot = number.replace(".","").isnumeric()
# no_check_comma = number.replace(",","").isnumeric()

# if no_check_dot and len(number)>=5:
#     number = round(float(number), 1)
#     print(f"Rounden number value: {number}")
# elif no_check_comma and len(number)>=5:
#     number = number.replace(",",".")
#     number = round(float(number),1)
#     print(f"Rounden number value: {number}")
# else:
#     print(f"You have failed enter the number")

# user_name = input("Enter your name: ")
# user_age = int(input("Enter your age: "))
# date_of_birth = 2023 - user_age
# print(date_of_birth)

# user_sentence = input("Enter your sentence: ")
# # print(user_sentence[::-1])
# print(user_sentence[::2])

# no_nr1 = int(input("Enter your number: "))
# no_nr2 = int(input("Enter your number: "))
# multiplication = no_nr1 * no_nr2
# print(multiplication)

# my_list = [1, 2, 2.5, 3, 25, 87]
# number_in_my_list = 1
# number_in_my_list1 = 2
# number_in_my_list2 = 2.5
# number_in_my_list3 = 3
# number_in_my_list4 = 25
# number_in_my_list5 = 87
# multiplication = number_in_my_list * number_in_my_list1 * number_in_my_list2 * number_in_my_list3 * number_in_my_list4 * number_in_my_list5
# print(multiplication)

# my_list = number_in_my_list + number_in_my_list1 + number_in_my_list2 + number_in_my_list3 + number_in_my_list4 + number_in_my_list5
# print(my_list)


# my_list = []
# number = 1
# number1 = 2
# number2 = 2.5
# number3 = 3
# number4 = 25
# number5 = 87
# my_list.append(number)
# my_list.append(number1)
# my_list.append(number2)
# my_list.append(number3)
# my_list.append(number4)
# my_list.append(number5)
# print(*my_list, sep = "---")

# my_list = [1, 2, 2.5, 3, 25, 87]
# print(max(my_list))

# my_list = []
# str1 = "123"
# str2 = "abc"
# str3 = "Valdas"
# # str = str1 + str2 + str3
# my_list.append(str1)
# my_list.append(str2)
# my_list.append(str3)
# # print(*str, sep = "-")
# print(my_list)

# my_list = ["200", "400", "600"]
# my_list2 = ["rndr", "sol", "btc"]
# print("concatenated =", my_list + my_list2)


# my_list = ["200", "400", "600"]
# my_list2 = ["rndr", "sol", "btc"]
# my_list.extend(my_list2)
# print(my_list)
# print([str(my_list[i]) + my_list2[i] for i in range(len(my_list))])

# user_number = int(input("Eneter your number: "))
# user_number1 = int(input("Eneter your number: "))
# user_number2 = int(input("Eneter your number: "))
# print(max(user_number, user_number1, user_number2))

# user_name = input("Enter your name: ")
# user_surename = input("Enter your surename: ")
# user_age = int(input("Enter your age: "))
# age_cap = 21 
# if user_age >= age_cap:
#     print("Your're allowed to enter Casino")
# else:
#     print("You're not allowed to enter Casino")

# user_no_nr1 = int(input("Eneter your number: "))
# user_no_nr2 = int(input("Enter your number: "))
# if user_no_nr1 > user_no_nr2: 
#     print (max)
# elif user_no_nr2 > user_no_nr1:
#     print(max)
# else: user_no_nr1 == user_no_nr2
# print(user_no_nr1)

# user_no_nr1 = int(input("Eneter your number: "))
# user_no_nr2 = int(input("Enter your number: "))
# user_symbol = input("Enter your symbol: ")
# if user_symbol == "+":
#  print(user_no_nr1 + user_no_nr2)
# elif user_symbol == "*":
#  print(user_no_nr1 * user_no_nr2)
# elif user_symbol == "-":
#  print(user_no_nr1 - user_no_nr2)
# elif user_symbol == "/":
#  print(user_no_nr1 / user_no_nr2)

my_dictionary = {1:10}
user_guees = int(input("Enter your number: "))