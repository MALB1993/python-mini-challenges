# This is a basic application that evaluates the user's input 
# regarding their human state (good, bad, or average) and prints
# a corresponding message based on the input.

# Requesting the user's input about their state
word = input("Human state (good, bad, average)? ")

# Check if the input is "good" and print the corresponding message
if word == "good":
    print("You are a Good Person.")
# Check if the input is "average" and print the corresponding message
elif word == "average":
    print("You are an Average Person.")
# Check if the input is "bad" and print the corresponding message
elif word == "bad":
    print("You are a Bad Person.")
# If the input doesn't match any of the above, prompt the user to provide a valid input
else:
    print("Please type the correct word (Good, Bad, or Average).")
