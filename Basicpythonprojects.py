#Area  of Rectangle

side=float(input("enter side of rectanle: "))
Area=(side*side)
print(f"area of rectangle is: {Area}")

#------------------------------------------------------------------------------------------------------
item=int(input("enter number of items: "))
price=float(input("enter price of items: "))
quantity=int(input("enter the quantity: "))
total=quantity*price
print(f"your total amount to pay is :Rs {total:.2f}")

#------------------------------------------------------------------------------------------------------

#some maths function

import math
x=3.14
result=math.sqrt(x)
print(result)
result=abs(x)
print(result)

#-------------------------------------------------------------------------------------------------------

# # # circumference of circle  

import math
radius=float(input("enter the radius: "))
pie=math.pi
circumference=2*pie*radius
print(circumference)
 
#-------------------------------------------------------------------------------------------------------

# # # Area of circle

radius=float(input("enter the radius: "))
area=math.pi*radius*radius
print(f"Area of circle is: {area}cm")

#--------------------------------------------------------------------------------------------------------


# #  Hypotenuse of a right-angled triangle

import math
a=float(input("enter number 1: "))
b=float(input("enter number 2: "))
c=math.sqrt(pow(a,2)+pow(b,2))
print(f"hypotenuse of triangle  : {c}cm")

#----------------------------------------------------------------------------------------------------------

### Simple Calculator 

operator=input("enter the operator '+','-','*','/': ")
num1=float(input("enter number 1: "))
num2=float(input("enter number 1: "))
if operator=="+":
    print(round(num1+num2,3))
elif operator=="-":
    print(round(num1-num2,3))   
elif operator=="*":
    print(round(num1*num2,3))
if operator=="/":
    if(num2==0):
        print("this divison is invalid")
    else :
         print(round(num1/num2,3))
    
else :
    print("unauthorized operator" )      

#----------------------------------------------------------------------------------------------------------

# # convert weight from kg to lbs or viseversa

weight=float(input("enter your weights : "))
unit=input("enter unit to be in k or l:  ")
if unit=="k":
    weight=weight*2.205
    print(f"weight in lbs ={round(weight,1)} lbs")
elif unit=="l":
    weight=weight/2.205
    print(f"weights in kg={round(weight,1)} kgs")   
else:
    print(f"{unit} is invalid")    

#----------------------------------------------------------------------------------------------------------


# # validate user input not more then 12 words,no digits allowed,only one  spaces allowed

name=input("enter your name: ")
space_count=name.count(" ")
if len(name)>12:
    print("name length is greater then validation")
elif space_count!=1:
    print("only one  space allowed in name at all")
elif not all(char.isalpha() or char==" " for char in name):
    print("no digit is allowed in name or special characters")
else :
    print(f" hello {name}") 

#----------------------------------------------------------------------------------------------------------

  
# simple interest

principle=0
rate=0
time=0
while True:
    principle=float(input("enter the principle amount: "))
    if principle<0:
        print("invalid value provided")
    else:
        break  
while True:
    rate=float(input("enter the  rate: "))
    if rate<0:
        print("invalid value provided")
    else:
        break    
while True:
    time=float(input("enter the  time: "))
    if time<0:
        print("invalid value provided")
    else:
        break    

total=principle*rate*time/100
print(f"total amount after {time} years is: {total} Rs")    

#--------------------------------------------------------------------------------------------------------

## Countdown program

import time 
counting = int(input("Enter the number of seconds for countdown: "))
for x in reversed(range(0,counting)):
    second=x % 60
    minutes=int(x//60)%60
    hours=int(x/3600)
    print(f"{hours:02}:{minutes:02}:{second:02}")
    time.sleep(1)
print("times up")

#--------------------------------------------------------------------------------------------------------

#nested loops

rows=int(input("enter rows: "))
columns=int(input("enter columns: "))
symbol=input("enter the symbol you wanted to print: ")
for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()

##----------------------------------------------------------------------------------------------------------

#shopping cart program

foods=[]
prices=[]
total=0
while True:
    food=input("enter what you wanted to buy: ")
    
    if food.lower()=="q":
        break
    else:
        price=float(input("enter the price of food: "))
        foods.append(food)
        prices.append(price)
print("-------list of items------")
for food in foods:
    print(food,end=" ")
for price in prices :
    total +=price    
print()
print(f"your total amount will be {total} Rs")    

##---------------------------------------END----------------------------------------------------------