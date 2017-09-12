from helpers import alphabet_position, rotate_character

alphabet = "abcdefghijklmnopqrstuvwxyz"

def encrypt(text, rot):
    result = ''
    for letter in text:
        result += rotate_character(letter,rot)
    return result

def main():
    text = input("Type a message:")
    rot = int(input("Rotate by:"))
    print(encrypt(text, rot))


if __name__ == "__main__":
    main()
