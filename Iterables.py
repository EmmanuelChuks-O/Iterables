# Iterables = An object/collection that can return its elements one at a time,
#             allowing it to be iterated over a loop

numbers = [1, 2, 3, 4, 5]

for number in reversed(numbers):
    print(number, end=" ")
print()

fruits = {"apple", "orange", "banana", "coconut"}

for fruit in fruits:
    print(fruit, end=",")
print()

name = "Emmanuel Okoh"

for character in name:
    print(character, end="")

print()

my_dictionary = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}

for key in my_dictionary.keys():
    print(key, end="")
print()
for value in my_dictionary.values():
    print(value, end="")
print()

for key, value in my_dictionary.items():
    print(f"{key}: {value}")