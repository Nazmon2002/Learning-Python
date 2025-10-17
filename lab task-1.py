1.
print("Name: Nazmonnahar")
print("Department: Computer Science and Engineering")
print("University name: Green University of Bangladesh")
2.
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
sum=a+b
print("sum = ", sum)
3.
celsius = float(input("Enter temperature in celsius: "))
fahrenheit=(celsius * 9/5)+32
print("Temperature in fahrenheit : ",fahrenheit)
4.
height = float(input("Enter height of rectangle: "))
width = float(input("Enter width of rectangle: "))
rect_area = height * width
rect_perimeter = 2* (height + width)
print("\n rectangle -> Area : ",rect_area, "Perimeter: ",rect_perimeter)

import math
radius = float(input("\nEnter radius of circle: "))
circle_area= math.pi * radius**2
circle_perimeter = 2* math.pi *radius
print("Circle -> Area : ",circle_area, "Perimeter : ",circle_perimeter)

c = float(input("\nEnter side c of triangle : "))
d = float(input("Enter side d of triangle : "))
e = float(input("Enter side e of triangle : "))
if c + d > e and c + e > d and d + e > c:
    s = (c + d + e) / 2
    triangle_area = math.sqrt(s * (s - c) * (s - d) * (s - e))
    triangle_perimeter = a + b + c
    print("Triangle -> Area:", triangle_area, "Perimeter:", triangle_perimeter)
else:
    print("Invalid triangle sides! The sum of any two sides must be greater than the third.")


5.
p=float(input("Enter principal Amount: "))
r=float(input("Enter annual interest rate (%) : "))
n=float(input("Enter time in year: "))
simple_interest = (p*r*n) /100
Compound_interest = p * ((1+r/100) ** n)-p
print("Simple interest = ", simple_interest)
print("Compound interest = ", Compound_interest)

6.
ch=input("Enter a charater: ")
print("The ASCII value of",ch, "is", ord(ch))

7.
m = int(input("Enter first number: "))
p = int(input("Enter second number: "))
print("Before swapping: m =", m, "p =", p)

temp = m
m = p
p = temp

print("After swapping: m =", m, "p =", p)

8.
q = int(input("Enter first number: "))
r = int(input("Enter second number: "))
print("Before swapping: q =", q, "r =", r)

q, r = r, q

print("After swapping: q =", q, "r =", r)

9.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is Even ")
else:
    print(num, "is Odd ")


if num & 1 == 0:
    print(num, "is Even ")
else:
    print(num, "is Odd ")

10.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Maximum number is:", a)
elif b >= a and b >= c:
    print("Maximum number is:", b)
else:
    print("Maximum number is:", c)

11.
total_days = int(input("Enter total number of days: "))

years = total_days // 365
weeks = (total_days % 365) // 7
days = (total_days % 365) % 7

print("Years:", years)
print("Weeks:", weeks)
print("Days:", days)

12.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

minimum = a if a < b else b
print("Minimum number is:", minimum)

13.
num = int(input("Enter a number: "))
print("Original number:", num)

num = num + 1
print("After pre-increment:", num)

num2 = num
print("Value shown before post-increment (simulated):", num2)
num2 = num2 + 1
print("After post-increment (simulated):", num2)
