# First program to print
print(24 * 7)

# Example basic program to print hours in a week
day_hours = 24
week_days = 7
week_hours = day_hours * week_days
print(week_hours)

# Prints the data type
print(type(week_hours)) 

# List
stu_grades = list(range(1,9,2))
print(stu_grades)

grades = [9, 8, 7.9]
my_sum = sum(grades)
length = len(grades)
mean = my_sum/length
print(mean)

# Print max
max_value = max(grades)
print(max_value)

# Print count of a single element
print(grades.count(9.0))

# Convert to lowercase
username = "Python3"
print(username.lower())

# Dictionary
day_temperatures = {'morning': 5.1, 'noon': 6.1, 'evening': 10.2}
print(day_temperatures['evening'])  # accessing a dict element

# Tuples - immutable
grades = (9, 8, 7.9)
color_codes = ((1,2,3), (4,5,6), (7,8,9))
day_temperatures = {'morning': (1.1 , 2.2, 3.4), 'noon': (2.3, 4.5, 3.1), 'evening': (2.4, 3.5, 6.5)}

# List methods - append, remove, access list items
seconds = [1.2323442655, 1.4534345567, 1.023458894]
current = 1.10001399445
seconds.append(current)
seconds.remove(1.4534345567)
print(seconds[0])

# Slicing a list in a range of index
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[1:4])
print(letters[ :3])     # First 3 elements
print(letters[-3: ])    # Last 3 elements

# Sometimes you might need to convert between different data types in Python for one reason or another. That is very easy to do:

# From tuple to list:
data = (1, 2, 3)
print(list(data))

# From list to tuple:
data = [1, 2, 3]
print(tuple(data))

# From list to dictionary:
data = [["name", "John"], ["surname", "smith"]]
print(dict(data))

# Note that the original data type needs to have the data structured in a way that can be understood by the new data type. For example, the following would not work:
# data = [1, 2, 3]
# dict(data)
# TypeError: cannot convert dictionary update sequence element #0 to a sequence

# Create Functions

# Currency converter function
def convert(amount):
    output = amount * 1.75
    return output
 
print(convert(10))

# mean function
def mean(my_list):
    the_mean = sum(my_list)/len(my_list)
    return the_mean

print(mean([1, 4, 6]))

# Sq area function
def foo(a):
    return a * a

print(foo(5))

# Password controller function
def foo(password):
    if len(password) >= 8:
        return True
    else:
        return False

# Temperature check function
def foo(temperature):
    if temperature > 25:
        return "Hot"
    elif 25 >= temperature >= 15:
        return "Warm"
    else:
        return "Cold"

# Multiple conditions in a function
message = "hello there"
 
if "hello" in message:
    print("hi")
elif "hi" in message:
    print("hi")
elif "hey" in message:
    print("hi")
else:
    print("I don't understand")

# Check type
isinstance("abc", str)
isinstance([1, 2, 3], list)
type("abc") == str
type([1, 2, 3]) == list

# User Input

# ip = input("Enter a number: ")
# print(ip)

# experience_months = input("Enter your experience in months: ")
# experience_years = int(experience_months) / 12

# name = input("Name? ")
# surname = input("Surname? ")
# message1 = "Hello %s %s" % (name, surname)
# message2 = f"Hello {name}"

def foo(name):
    return f"Hi {name}"

def foo(name):
    return f"Hi {name.title()}"

def foo(name):
    return "Hi %s" % name

def foo(name):
    return "Hi %s" % name.title()

# String Formatting
name = "Sim"
experience_years = 1.5
print("Hi {}, you have {} years of experience".format(name, experience_years))

name = "John"
surname = "Smith"
message = "Your name is {}. Your surname is {}".format(name, surname)
print(message)

# For Loop
colors = [11, 34, 98, 43, 45, 54, 54]
for color in colors:
    print(color)

for color in colors:
    if isinstance(color, int):
        print(color)

# Looping through a dictionary - 1
day_temperatures = {'morning': 5.1, 'noon': 6.1, 'evening': 10.2}

for temp in day_temperatures.items():
    print(temp)

for temp in day_temperatures.values():
    print(temp)

# Looping through a dictionary - 2: Both below for loops gives same output
phone_numbers = {"John": "+37682929928", "Marry": "+423998200919"}
 
for pair in phone_numbers.items():
    print(f"{pair[0]} has as phone number {pair[1]}")

for key, value in phone_numbers.items():
    print(f"{key} has as phone number {value}")

# Looping through a dictionary - 3: Prints both keys and values
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for key, value in phone_numbers.items():
    print(f"{key}: {value}")

# Replaces + with 00 in phone numbers
for value in phone_numbers.values():
    print(value.replace("+", "00"))

# String formatting with for looping a dictionary
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))

# While Loop
a = 0
while a < 5:
    a = a + 1
    print(a)

a = 0
while True:
    a = a + 1
    print(a)
    if a >= 4:
        break
    else:
        continue

# Build a first program - section 8
def sentence_maker(phrase):
    interrogatives = ("how", "what", "why")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

print(sentence_maker("how are you"))

results = []
# while True:
#     user_input = input("Say something: ")
#     if user_input == "\end":
#        break
#    else:
#       results.append(sentence_maker(user_input))

# print(results)  # prints as a list
# print(" ".join(results))    # prints as a sentence

# List comprehensions - section 9
def foo(lst):
    return [i for i in lst if  isinstance(i, int)]

def foo(lst):
    return [i for i in lst if i > 0 ]

def foo(lst):
    return [i if not isinstance(i, str) else 0 for i in lst ]

def foo(lst):
    return sum([float(i) for i in lst])

# A list comprehension is an expression that creates a list by iterating over another container.

# A basic list comprehension:
#  [i*2 for i in [1, 5, 10]]
#  Output: [2, 10, 20]

# List comprehension with if condition:
# [i*2 for i in [1, -2, 10] if i>0]
# Output: [2, 20]

# List comprehension with an if and else condition:
# [i*2 if i>0 else 0 for i in [1, -2, 10]]
# Output: [2, 0, 20]

# More about Functions - section 10

# Function to concatenate two strings
def foo(s1, s2):
    return s1 + s2

# Function to return mean which takes indefenite number of numbers as arguments
def foo(*args):
    return sum(args) / len(args)

# Function which takes indefenite number of strings as arguments
def foo(*args):
    args = [x.upper() for x in args]
    return sorted(args)

# Function which takes indefenite number of keyword arguments
def find_sum(**kwargs):
    return sum(kwargs.values())
print(find_sum(x=1, y=2, z=6))

# Functions can have default parameters (e.g. coefficient):
def converter(feet, coefficient = 3.2808):
    meters = feet / coefficient
    return meters
print(converter(10))
# Output: 3.0480370641306997

# Arguments can be passed as non-keyword (positional) arguments (e.g. a) or keyword arguments (e.g. b=2 and c=10):
def volume(a, b, c):
    return a * b * c
print(volume(1, b=2, c=10))

# An *args parameter allows the  function to be called with an arbitrary number of non-keyword arguments:
def find_max(*args):
    return max(args)
print(find_max(3, 99, 1001, 2, 8))
# Output: 1001

# An **kwargs parameter allows the function to be called with an arbitrary number of keyword arguments:
def find_winner(**kwargs):
    return max(kwargs, key = kwargs.get)
print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34))
# Output: Sim

# File Processing - section 11
myfile = open("fruits.txt")
print(myfile)
myfile.close()

with open("fruits.txt") as myfile:
    content = myfile
print(content)

# Read the bear.txt and print out the first 90 characters of it's content
file = open("files/bear.txt")
content = file.read()
file.close()
print(content[:90])

# Write to a file
with open("files/vegetables.txt", "w") as myfile:
    myfile.write("Tomato")

# Function that gets a single char and a filepath as arguments and returns the no: of occurences of that char in the file
def foo(character, filepath="files/bear.txt"):
    file = open(filepath)
    content = file.read()
    return content.count(character)

# Read and append
with open("files/bear.txt") as file:
    content = file.read()
with open("files/bear2.txt", "a") as file:
    file.write(content)

# Append and read a file - Copy the contents N times
with open("files/data.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    file.seek(0)
    file.write(content)
    file.write(content)

# Modules - section 12
import os
import time
import pandas

# while True:
#     if os.path.exists("files/vegetables.txt"):
#         with open("files/vegetables.txt") as file:
#             print(file.read())
#     else:
#         print("file does not exist")
#     time.sleep(5)

a = 0
while a<4:
    a = a+1
    if os.path.exists("files/temps_today.csv"):
        data = pandas.read_csv("files/temps_today.csv")
        print(data.mean())
        print(data.mean()["st1"])   # gives the mean of only st1 column
    else:
        print("file does not exist")
    time.sleep(5)

# Modules - section 16 - Exception handling
def divide(a,b):
    try:
        return a/b
    except:
        return "Zero division is meaningless"

print(divide(1,0))





    




