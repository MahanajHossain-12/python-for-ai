name = "alice"

age = 30

string = "Taka lagbe prochur"

first_name = "Alice"
last_name = "Smith"

full_name = first_name + " " + last_name

long_dash = "-" * 10
print(full_name)
print(long_dash)

len(full_name)


is_true = True
age = 16

can_vote = age >= 18

age = 25
has_license = True

# AND both must be True
can_drive = age >= 18 and has_license
print(can_drive)

age = 25
have_license = True
Drunk = False

can_drive = age > 18 and have_license and not Drunk

# String Manipulation

Name = "Udoy Mido"
string = f"My name is {Name}!"  # f string = "My name is {}!".format(Name) #format

Name = "Sanjo Rashomo"
Name.title()  # Sanjo Rashomo
Name.upper()  # SANJO RASHOMO
Name.lower()  # sanjo rashomo

temparature = 31

if temparature > 30:
    print("Its very hotttt!")
elif temparature > 25 and temparature <= 30:
    print("Its hott!")
else:
    print("Its good weather!")

# nested if else
age = 28
has_ticket = True

if has_ticket:
    if age > 18:
        print("You can enter the hall!")
    else:
        print("You are not allowed to enter the hall!")
else:
    print("Please buy  tickets!")


# LOOPS
for i in range(6):
    print(i)

for x in range(5):
    print("Midoriya")

for c in range(1, 11):
    print(c)

for v in range(0, 11, 2):  # range(start, stop, step) #step is the increment value
    print(v)


###################################### Data Structures ################################################

list1 = ["Udoy", "Mido", "Sanjo", "Rashomo", 12, 67, True, False]
list1.append("New")  # append adds an element to the end of the list.
list1.remove(
    "Sanjo"
)  # remove removes the first occurrence of a specific element from the list.
list1.insert(
    2, "Inserted"
)  # insert adds an element at a specific index, shifting the rest of the elements to the right.
list1.pop(
    3
)  # pop removes the last element by default, but you can specify an index to remove a specific element.
list1.sort(
    key=str
)  # sort sorts the list in ascending order. The key parameter allows you to specify a function to be called on each list element before making comparisons. In this case, str is used to convert all elements to strings for comparison.
print(list1)
list1.reverse()  # reverse reverses the order of the elements in the list.
list1.clear()  # clear removes all elements from the list, leaving it empty.
list1.extend(
    ["New1", "New2"]
)  # extend adds all elements from an iterable (like another list) to the end of the list.
list1.count(
    "New1"
)  # count returns the number of occurrences of a specific element in the list.
list1.index(
    "New1"
)  # index returns the index of the first occurrence of a specific element in the list. If the element is not found, it raises a ValueError.
print(list1)

# Dictionary

person_1 = {"name": "Udoy", "gender": "Male", "City": "Dhaka", "Kamla": "PNM"}
person_1["age"] = 25  # Adding a new key-value pair to the dictionary


# set
my_set = {1, 2, 3, 4, 5}
my_set.add(6)  # Adding an element to the set
print(my_set)

my_set.remove(3)  # Removing an element from the set
print(my_set)
my_set.discard(
    10
)  # Discarding an element from the set (does not raise an error if the element is not found)

# checking if an element is in the set
if 4 in my_set:
    print("4 is in the set")


def welcoming():
    print("Hello, welcome to the program!")
    pass  # Placeholder for future code


welcoming()  # Calling the function to execute it


def greet(name):
    print(f"Hello, {name}! Welcome to the program!")
    pass  # Placeholder for future code


greet("Alice")  # Calling the function with an argument
greet("Bob")  # Calling the function with another argument
greet("Charlie")  # Calling the function with yet another argument


def greet_user(name, age):
    print(f"Hello, {name}! You are {age} years old.")
    pass  # Placeholder for future code


greet_user("Alice", 25)  # Calling the function with two arguments
greet_user("Bob", 30)  # Calling the function with two arguments
greet_user("Charlie", 35)  # Calling the function with two arguments


def calculate_total(price, tax_rate, discount):
    total = price + (price * tax_rate) - discount
    print(f"Calculated total: {total}")
    return total  # Returning the calculated total to the caller


# Example usage of the calculate_total function
Total_1 = calculate_total(
    100, 0.1, 5
)  # Calling the function with price, tax_rate, and discount
Total_2 = calculate_total(
    200, 0.15, 10
)  # Calling the function with different arguments
Total = Total_1 + Total_2  # Summing the totals from both function calls
print(f"Total from both calculations: {Total}")  # Printing the final total


def add_return(a, b):
    return a + b  # Returning the sum of a and b to the caller


result = add_return(5, 10)  # Calling the function and storing the returned value
print(f"The result of add_return is: {result}")  # Printing the result


def calculate_area(LENGTH, WIDTH):
    AREA = LENGTH * WIDTH
    return AREA  # Returning the calculated area to the caller


result_area = calculate_area(12, 10)  # Calling the function with length and width
print(f"The area is: {result_area}")  # Printing the calculated area


def double_value(x):
    return x * 2  # Returning double the value of x to the caller


result_double = double_value(
    5
)  # Calling the function with an argument, output will be 10

total_double = result_double + 10  # Adding 10 to the returned value, output will be 20

if double_value(3) > 5:  # Calling the function within an if statement
    print(
        f"The doubled value is greater than 5: {double_value(3)}"
    )  # This will not print since double_value(3) is 6


def min_max():
    numbers = [3, 5, 1, 8, 2]
    minimum = min(numbers)  # Finding the minimum value in the list
    maximum = max(numbers)  # Finding the maximum value in the list
    return minimum, maximum  # Returning both minimum and maximum values as a tuple


min_val, max_val = min_max()  # Calling the function and unpacking both returned values
print(
    f"Minimum value: {min_val}, Maximum value: {max_val}"
)  # Printing the minimum and maximum values


# Importing the entire math module and specific functions/constants from it

import math  # Importing the math module to access mathematical functions and constants
from math import (
    sqrt,
    pi,
)  # Importing specific functions (sqrt) and constants (pi) from the math module

square_root = sqrt(16)  # Using the sqrt function to calculate the square root of 16

import datetime  # Importing the datetime module to work with dates and times

current_date = datetime.datetime.now()  # Getting the current date and time
print(f"Current date and time: {current_date}")  # Printing the current date and time

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
}  # Creating a dictionary with sample data
df = pd.DataFrame(data)  # Creating a DataFrame from the dictionary
print(df)  # Printing the DataFrame to the console


import requests  # Importing the requests module to make HTTP requests

# We need coordinates to get weather data
latitude = 48.85  # Paris latitude
longitude = 2.35  # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(
    url
)  # Making a GET request to the specified URL to retrieve weather data
data = (
    response.json()
)  # Parsing the JSON response from the API into a Python dictionary

temperature = data["current"][
    "temperature_2m"
]  # Extracting the current temperature from the parsed data
print(f"The current temperature in Paris is: {temperature}°C")  # Printing the current


import requests


def get_weather(latitude, longitude):
    response = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m"
    )
    data = response.json()
    return data["current"]["temperature_2m"]


# Get temperature for different cities
paris_temp = get_weather(48.85, 2.35)
london_temp = get_weather(51.50, -0.12)
tokyo_temp = get_weather(35.68, 139.69)

print(f"Paris: {paris_temp}°C")
print(f"London: {london_temp}°C")
print(f"Tokyo: {tokyo_temp}°C")
