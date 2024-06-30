import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    while True:
        try:
            length = int(input("Please enter the desired password length:"))
            if length < 1:
                print("The length must be at least 1. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    password = generate_password(length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()