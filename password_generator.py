import random
import string

def generate_password(length, use_uppercase=True, use_numbers=True, use_symbols=True):
    """
    Generate a secure random password.
    
    :param length: Length of the password.
    :param use_uppercase: Include uppercase letters.
    :param use_numbers: Include numbers.
    :param use_symbols: Include special symbols.
    :return: Generated password as a string.
    """
    # Define character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ""
    numbers = string.digits if use_numbers else ""
    symbols = string.punctuation if use_symbols else ""
    
    # Combine pools based on options
    all_characters = lowercase + uppercase + numbers + symbols

    if not all_characters:
        raise ValueError("At least one character set must be selected!")

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password


def main():
    print("Random Password Generator")
    
    # Get user input
    try:
        length = int(input("Enter password length (minimum 8): "))
        if length < 8:
            print("Password length must be at least 8 characters.")
            return

        use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'
        
        # Generate and display the password
        password = generate_password(length, use_uppercase, use_numbers, use_symbols)
        print("\nYour generated password:")
        print(password)
    
    except ValueError:
        print("Invalid input. Please enter valid values.")

if __name__ == "__main__":
    main()
