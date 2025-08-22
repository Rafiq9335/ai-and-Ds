#1
student = ["Tahir", 44, "AI and Data Science", True]

print("Task 1: Display student data")
for item in student:
    print(item)

#2
strings = []
numbers = []
booleans = []

for item in student:
    if isinstance(item, str):
        strings.append(item)
    elif isinstance(item, bool):
        booleans.append(item)
    elif isinstance(item, (int, float)):
        numbers.append(item)

print("\nTask 2: Separate data types")
print("Strings:", strings)
print("Numbers:", numbers)
print("Booleans:", booleans)
#3
fruits = ["apple", "raspberry", "pineapple", "cherry"]

print("\nTask 3: Fruit list operations")

# a) Check if 'apple' exists and get index
if "apple" in fruits:
    print("'apple' found at index:", fruits.index("apple"))

# b) Replace raspberry and pineapple with orange
fruits[1:3] = ["orange"]

# c) Insert 'apricot' at index 2
fruits.insert(2, "apricot")

# d) Extend with ["car", "bike", "aeroplane"]
fruits.extend(["car", "bike", "aeroplane"])

print("Updated fruits list:", fruits)

#4
scores_list = [40, 89, 90, 89, 23, 90, 50]

unique_scores = list(set(scores_list))  # Remove duplicates
unique_scores.sort(reverse=True)        # Sort in descending order

first_best = unique_scores[0]
second_best = unique_scores[1]

print("\nTask 4: Best scores")
print("First best score:", first_best)
print("Second best score:", second_best)

#5
numbers = [32, 54, 66, 11, 77, 10, 90]

# a) Remove items < 20
numbers = [num for num in numbers if num >= 20]

# b) Sort ascending and descending
asc = sorted(numbers)
desc = sorted(numbers, reverse=True)


average = sum(numbers) / len(numbers)

print("\nTask 5: Number list operations")
print("Filtered list (>=20):", numbers)
print("Ascending order:", asc)
print("Descending order:", desc)
print("Average value:", average)
#6
gadgets = ["Mobile", "Laptop", 10.0, "Marker", 3, 10, "Speakers", "Camera", 310.25]

strings = []
numbers = []

for item in gadgets:
    if isinstance(item, str):
        strings.append(item)
    elif isinstance(item, (int, float)):
        numbers.append(item)

strings_asc = sorted(strings)
strings_desc = sorted(strings, reverse=True)
strings_by_length = sorted(strings, key=len)

numbers_asc = sorted(numbers)
numbers_desc = sorted(numbers, reverse=True)

print("\nTask 6: Gadgets list operations")
print("Strings:", strings)
print("Numbers:", numbers)
print("Strings Ascending:", strings_asc)
print("Strings Descending:", strings_desc)
print("Strings by Length:", strings_by_length)
print("Numbers Ascending:", numbers_asc)
print("Numbers Descending:", numbers_desc)
