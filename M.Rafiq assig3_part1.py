#part1 Functions
# 1
def Greetings(User_Name):
    print("Greetings")
    
print("Welcome to SMIT training center, Ahsan ")


#2
def argue(num):
 if num>0:
       return "Positive"
 elif num<0:
       return "Negative"
 else :
       return "zero"
        
#3
def func (val_1,val_2):
 if val_1>val_2:
    return "value 1 is greater"
 elif val_2>val_1:
    return "value 2 is greater"
 else :
    return "both are equal"
#4
def larger_num (a,b,c):
 if a> c > b:
    return"num1 is greater"
 if b> a > c:
    return"num2 is greater"
 if c> b > a:
    return "num3 is greater"
 if a> b > c:
    return"num1 is greater"
 if b> c > a:
    return"num2 is greater"
 if c> a > b:
    return "num3 is greater"      
 elif b==a==c:
    return"all are equal"
   
#5
def age_chk(age):
 if age< 18 :
     return"minor"
 elif age >18 <60 :
    return "adult"
 elif age >60 :
    return"senior citizen"
    
    
#6
def num_chk (num):
 if num%2==0:
  print ("it is even")
 elif num%2!=0:
  print("it is odd")
#7
def num_sqr(num):
    return "num*num"
#8
def circumfrence_area (r):
  totalarea= 2* 3.14
  print (f"The total circumfrence area is {totalarea}")
  r=(int (input ("Radius is: ")))

  circumfrence_area(r)
#9
def fun (Userscore):
    if Userscore > 60 :
        return "pass"
    else:
        return "fails"
#10
def is_prime(num):
    if num <= 1:
        return False  
    for i in range(2, int(num ** 0.5) + 1):  
        if num % i == 0:
            return False
    return True
#11
def factorial(n):
    if n == 0 or n == 1:  # base case
        return 1
    return n * factorial(n - 1)
