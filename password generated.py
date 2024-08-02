import string
import random
def generate_password(length):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    try:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            raise ValueError("The length should be a positive integer.")
        # Generate the password
        password = generate_password(length)
        # Display the password
        print("Generated Password: ", password)
    except ValueError as e:
        print("Invalid input:", e)
if _name_ == "_main_":
    main()
