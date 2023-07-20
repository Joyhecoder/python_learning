import math
#? declare a variable 
age = 20
price = 19.95
first_name = "Joy"
is_online = True
# print(age)

#? input
# name = input("what is your name? >>")
# print("Hello, " + name)

# birth_year = input("Enter your birth year: ")
# birth_year_int = int(birth_year)
# age = 2023 - birth_year_int
# print(age)

#? converting 
int()
float()
bool()
str()

#? first_num = input("enter a number: ")
# second_num = input("enter a second number: ")
# sum = float(first_num) + float(second_num)
# print(f"{first_num} plus {second_num} is {sum}")

#? object methods
# course = 'Python for Beginners'
# print(course.upper())
# print(course.lower())
# print(course.find('for')) #7
# print(course.find('Y')) #-1
# print(course.replace('for', '4'))
# #! check if an element is in an object
# print('Python' in course)
# print(course)

#? math operators
# print(10 % 3)
# print(10 ** 3)

# x = 10
# x = x + 3  #x += 3

# x = 10 + 3 * 2 #16, it follows the math rules
# y = (10 + 3) * 2 #26

# print( 10 // 3) #3, rounding

#? comparison operators
# x = 3 > 2 #True
# x = 3 == 2 #False
# x = 3 != 2 #True
# print(x)

#? logical operators
price = 25
# print(price > 10 and price < 30) #True
# print(price > 10 and price < 25) #False
# print(price > 10 or price < 25) #True
# print(not price > 10 ) #False

#? if statement
# temperature = 25
# if temperature > 30:
#     print(f'Weather is hot, current temperature is {temperature}')
# elif temperature > 20:
#     print(f"it's a good day, temperature is {temperature}")
# else:
#     print(f"it's an ok day, current temperature is {temperature}")

#! exercise:
# weight = float(input("enter your weight in number: "))
# unit = input("Please enter k for kilogram or l for pounds").upper()
# if unit == "K":
#     print(f"your weight pounds is {round(weight * 2.2, 2)}")
# else:
#     print(f"your weight in kg is {round(weight / 2.2, 2)}")

#? while loop
# i = 1
# while i <= 5:
#     print(i * '*')
#     i += 1


#? List
names = ["Julie", "John", "Bob", "Mosh", "Mary"]
# print(names[-2])
#!change an element in list
names[0] = "Juliet"
# print(names)
#!slice method in python
# print(names[0:3])

#? List methods
# numbers = [1, 2, 3, 4, 5]
# print(10 in numbers)
# numbers.append(6)

# numbers.insert(1, 9)

# numbers.remove(3)
# numbers.remove(9)

# print(len(numbers))

# numbers.clear()
# print(numbers)

#? for loops
# for num in numbers:
#     print(num)

# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i += 1

#? range
numbers = range(5, 10, 2)
# for num in numbers:
#     print(num)

#? tuple: it is like a list but it is not mutable 
numbers = (1, 1, 2, 3)

# print(numbers.count(1))


#? string
course = '''
Hi John,

Here is our first email to you.

Thank you,
Josh
'''
# print(course)

#? a copy of the course
another = course[:]
# print(another)


#? formatted string
first = "John"
last = "Smith"
message = f"{first} [{last}] is a coder"
# print(message)


#? string method
course = 'Python for Beginners'
# print(len(course))
# print(course.upper(), course.lower())
# print(course.find(' '))
# print(course.replace('Beginners', 'Absolute Beginners'))
# print("python" in course)

#? Math functions
x = 2.9
# print(round(x))
# print(abs(-2.9))
# print(math.ceil(2.9))
# print(math.floor(2.9))


#! exercise
# house_price = 1000000
# credit = 'ok'
# if credit == 'good':
#     print(type(house_price))
#     price = house_price / 10
#     print(f'you need to put down ${price}')
# else:
#     price = house_price/5
#     print(f'You need to put down ${price}')

#? conditions
# has_high_income = False
# has_good_credit = True
# if has_high_income or has_good_credit:
#     print("Eligible for loan")

#? comparison
# name = "Jo"
# if len(name) < 3:
#     print("name must be at least 3 characters")
# elif len(name) > 50:
#     print("name is too long")
# else:
#     print("Name looks good!")

#? while loops
# secret_number = 9
# i = 0
# while i < 3:
#     guess = int(input("guess your number >> "))
#     i += 1
#     if guess == secret_number:
#         print("you got the secret number!")
#         break
    
# else:
#     print("you failed")

#! exercise
# user_response = ""
# last_response = ""
# while True:
#     print("Please enter your choice: start, stop or quit")
#     user_response = input("> ").lower()
#     if user_response == 'start':
#         if last_response == user_response:
#             print("car has already started!")
#         else:
#             print("Car started... Ready to go!")
#         last_response = user_response
#     elif user_response == 'stop':
#         if last_response == user_response:
#             print("car has stopped!")
#         else:
#             print('car stopped.')
#         last_response = user_response
#     elif user_response == 'quit':
#         break
#     else:
#         print("I don't understand that..")
    
    
#? for loops
# for item in 'Python':
#     print(item)
# for item in ['Mosh', "joshn", 'Sarah']:
#     print(item)
# for item in range(0,100):
#     print(item)

#! exercise:
# prices = [10, 20, 40]
# sum = 0
# for price in prices:
#     sum += price
# print(f"your cart has ${sum} worth of items")

#? nested loops
# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')

#! exercise:
# numbers = [5, 2, 5, 2, 2]
# # for x in numbers:
# #     y = 'x' * x
# #     print(y)

# for x in numbers:
#     x_in_each_row = ""
#     for y in range(x):
#         x_in_each_row += "x"
#     print(x_in_each_row)

#! exercise to find the largest num in a list
# num_list = [ 2, 4, 1, 5, 34, 0, 2]
# large_num = num_list[0]
# for num in num_list:
#     if num > large_num:
#         large_num = num
# print(f"the largest number in the list is {large_num}")

#? 2D list
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for row in matrix:
#     for item in row:
#         print(item)

#? list methods
# numbers = [5, 3, 4, 6, 4]
# numbers2 = numbers.copy()
# numbers.append(10)
# numbers.insert(2, 99)
# numbers.remove(5)
# numbers.pop()
# print(numbers.index(99))
# print(5 in numbers)
# print(numbers.count(4))
# numbers.sort()
# numbers.reverse()
# print(numbers)
# print(numbers2)

#! remove duplicates in a list
duplicated_list = [1, 1, 2, 3, 4, 5, 5, 3]
duplicated_list.sort()
last_num = duplicated_list[-1] + 1
for num in duplicated_list:
    if num == last_num:
        duplicated_list.remove(num)
    else:
        last_num = num
print(duplicated_list)