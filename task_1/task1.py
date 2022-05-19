import random
import time
import os
def get_seq_sizes():
    bits = 8
    N = 4096
    while bits <= 4096:
        print(f"{bits}-bits sequence has {1 << bits} varients")
        bits*=2

def get_n_bit_number(number_of_bits: int):
    return random.randint(1,1 << number_of_bits)

def brutforce(number:int):
    i = 0
    start_timer = time.time()
    while True:
        if number == i:
            end_timer = time.time()
            print("Element found!")
            print("Linear search time required:", int(round((end_timer - start_timer) * 1000)),"ms")
            break
        i+=1
    return i
os.system("cls")
get_seq_sizes()
input("Press Enter to continue...")
os.system("cls")
print("=======BrutForce======")
bits = int(input("Enter number of bits: "))
number = get_n_bit_number(bits)
print("Generated number:",number)
print("\nBrutforcing... \n")
brutforce(number)