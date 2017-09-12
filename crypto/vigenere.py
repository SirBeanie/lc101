from helpers import alphabet_position, rotate_character

alphabet = "abcdefghijklmnopqrstuvwxyz"

def encrypt(text, key):
    result = ''
    key_encrypt = []
    for letter in key:
        key_encrypt.append(alphabet.index(letter.lower()))

    non_alpha = 0
    for i, letter in enumerate(text):
        if letter.isalpha():
            result += rotate_character(letter, key_encrypt[(i - non_alpha) % len(key_encrypt)])
        else:
            result += rotate_character(letter, key_encrypt[(i - non_alpha) % len(key_encrypt)])
            non_alpha += 1

    return result
    
def main():
    message = input("Type a message:")
    key = input("Encryption key")
    print(encrypt(message, key))


if __name__ == "__main__":
    main()
