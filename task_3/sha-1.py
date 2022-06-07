import math
import bitarray
from bitarray.util import int2ba



def read_chunk(bin_arr:bitarray.bitarray,start:int, size_of_chunk: int = 512)->bitarray:
    if len(bin_arr) <= start+size_of_chunk:
        return bin_arr[start:]
    return bin_arr[start:start+size_of_chunk]
def bitarray_to_int(bin_arr:bitarray.bitarray)->int:
    num = 0
    for bit in bin_arr:
        num = (num << 1) | bit
    return num
def leftrotate(array:bitarray.bitarray, steps:int)->bitarray.bitarray:
    for i in range(steps):
        array.append(array.pop(0))
    return array
def SHA1(msg:bitarray.bitarray)->str:
    
    #init vars
    h0 = 0X67452301
    h1 = 0XEFCDAB89
    h2 = 0X98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    #prepare message add 1 bit and k 0 bits
    message_length = len(msg)
    msg.append(1)
    if len(msg)%512 > 448:
        msg.extend([0]*((512-len(msg)%512)+448))
    else:
        msg.extend([0]*(448-len(msg)%512 ))
    
    #add message length
    bin_length = int2ba(message_length)
    #add zeros to the begining
    if len(bin_length) < 64:
        bin_length = bitarray.bitarray([0]*(64-len(bin_length)))+bin_length
    msg.extend(bin_length)

    start =  0
    chunk = read_chunk(msg,0)
    while len(chunk) !=0:
        #split into words with 32 bits
        words = []
        for i in range(0,16):
            words.append(chunk[i*32:(i+1)*32])
        #extend array to 80 elements
        for i in range(16,80):
            words.append(words[i-3]^words[i-8]^words[i-14]^words[i-16])
        
        #init hash values
        a = h0
        b = h1
        c = h2
        d = h3
        e = h4
        
        #main loop
        for i in range(80):
            if i <= 19:
                f = (b ^ c) | ((~ b) & d)
                k = 0x5A827999
            elif i <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif i <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            elif i <=79:
                f = b ^ c ^ d
                k = 0xCA62C1D6
        
            temp = bitarray_to_int(leftrotate(int2ba(a),5)) + f + e + k + bitarray_to_int(words[i])
            e = d
            d = c
            c = bitarray_to_int(leftrotate(int2ba(b),30))
            b = a
            a = temp

        h0 = h0 + a
        h1 = h1 + b 
        h2 = h2 + c
        h3 = h3 + d
        h4 = h4 + e

        #read new chunk
        start+=512
        chunk = read_chunk(msg,start)

    hash = list(map(hex,[h0, h1, h2, h3, h4]))

    return  hash
    

if __name__ == '__main__':
   
    bin_arr = bitarray.bitarray()

    #message = input("Input message: ")
    message = "abc"
    bin_arr.frombytes(message.encode('utf-8'))
    print("Hash value: ",SHA1(bin_arr))