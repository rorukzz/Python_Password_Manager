# Python Password Manager

This Python password manager allows you to securely store and manage your passwords. It encrypts the passwords using the Fernet encryption scheme to ensure their confidentiality.

## Features

- **Encryption**: Utilizes the Fernet symmetric encryption scheme for robust security.
- **Password Management**: Enables viewing saved passwords, adding new passwords, and seamless encryption and decryption of data.
- **File Storage**: Stores encrypted passwords in a JSON file for persistence.

## Prerequisites

- Python 3.x
- `cryptography` library (install via `pip install cryptography`)

## Installation

1. Clone or download this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.

## Usage

1. Run the `main.py` script.
2. Follow the on-screen prompts to manage your passwords:
   - View saved passwords
   - Add a new password
   - Exit the password manager

## Note

- **Security**: While this password manager encrypts passwords for storage, it's essential to keep the encryption key (`key`) safe and not share it with anyone. Losing the key will result in losing access to the encrypted passwords.
- **Backup**: Consider keeping backups of the encrypted password file (`passwords.json`) in a secure location.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to enhance the functionality or fix any bugs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
