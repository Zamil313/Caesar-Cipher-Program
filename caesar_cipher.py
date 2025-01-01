def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def get_input(prompt):
    """Handles input with fallback for environments that do not support input()."""
    try:
        return input(prompt)
    except OSError:
        print(f"Input error occurred: Falling back to default input.")
        # Provide fallback inputs or exit gracefully.
        if "choice" in prompt.lower():
            return "3"  # Default to exit
        if "message" in prompt.lower():
            return "Test Message"  # Example default message
        if "shift" in prompt.lower():
            return "3"  # Example default shift value

def main():
    print("Caesar Cipher Program")
    while True:
        print("\nOptions:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")

        choice = get_input("Enter your choice (1/2/3): ")

        if choice == "1":
            message = get_input("Enter the message to encrypt: ")
            try:
                shift = int(get_input("Enter the shift value: "))
                if shift < 0 or shift > 25:
                    print("Shift value should be between 0 and 25. Please try again.")
                    continue
                encrypted_message = caesar_cipher_encrypt(message, shift)
                print(f"Encrypted message of {message}: {encrypted_message}")
            except ValueError:
                print("Invalid input for shift value. Please enter an integer.")

        elif choice == "2":
            message = get_input("Enter the message to decrypt: ")
            try:
                shift = int(get_input("Enter the shift value: "))
                if shift < 0 or shift > 25:
                    print("Shift value should be between 0 and 25. Please try again.")
                    continue
                decrypted_message = caesar_cipher_decrypt(message, shift)
                print(f"Decrypted message of {message}: {decrypted_message}")
            except ValueError:
                print("Invalid input for shift value. Please enter an integer.")

        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
