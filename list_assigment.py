# -*- coding: utf-8 -*-
"""list_assigment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rN1Rd2AlG5Vw28DAmnRVpXmAcBMgwhjE

Question 1: Basic List Operations

a) Create a list named `fruits` containing the following items: "apple", "banana", "orange", "grape", "kiwi".

b) Add "pear" to the end of the list.

c) Insert "mango" at the second position in the list.

d) Remove "orange" from the list.
"""

# a) Create a list named fruits containing the following items: "apple", "banana", "orange", "grape", "kiwi"
fruits = ['apple','banana','orange','grape','kiwi']

print(fruits)

# b) Add "pear" to the end of the list

fruits = ['apple','banana','orange','grape','kiwi']

fruits.append('pear')

print(fruits)

# c) Insert "mango" at the second position in the list

fruits = ['apple','banana','orange','grape','kiwi']

fruits.insert(3,'mango')

print(fruits)

# d) Remove "orange" from the list.

fruits = ['apple','banana','orange','grape','kiwi']

fruits.remove('orange')

print(fruits)

"""Question 2: Slicing and Indexing

a) Create a list named `numbers` containing the integers from 0 to 9.

b) Print the element at index 3.

c) Print a sublist containing the elements from index 2 to 6 (inclusive).

d) Print the last three elements using negative indexing.

"""

numbers=(list(range(0,10)))

print(numbers)

numbers=(list(range(0,10)))

print(numbers[3])

numbers=(list(range(0,10)))

print(numbers[2:6])

numbers=(list(range(0,10)))

print(numbers[-4:-1])

"""a) Create a list named `squares` using a list comprehension that contains the squares of numbers from 1 to 10.

b) Create a new list named `even_squares` using a list comprehension that contains the squares of even numbers from the `squares` list.


"""

square = [x**2 for x in range (1,10)]

print(square)

even_square = [x**2 for x in square if x % 2 == 0]

print(even_square)

"""Question 4: List Manipulation

a) Create a list named `colors` containing the following items: "red", "green",
   "blue", "yellow", "purple".

b) Swap the first and last elements of the list.
c) Reverse the order of the list.
d) Remove the second and third elements from the list.

"""

colors = ["red", "green", "blue", "yellow", "purple"]

# Swapping the first and last elements

colors[0], colors[-1] = colors[-1], colors[0]

print(colors)

colors = ["red", "green", "blue", "yellow", "purple"]

colors.reverse()

print(colors)

colors = ["red", "green", "blue", "yellow", "purple"]

del colors[3:5]

print(colors)

"""Question 5: Advanced Slicing

a) Create a list named `letters` containing the letters from 'a' to 'j'.

b) Using slicing, create a new list `first_half` containing the first half of the `letters` list.

c) Using slicing, create a new list `last_three` containing the last three elements of the `letters` list.

"""

letters = ['a','b','c','d','e','f','g','h','i','j']

print(letters)

letters = ['a','b','c','d','e','f','g','h','i','j']

first_half = (letters[0:5])

print(first_half)

letters = ['a','b','c','d','e','f','g','h','i','j']

last_three = (letters[-3:])

print(last_three)

"""Question 6: Nested Lists

a) Create a nested list named `matrix` with the following rows:
   - [1, 2, 3]
   - [4, 5, 6]
   - [7, 8, 9]

b) Print the element in the second row and third column.

c) Use nested indexing to change the value at the second row and first column to 0.

"""

list = [1, 2, 3],[4, 5, 6],[7, 8, 9]


print(list[0])
print(list[1])
print(list[2])

list = [1, 2, 3],[4, 5, 6],[7, 8, 9]

list[1][0]=(0)

print(list[0])
print(list[1])
print(list[2])