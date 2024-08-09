alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#miguel
#sonblr
#7

def ceasar_cipher(text:str, shift_amount: int, direction:str):
    ouput_text = ""
    if direction == "decode":
        shift_amount *= -1  # This is for decoding.
    for letter in text:
        if letter not in alphabet:
            ouput_text+=letter
        else:  
            shifted_position = alphabet.index(letter)+shift_amount
            shifted_position %=len(alphabet) # for the last letters start in the begin.
            ouput_text += alphabet[shifted_position]
    return ouput_text




should_continue = True

while should_continue:
    direction = input("Type 'encode' or 'decode' to convert: \n").lower()
    text = input("Type your message: : \n").lower()
    shift = int(input("Type the shift number: \n"))
    print(f"here you have a {direction} text: {ceasar_cipher(text=text, shift_amount=shift, direction=direction)}")
    restart =input("Do you want to continue cipher? 'yes' or 'no'").lower()
    if restart == "no":
        should_continue = False
    else:
        should_continue = True
