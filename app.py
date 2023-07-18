
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

print(numbers.count(1))

