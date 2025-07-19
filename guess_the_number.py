# Number Guessing Game
# This is one of the most popular beginner Python programs because it teaches you:
#
# Random number generation
#
# User input
#
# Conditional logic (if, elif, else)
#
# Loops (while)
#
# Clean program structure

#Program Idea:
# The computer picks a random number between 1 and 10.

# The user guesses the number.

# The program gives feedback ("too high", "too low", or "correct").

# Loops until the user guesses correctly.

# First step, Import Pythons "random" module *This allows us to use the random function in python, which when called upon, produces a random number.

import random

# Make a variable that will generate a random number between 1 and 10
secret_number = random.randint(1, 10)

