alphabet = "abcdefghijklmnopqrstuvwxyz"

def alphabet_position(letter):
    return alphabet.index(letter.lower())    

def rotate_character(char, rot):
    if  char.isalpha():
        new_letter = alphabet_position(char) + rot
        if new_letter < 26:
            if char == char.lower():
                return alphabet[new_letter]
            else:
                return alphabet[new_letter].upper()
        else:
            if char == char.lower():
                return alphabet[new_letter % 26]
            else:
                return alphabet [new_letter % 26].upper()
    else:
        return char
def encrypt(text, rot):
    result = ''
    for letter in text:
        result += rotate_character(letter,rot)
    return result

def main():
    print(encrypt('Hello, World!',5))
main()