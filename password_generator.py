import random
import string

def get_password_length():
    while True:
        user_input = input("Enter the length of the password (default is 12): ") or "12"
        try:
            length = int(user_input)
            return length
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special_chars=True):
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special_chars = '!@#$%^&*()_+-=[]{}|;:,.<>?' if use_special_chars else ''

    # Combine character sets based on user preferences
    all_chars = lowercase_letters + uppercase_letters + digits + special_chars

    # Ensure at least one character from each selected set is included
    password = []
    if use_uppercase:
        password.append(random.choice(uppercase_letters))
    if use_digits:
        password.append(random.choice(digits))
    if use_special_chars:
        password.append(random.choice(special_chars))
    password.extend(random.choice(all_chars) for _ in range(length - len(password)))

    # Shuffle the password to ensure randomness
    random.shuffle(password)
    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    length = get_password_length()
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_uppercase, use_digits, use_special_chars)
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()
