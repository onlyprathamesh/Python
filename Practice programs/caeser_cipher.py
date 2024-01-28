<<<<<<< HEAD
from caeser_cipher_art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
value = False
while not value:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def operation (cipher_text, shift_number, operation_direction) :
        end_text = ""
        
        if operation_direction == "decode" :
            shift_number *= -1

        for letter in cipher_text :
            if letter in alphabet :
                letter_index = alphabet.index(letter)
                new_shift = letter_index + shift_number
                new_letter = alphabet[new_shift]
                end_text += new_letter
        print(f"Your {direction}d messege is : {end_text}")

    operation (cipher_text=text, shift_number=shift, operation_direction=direction)
    next_operation = str(input("Do u want to run again? (yes or no) : ")).lower()

    if next_operation == "no" :
        value = True



'''
Done by using 2 seperate functions
def encrypt (plain_text, shift_command) :
   cipher_text = ""
   for letter in plain_text :
    letter_place = alphabet.index(letter)
    shifted_value = letter_place + shift_command
    if shifted_value >= 26 :
        shifted_value = shifted_value - 26
    new_letter = alphabet[shifted_value]
    cipher_text += new_letter
   print(f"Your Encrypted messege is : {cipher_text}")

def decrypt (plain_text, shift_command) :
    cipher_text = ""
    for letter in plain_text :
     letter_place = alphabet.index(letter)
     shifted_value = letter_place - shift_command
     new_letter = alphabet[shifted_value]
     cipher_text += new_letter
    print(f"Your Decrypted messege is : {cipher_text}")

if direction == "encode" :
    encrypt(plain_text = text, shift_command =shift)
elif direction == "decode" :
    decrypt(plain_text = text, shift_command =shift)
else :
    print("You have choose wrong input. Please Try Again...!")
=======
from caeser_cipher_art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
value = False
while not value :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def operation (cipher_text, shift_number, operation_direction) :
        end_text = ""
        
        if operation_direction == "decode" :
            shift_number *= -1

        for letter in cipher_text :
            if letter in alphabet :
                letter_index = alphabet.index(letter)
                new_shift = letter_index + shift_number
                new_letter = alphabet[new_shift]
                end_text += new_letter
        print(f"Your {direction}d messege is : {end_text}")

    operation (cipher_text=text, shift_number=shift, operation_direction=direction)
    next_operation = input("Do u want to run again? (yes or no) : ").lower

    if next_operation == "no" :
        value = True



'''
Done by using 2 seperate functions
def encrypt (plain_text, shift_command) :
   cipher_text = ""
   for letter in plain_text :
    letter_place = alphabet.index(letter)
    shifted_value = letter_place + shift_command
    if shifted_value >= 26 :
        shifted_value = shifted_value - 26
    new_letter = alphabet[shifted_value]
    cipher_text += new_letter
   print(f"Your Encrypted messege is : {cipher_text}")

def decrypt (plain_text, shift_command) :
    cipher_text = ""
    for letter in plain_text :
     letter_place = alphabet.index(letter)
     shifted_value = letter_place - shift_command
     new_letter = alphabet[shifted_value]
     cipher_text += new_letter
    print(f"Your Decrypted messege is : {cipher_text}")

if direction == "encode" :
    encrypt(plain_text = text, shift_command =shift)
elif direction == "decode" :
    decrypt(plain_text = text, shift_command =shift)
else :
    print("You have choose wrong input. Please Try Again...!")
>>>>>>> d6923851b62279e23da6ef0dfb58ffafc1517201
'''