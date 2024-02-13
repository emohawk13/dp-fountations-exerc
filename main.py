# Assignment 
# print() a string using double quotes ", including an apostrophe in the string
# print() a string using single quotes ', including an apostrophe in the string
# See what the output of each looks like.

#print("Printing using the double quotes!")
#print('Printing using single quotes!')

# common built in string functions 

name = 'Steve Harrington'
for_alpha = 'try'
#print in lower case
print(name.lower())
print()
print(name.upper())
print()
print(name.title())
print()
print(name.isalpha())
print()
print(for_alpha.isalpha())
print()

# Write a program that prints out a quote that you like. It should print the quotation, with proper quoting and punctuation. It should also print the author of the quote. For an extra challenge, make sure your quote also has at least one apostrophe in it.
quote = '"If you can\'t simply, you don\'t understand it well enough"'
person_name = "-Albert Einstein"

print(quote)
print(person_name)

#Concatenation 
first_name = "Steve"
last_name = "Harrington"

full_name = first_name + ' ' + last_name
print(full_name)

sub_total = 11.55
tax = sub_total * 0.2
total = sub_total + tax

print('Your total is $' + str(total))

sub_total = 11.55
tax = sub_total * 0.2
total = sub_total + tax

print(f'Your total is $ ${total:.2f}')

apples = 10
oranges = 12

print(f'I have {apples} apples and {oranges} oranges')

print(f'Your total is $ ${total:.20f}')

apples = 10
oranges = 12

print(f'I have {apples} apples and {oranges} oranges')


quantity = 6
item = 'bananas'
price = 1.74
print(f'Price per {item} is ${price/quantity}')
print(f'The Total is ${price * quantity}')


val = 12.3

print(f'{val:.2f}')
12.30

print(f'{val:.5f}')
12.30000

#leading zeros
x = 5

print(f'{x:01}')
print(f'{x*x:03}')
print(f'{x*x*x:05}')


# Justifying Data
s1 = 'a'
s2 = 'ab'
s3 = 'abc'
s4 = 'abcd'
# Default left-justification
print(s1)
print(s2)
print(s3)
print(s4)
# Center-Aligned 
print(f'{s1:^10}')
print(f'{s2:^10}')
print(f'{s3:^10}')
print(f'{s4:^10}')
# Right-justified
print(f'{s1:>10}')
print(f'{s2:>10}')
print(f'{s3:>10}')
print(f'{s4:>10}')



# Exercise

# Name   City       State         Age
# ------ ---------- ------------- ----
# Jane   Boston     Massachusetts  24
# Fred   Portland   Oregon         31
# Betsy  Orlando    Florida        29

name1 = 'Jane'
name2 = 'Fred'
name3 = 'Betsy'
city1 = 'Boston'
city2 = 'Portland'
city3 = 'Orlando'
state1 = 'Massachusetts'
state2 = 'Oregon'
state3 = 'Florida'
age1 = 24
age2 = 31
age3 = 29

h1 = 'Name'
h2 = 'City'
h3 = 'State'
h4 = 'Age'
dash ='-'

print(f'{h1:^6} {h2:^9} {h3:^13} {h4:^3}')
print(f'{dash*6} {dash*9} {dash*13} {dash*3}')
print(f'{name1:6} {city1:>9} {state1:13} {age1}')
print(f'{name2:6} {city2:>9} {state2:13} {age2}')
print(f'{name3:6} {city3:>9} {state3:13} {age3}')

#inputs
first_name = input("Please enter your First Name:")
greeting = f'Hi {first_name}'
print()
print(greeting)

number = input("Plese enter a number: ")
new_num = int(number)
print(type(number))
print(type(new_num))

#inputs exercise
#First Program
location = input("Where are you from? ")
print(f'I hear that living in {location} is nice!')

#Second Program
first_name = input("Please enter your first name: ")
question = input("What is your favorite animal? ")
print()
print(f'Hi {first_name}, a {question} is a cool animal! I bet your {question} loves {location}!')



# data type conversion
# Implicit Type Conversion
# automatically converts the data

num_int = 5
num_float = 12.49

total = num_int + num_float
print(type(total))
print(total)

# Explicit Type Conversion
# manually converting data yourself

age_str = input("How old are you? ")
age_num = int(age_str)
years_till_100 = 100 - age_num
print('You will be 100 years old in ' + str(years_till_100) + ' years')

# OR
age_num = int(input("How old are you? "))
print(f'You will be 100 years old in {100 - age_num} years')

x = "hello"
y = int(x)

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: 'hello'

# BASE 10 = 0-9

# Data loss
x = 6.65
y = int(x)
print(y)

# Integer Arithmetic
x = 5+2 * (6*2)
print(x)
y = 5 % 2
print(y)
z = 5 // 2
print(z)
a = 369532456 
print(a/32)


# Floating Point Arithmetic
x = 20072 * 10**-2
print(x)

if 0.2 != 0.199999:
    print(True)

test = 0.3 + 0.6 == 0.9

if test:
    print(True)
else:
    print(False)

test = .1 + .1 + .1 + .1 == .4

if test:
    print(True)
else:
    print(False)


x = 6.6 * 6.6

print(x)
print(f'{x:.2f}')


x = 6.6 * 6.6

print(x)
print(f'{x:.2f}')

if f'{x:.2f}' == '43.56':
    print(True)