def alphabet_position(letter):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if abc.find(letter) >= 0:
        return abc.index(letter)
    elif ABC.find(letter) >=0:
        return ABC.index(letter)
    else:
        return -1

def rotate_character(char, rot):
    n_letter = ''
    abc = 'abcdefghijklmnopqrstuvwxyz'
    ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if alphabet_position(char) < 0:
        # import string; aBc =  string.ascii_letters()
        return char
    elif abc.find(char) >= 0:
        o_c = alphabet_position(char)
        n_c = (o_c + rot) % 26
        n_letter += abc[n_c]
        return n_letter
    else:
        o_c = alphabet_position(char)
        n_c = (o_c + rot) % 26
        n_letter += ABC[n_c]
        return n_letter