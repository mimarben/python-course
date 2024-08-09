alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' or 'decode' to convert: \n").lower()
text = input("Type your message: : \n").lower()
shift = int(input("Type the shift number: \n"))
#continue_cipher = input("Do you want to continue cipher? 'yes' or 'no'").lower()
#miguel
#sonblr
#7
def encrypter(orignal_text, shift_amount):
    encrypted_text = ""
    for letter in orignal_text:        
        shifted_position = alphabet.index(letter)+shift_amount
        shifted_position %=len(alphabet) # for the last letters start in the begin.
        encrypted_text += alphabet[shifted_position]
    return encrypted_text

def decrypter(encrypted_text, shift_amount):
    decrypter_text = ""
    for char in encrypted_text:
        shifted_position = alphabet.index(char)-shift_amount
        shifted_position %=len(alphabet) # for the last letters start in the begin.
        decrypter_text += alphabet[shifted_position]
    return decrypter_text

if direction == 'encode':
    print(encrypter(text, shift))
elif direction == 'decode':
    print(decrypter(text, shift))
else:
    print("Invalid direction. Please type 'encode' or 'decode'.")

print("________________________________________________________________")