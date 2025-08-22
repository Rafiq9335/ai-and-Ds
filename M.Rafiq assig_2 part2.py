#1
for i in range(1, 31):
    print(i)
#2
num = 2
while num <= 50:
    print(num)
    num += 2
#3
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
#4
num = 1
while num <= 50:
    print(num)
    num += 2
#5
total = 0
for i in range(1, 51):
    total += i
print("Sum of numbers from 1 to 50 is:", total)
#5
total = 0
for i in range(1, 51):
    total += i
print("Sum of numbers from 1 to 50 is:", total)
#6
text = input("Enter a string: ")
for char in text:
    print(char)
#7
num = int(input("Enter a number: "))
factorial = 1
n = 1
while n <= num:
    factorial *= n
    n += 1
print(f"Factorial of {num} is: {factorial}")
#8
for i in range(10, 0, -1):
    print(i)
#9
correct_password = "python123"
while True:
    password = input("Enter password: ")
    if password == correct_password:
        print("Access granted!")
        break
    else:
        print("Wrong password. Try again.")
#10
for i in range(1, 11):
    print(f"Square of {i} is {i * i}")
#11
even_sum = 0
odd_sum = 0

for i in range(1, 51):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
# bonus challenge
a, b = 0, 1
for i in range(10):
    print(a)
    a, b = b, a + b

