import random

# Welcome message
print("Welcome to the 1 times 1 trainer\n")

# Loop for the practice rounds
while True:
    # Generate random numbers for the task
    zahl1 = random.randint(1, 10)
    zahl2 = random.randint(1, 10)

    # Issue the task
    print("What is " + str(zahl1) + " times " + str(zahl2) + "?")
    
    # Get the user's answer
    answer = int(input("Answer: "))
    
    # Check if the answer is correct
    if answer == zahl1 * zahl2:
        print("Correct!")
    else:
        print("Wrong! The correct answer is " + str(zahl1 * zahl2) + ".")
    
    # Query whether the user wants to continue practicing
    fortsetzen = input("\nWould you like to continue practicing? (y/n) ")
    if fortsetzen.lower() != "y":
        break

# Farewell message
print("\n Thanks for practicing! Until next time.")
