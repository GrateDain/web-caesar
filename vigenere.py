from helpers import alphabet_position, rotate_character

def encrypt(text, rotation):
    n_text = ''
    key_rotation = 0
    for char in text:
        rot = rotation[key_rotation % len(rotation)]
        n_text += rotate_character(char, alphabet_position(rot))
        if alphabet_position(char) >= 0:
            key_rotation += 1
    return n_text

def main():
    message = str(input('Type a message:'))
    rotation = input('Encryption key:')
    print(encrypt(message, rotation))

if __name__ == '__main__':
    main()