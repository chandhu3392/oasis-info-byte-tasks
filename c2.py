import random
import string

def generate_password(length=12):
    # Define characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password using the defined characters
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    # Get desired password length from the user
    length = int(input("Enter the desired password length: "))

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
