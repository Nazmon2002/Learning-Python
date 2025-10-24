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

<<<<<<< HEAD
9.
=======
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

14.
num = float(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Neutral (Zero)")

15.
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")

16.
marks = float(input("Enter your marks (0–100): "))

if marks >= 80:
    grade = "A+"
    cgpa = 4.00
elif marks >= 75:
    grade = "A"
    cgpa = 3.75
elif marks >= 70:
    grade = "A-"
    cgpa = 3.50
elif marks >= 65:
    grade = "B+"
    cgpa = 3.25
elif marks >= 60:
    grade = "B"
    cgpa = 3.00
elif marks >= 55:
    grade = "B-"
    cgpa = 2.75
elif marks >= 50:
    grade = "C+"
    cgpa = 2.50
elif marks >= 45:
    grade = "C"
    cgpa = 2.25
elif marks >= 40:
    grade = "D"
    cgpa = 2.00
else:
    grade = "F"
    cgpa = 0.00

print("Your Grade is:", grade)
print("Your CGPA is:", cgpa)

17.
ch = input("Enter a single character: ")

if ch.isalpha():
    if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
        print("Vowel")
    else:
        print("Consonant")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Symbol")

18.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

match op:
    case '+':
        print("Result:", num1 + num2)
    case '-':
        print("Result:", num1 - num2)
    case '*':
        print("Result:", num1 * num2)
    case '/':
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Division by zero not allowed")
    case _:
        print("Invalid operator")

19.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print(a, "is the greatest")
elif b >= a and b >= c:
    print(b, "is the greatest")
else:
    print(c, "is the greatest")

20.
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        print("Program ended.")
        break
    else:
        print("You entered:", num)

21.
print("Using for loop:")
for i in range(1, 101):
    print(i, end=" ")

print("\n\nUsing while loop:")
i = 1
while i <= 100:
    print(i, end=" ")
    i += 1

print("\n\nUsing simulated do-while loop:")
i = 1
while True:
    print(i, end=" ")
    i += 1
    if i > 100:
        break

22.
n = int(input("Enter N: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum of first", n, "natural numbers is:", total)

23.
n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial of", n, "is:", fact)

24.
num = int(input("Enter a number: "))
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num //= 10

print("Reversed number:", rev)

25.
num = int(input("Enter a number: "))
temp = num
count = 0
sum_digits = 0

while temp > 0:
    digit = temp % 10
    count += 1
    sum_digits += digit
    temp //= 10

print("Number of digits:", count)
print("Sum of digits:", sum_digits)

26.
num = int(input("Enter a number: "))

print("Multiplication Table of", num)
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

27.
low = int(input("Enter lower limit: "))
high = int(input("Enter upper limit: "))

print("Even numbers between", low, "and", high, ":")
for i in range(low, high + 1):
    if i % 2 == 0:
        print(i, end=" ")

28.
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(num, "is not a Prime number")
            break
    else:
        print(num, "is a Prime number")
else:
    print(num, "is not a Prime number")

29.
import math

num = int(input("Enter a number: "))
temp = num
sum_fact = 0

while temp > 0:
    digit = temp % 10
    sum_fact += math.factorial(digit)
    temp //= 10

if sum_fact == num:
    print(num, "is a Strong number")
else:
    print(num, "is not a Strong number")


30.
num = int(input("Enter a number: "))
temp = num
sum_digits = 0
prod_digits = 1

while temp > 0:
    digit = temp % 10
    sum_digits += digit
    prod_digits *= digit
    temp //= 10

if sum_digits == prod_digits:
    print(num, "is a Spy number")
else:
    print(num, "is not a Spy number")

31.
num = int(input("Enter a number: "))
temp = num
n = len(str(num))
sum_pow = 0

while temp > 0:
    digit = temp % 10
    sum_pow += digit ** n
    temp //= 10

if sum_pow == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

32.
num = int(input("Enter a number: "))
rev = int(str(num)[::-1])

if num == rev:
    print(num, "is a Palindrome number")
else:
    print(num, "is not a Palindrome number")
>>>>>>> d10122acda115640582992fd538e308dca19094c
