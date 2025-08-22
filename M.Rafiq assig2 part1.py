#part1
#1
chek_num=float(input("Enter Value:"))
if chek_num < 0 :
    print("negative")
elif chek_num >0:
    print ("positive")
elif chek_num ==0:
    print ("zero")
#2
a=int(input("Enter Number 1:"))
b=int(input("Enter Number 2:"))     
if a> b:
      print("num1 is greater")
elif b> a :
      print("num2 is greater")
elif b==a:
    print("both are equal")
#3
a=int(input("Enter Number 1:"))
b=int(input("Enter Number 2:"))
c=int(input("Enter Number 3:"))
if a> c > b:
    print("num1 is greater")
if b> a > c:
      print("num2 is greater")
if c> b > a:
    print ("num3 is greater")
if a> b > c:
    print("num1 is greater")
if b> c > a:
      print("num2 is greater")
if c> a > b:
    print ("num3 is greater")      
elif b==a==c:
    print("all are equal")
else :
    print ("ERROR")
#4
Institute=("Saylani Mass IT Institute,666 mass it institute")
print ("chk str Mass")
institute=str(input( "chk_string"))
if institute in Institute :
    print ("string found")
if institute not in Institute :
    print ("string not found")
#5
age=int(input("enter age"))
if age< 18 :
     print ("minor")
elif age >18 <60 :
    print ("adult")
elif age >60 :
    print ("senior citizen")
#6
num =int(input("enter num"))
if num%2==0:
   print ("number is even")
else:
   print ("number is odd")
#7
value_1=int(input("Enter value 1"))
value_2=int(input("Enter value 2"))
operator=(input("Enter operators (/,x,+,-)"))
if operator is '/' :
    print (f"{value_1}/{value_2}=",value_1/value_2)
elif operator is ("x"):
    print (f"{value_1} x {value_2} = ",value_1*value_2)
elif operator is("+"):
    print(f"{value_1} x {value_2} = ",value_1+value_2)
elif operator is ("-]"):
    print(f"{value_1} x {value_2} = ",value_1-value_2)
else:
    print ("error")

#8
    # Take input
num = int(input("Enter a number: "))

# Check range
if 20 <= num < 40:
    print("The number lies in the range 20 to 40.")
else:
    print("The number is outside the range.")
#9
    # Take input
num = int(input("Enter an integer: "))

# Check divisibility
if num % 2 == 0 and num % 3 == 0:
    print("The number is divisible by both 2 and 3.")
elif num % 2 == 0:
    print("The number is divisible by 2 only.")
elif num % 3 == 0:
    print("The number is divisible by 3 only.")
else:
    print("The number is not divisible by 2 or 3.")

#10
    # Take input
score = int(input("Enter your score: "))

# Check pass/fail
if score > 60:
    print("Pass")
else:
    print("Fail")
#11
    # Take input
num = int(input("Enter a number: "))

# Check for prime
if num > 1:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("The number is prime.")
    else:
        print("The number is not prime.")
else:
    print("The number is not prime.")

#12
    # Take input
temp = float(input("Enter temperature in Celsius: "))

# Classify temperature
if temp < 0:
    print("Freezing temperature.")
elif 0 < temp < 26:
    print("Moderate temperature.")
else:
    print("Hot temperature.")

   
