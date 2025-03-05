message = input("What is the message? ")
shift = int(input("What is the shift? "))


def encode(message, shift):
    result = ""
    for letter in message:
        if letter.islower() == True:
            i = ord(letter)
            shifted_letter = i + shift
            if shifted_letter < 97:
                shifted_letter = shifted_letter + 26
            elif shifted_letter > 122:
                shifted_letter = shifted_letter - 26
            else:
                shifted_letter = shifted_letter    
        elif letter.isupper() == True:
            i = ord(letter)
            shifted_letter = i + shift
            if shifted_letter < 65:
                shifted_letter = shifted_letter + 26
            elif shifted_letter > 90:
                shifted_letter = shifted_letter - 26
            else:
                shifted_letter = shifted_letter    
        else:
            shifted_letter = ord(letter)

        p = chr(shifted_letter)
        result += p
    return result





print(encode(message, shift))
