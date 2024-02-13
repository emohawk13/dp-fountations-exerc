score = input("What did the student score?")

# Convert the input to an integer
score = int(score)

if score == 100:
    print("You got an 'A'! Good job!")
elif score >= 90: 
    print("You got an 'A'!")
elif score >= 80:
    print("You got a 'B'.")
elif score >= 70:
    print("You got a 'C'.")
elif score >= 60:
    print("You got a 'D'.")
else:
    print("You got an 'F'.")


# Magic 8-Ball Assignment
import random

# Random Responses 
opt1 = "Outlook good"
opt2 = "You may rely on it"
opt3 = "Ask again later"
opt4 = "Concentrate and ask again"
opt5 = "Reply hazy, try again"
opt6 = "My reply is no"
opt7 = "My sources say no"

option_list = [opt1,opt2,opt3,opt4,opt5,opt6,opt7]

question = input("Ask the magic 8 ball a question: (press enter to quit) ")

if question == "": 
    print("Goodbye!")
elif len(question) < 10:
  print("Please enter a valid question")
else:
    random_response = random.choice(option_list)
    print("Magic 8-Ball says:", random_response)
    

sentence = "The quick brown fox jumps over the lazy dog"
vowels = "aeiouAEIOU"

for i in sentence:
    if i not in vowels:
        print(i, end="")


sentence = "The quick brown fox jumps over the lazy dog"
vowels = "aeiouAEIOU"

for i in sentence:
    if i not in vowels:
        print(i, end="")


#FizzBuzz 
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


import random

# Random Responses 
opt1 = "Outlook good"
opt2 = "You may rely on it"
opt3 = "Ask again later"
opt4 = "Concentrate and ask again"
opt5 = "Reply hazy, try again"
opt6 = "My reply is no"
opt7 = "My sources say no"

option_list = [opt1,opt2,opt3,opt4,opt5,opt6,opt7]

while True:
    question = input("Ask the magic 8 ball a question: (Type 'quit' to end) ")
    
    if question.lower() == 'quit':
        print("Goodbye!")
        break 
    else:
        random_response = random.choice(option_list)
        print("Magic 8-Ball says:", random_response)
        print("Please ask another question or type 'quit' to end")


# Print Partial Range
for i in range(1,10):
    if 2 <= i <= 7:
        print(i)


pipeline = "1111111devpipeline2222222"

for char in pipeline:
    if char == "1" or char == "2":
        continue
    print(char, end="")



pipeline = "1111111devpipeline2222222"

for char in pipeline:
    if char == "1" or char == "2":
        continue
    print(char, end="")
