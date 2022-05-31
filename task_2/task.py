import os

system_16 = {}
for i in range(10):
    system_16[str(i)] = i
system_16.update({'a' : 10, 'b' : 11, 'c':12, 'd' : 13, 'e' : 14, 'f':15})

def hex_to_int_big_end(hex_num:str)->int:
    number,power = 0,len(hex_num)-1
    for i in hex_num:
        if not i in system_16:
            raise ValueError
        number += system_16[i]*16**power
        power-=1
    return number
def hex_to_int_little_end(hex_num:str)->int:
    number,power = 0,0
    for i in hex_num:
        if not i in system_16:
            raise ValueError
        number += system_16[i]*16**power
        power+=1
    return number
def norm_hex(hex_num:str)->int:
    hex_num = hex_num.lower()
    if 'x' in hex_num:
        hex_num = hex_num[hex_num.find('x')+1:]
    return hex_num

os.system("clear")
hex_num = input("Enter hex number: ")
hex_num = norm_hex(hex_num)

print("Number of bytes:",len(hex_num)//2)
print("Little-endian:",hex_to_int_little_end(hex_num))
print("Big-endian:",hex_to_int_big_end(hex_num))
    