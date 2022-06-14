from curses.ascii import islower
import random

def gen_key(size:int = 10):
    letters = list(map(chr,random.sample(range(ord('a'), ord('z')), size)))
    return "".join(letters)
def encode(message:str,key:str)->str:
    key_size = len(key)
    a_lower_code = ord('a')
    a_upper_code = ord('A')
    new_message = ""
    i = 0
    
    for letter in message:
        if not letter.isalpha():
            new_message+=letter
            continue

        coded_letter = (ord(letter.lower())+ord(key[i])-2*a_lower_code)%26
        i=(i+1)%key_size

        if islower(letter):
            new_message += chr(coded_letter+a_lower_code)
        else:
            new_message += chr(coded_letter+a_upper_code)

    return new_message
if __name__ == "__main__":
    message = input("Enter message: ")
    key =  gen_key()
    print("Key: ",key)
    print("Encoded message:",encode(message,key))

