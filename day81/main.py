MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

# while True:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#     text = input("Type your message:\n").upper()

    
#     again = input("You want go again? type 'yes' or 'no'\n").lower()
#     if again == 'no':
#         break

sample = 'thiago wilton'

def encrypt(entry):
    new_string = []
    for letter in entry.upper():
        if letter == ' ': new_string.append('/')
        for character in MORSE_CODE_DICT:
            if letter == character:
                new_string.append(MORSE_CODE_DICT.get(character))
    return ' '.join(new_string)

def decrypt(entry):
    entry_list = entry.split(' ')
    new_string = []
    for code in entry_list:
            if code == '/': new_string.append(' ')
            for character in MORSE_CODE_DICT:
                if code == MORSE_CODE_DICT.get(character):
                    new_string.append(str(character))
    return ''.join(new_string)

print(decrypt('- .... .. .- --. --- / .-- .. .-.. - --- -.'))