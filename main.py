import json
import base64
from cryptography.fernet import Fernet

# Generate a key for encryption
def generate_key():
    return Fernet.generate_key()

# Encrypt data
def encrypt_data(key, data):
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data

# Decrypt data
def decrypt_data(key, encrypted_data):
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
    return decrypted_data

# Load passwords from file
def load_passwords(file_path, key):
    try:
        with open(file_path, 'rb') as file:
            encrypted_passwords = json.load(file)
            decrypted_passwords = {decrypt_data(key, encrypted_password): decrypt_data(key, encrypted_username) for encrypted_username, encrypted_password in encrypted_passwords.items()}
        return decrypted_passwords
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_passwords(file_path, passwords, key):
    encrypted_passwords = {base64.b64encode(encrypt_data(key, username)).decode(): base64.b64encode(encrypt_data(key, password)).decode() for username, password in passwords.items()}
    with open(file_path, 'w') as file:  # Open the file in text mode ('w')
        json.dump(encrypted_passwords, file)

# Main function
def main():
    file_path = 'passwords.json'
    key = generate_key()

    # Load existing passwords or create a new dictionary
    passwords = load_passwords(file_path, key)

    while True:
        print("\nPassword Manager Menu:")
        print("1. View saved passwords")
        print("2. Add a new password")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            if passwords:
                print("\nSaved Passwords:")
                for username, password in passwords.items():
                    print(f"Username: {username}, Password: {password}")
            else:
                print("No passwords saved.")

        elif choice == '2':
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            passwords[username] = password
            save_passwords(file_path, passwords, key)
            print("Password saved successfully.")

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
