#This program will ask a user for their name, age , and return a message Returning their name and how old they will be in 5 years

# Creates variable "name" (this will store the users name) , input - Command that allows us to ask the user a question, user answers question, There answer is stored in this variable
name = input("Enter your name: ")

# Create Variable "age", and uses "input" command to ask user what age they are, and stores it in this variable
age = input("How old are you? ")

#Convert the "age" variable to an integer so we can use it to do math
age = int(age)

# create a function that will take the users age and add 5 years
users_age_plus_five = age + 5

