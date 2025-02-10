"""
Questions:
1. Strings
Given the string s = "hello python", print:

1a.The first and last characters.
1b.The string in uppercase.
1c.The string in reverse order.
"""
s= "hello python" #Given string
# Solution 1a:

print(f"First character is {s[0]} and last character is {s[-1]}")

# Solution 1b:

print(s.upper())

# Solution 1c:

print(f"{s[::-1]}")

"""
2. Replace "bad" with "good" in the string:

2a.Print the modified sentence.
"""

sentence = "This is a bad example." #Given sentence
#  Solution 2a.

modified_sentence=sentence.replace("bad","good") #learned replace function which is use for replacing string 
print(modified_sentence)

"""
3.Check if the string "programming" contains the letter 'm'.

If it does, print "Found m!".
Otherwise, print "m not found."
"""
# Solution:
word= "programming"

if "m" in word :
    print("Found m!")
else:
   print("m not found.")


"""
2. Lists
Given the list numbers = [10, 20, 30, 40, 50], perform the following:

Print the second and fourth elements.
Append 60 to the list.
Remove 20 from the list.
Print the length of the list.
Given fruits = ["apple", "banana", "cherry", "date", "fig"], do the following:

Print the first three elements of the list.
Check if "banana" is in the list. If yes, print "Banana is available!".
Sort the list in reverse alphabetical order and print it.
"""
# Solution 2a.
numbers = [10, 20, 30, 40, 50]
print(numbers[1], numbers[3])


numbers.append(60)
print(numbers)

numbers.remove(20)
print(numbers)

print(len(numbers))

# Solution 2b.
fruits = ["apple", "banana", "cherry", "date", "fig"]

print(fruits[:3])

if "banana" in fruits:
    print("Banana is available!")

print(sorted(fruits,reverse=True))



"""
3.For Loops
Print all even numbers from 0 to 20 using a for loop.

Given a list of numbers digits = [3, 6, 9, 12, 15], use a for loop to multiply each number by 2 and print the result.

Given colors = ["red", "blue", "green", "yellow"], use a for loop to print each color in uppercase.

Use enumerate() to print both index and value of each element in cars = ["Toyota", "Honda", "Ford"].

"""
# Solution 3a.

for num in range(0,21,2):
    print(num)

# Solution 3b.
digits = [3, 6, 9, 12, 15]
for digit in digits:
    digit= digit*2
    print(digit)

# Solution 3c.
colors = ["red", "blue", "green", "yellow"]
for color in colors:
    print(color.upper())

# Solution 3d.
cars = ["Toyota", "Honda", "Ford"]
for index, car in enumerate(cars):
    print(index,car)