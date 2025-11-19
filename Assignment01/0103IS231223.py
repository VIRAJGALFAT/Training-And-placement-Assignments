# Condition statements, Ladder If, For Loop, While Loop

'''
Batch Time: 10:30 AM to 12:10 PM
Name: Viraj Galfat
Batch: 5
Enrollment: 0103IS231223

'''
# conditional statements

#Q1
num = int(input())
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#Q2
num = int(input())
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#Q3
year = int(input())
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")

#Q4
a = int(input())
b = int(input())
if a > b:
    print(a, "is greater")
elif b > a:
    print(b, "is greater")
else:
    print("Both are Equal")

#Q5 
age = int(input())
if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible")

#Q6
ch = input().lower()
if ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")

#Q7
num = int(input())
if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not Divisible")

#Q8
num = int(input())
if -9 <= num <= 9:
    print("Single Digit")
elif -99 <= num <= 99:
    print("Two Digit")
else:
    print("More than Two Digits")

#Q9
marks = int(input())
if marks >= 40:
    print("Pass")
else:
    print("Fail")

#10
num = int(input())
if num % 3 == 0 and num % 7 == 0:
    print("Multiple of 3 and 7")
else:
    print("No")

#LADDER IF & NESTED IF

# Q1
a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)


# Q2
age = int(input())
if age < 13:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior")


# Q3
marks = int(input())
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
elif marks >= 35:
    print("D")
else:
    print("Fail")


# Q4
a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")


# Q5
ch = input()

if ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Symbol")


# Q6
units = int(input())

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10

print(bill)


# Q7
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a > b:
    if a > c:
        if a > d:
            print(a)
        else:
            print(d)
    else:
        if c > d:
            print(c)
        else:
            print(d)
else:
    if b > c:
        if b > d:
            print(b)
        else:
            print(d)
    else:
        if c > d:
            print(c)
        else:
            print(d)


# Q8
year = int(input())
if year % 100 == 0:
    print("Century Year")
    if year % 400 == 0:
        print("Also Leap Year")
else:
    print("Not Century Year")



#FOR LOOP PROBLEMS

# Q1
for i in range(100, 1000):
    s = 0
    x = str(i)
    for d in x:
        s += int(d)**3
    if s == i:
        print(i)


# Q2
n = int(input())
count = 0
for i in range(2, 1000):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
        count += 1
        if count == n:
            break


# Q3
for i in range(1, 501):
    if i % 3 == 0:
        s = 0
        for d in str(i):
            s += int(d)
        if s <= 10:
            print(i)


# Q4
n = int(input())
for i in range(1, n+1):
    print("*" * (2*i - 1))


# Q5
s = input().lower()
alpha = "abcdefghijklmnopqrstuvwxyz"
found = True
for ch in alpha:
    if ch not in s:
        found = False
        break
if found:
    print("Pangram")
else:
    print("Not Pangram")


# Q6
prime = []
for i in range(2, 101):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime.append(i)

for i in prime:
    if i + 2 in prime:
        print(i, i + 2)


# Q7
num = int(input())
s = 0
for d in str(num):
    s += int(d)
if num % s == 0:
    print("Harshad")
else:
    print("Not Harshad")

#WHILE LOOP PROBLEMS

# Q11
num = int(input())
rev = 0
x = num
while x > 0:
    rev = rev*10 + x%10
    x //= 10

if rev < 2:
    print("Not Prime")
else:
    for i in range(2, rev):
        if rev % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")


# Q12
total = 0
while total <= 100:
    n = input()
    for d in n:
        total += int(d)
print("Done")


# Q13
num = input()
i = 0
found = False

while i < len(num):
    if num[i] == "0" and i != 0:
        found = True
    i += 1

if num[0] != "0" and found:
    print("Duck")
else:
    print("Not Duck")


# Q14
num = int(input())
x = num
seen = set()

while x != 1 and x not in seen:
    seen.add(x)
    s = 0
    while x > 0:
        s += (x % 10)**2
        x //= 10
    x = s

if x == 1:
    print("Happy Number")
else:
    print("Not Happy")


# Q15
n = int(input())
i = 2
largest = 1

while i*i <= n:
    while n % i == 0:
        largest = i
        n //= i
    i += 1

if n > 1:
    largest = n

print(largest)


# Q16
while True:
    s = input()
    if s == s[::-1]:
        print("Palindrome")
        break



