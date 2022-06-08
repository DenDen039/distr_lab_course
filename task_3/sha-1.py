def read_chunk(bite_arr:bytearray,start:int, size_of_chunk: int = 64)->bytearray:
    if len(bite_arr) <= start+size_of_chunk:
        return bite_arr[start:]
    return bite_arr[start:start+size_of_chunk]

def left_rotate(n:int, b:int)->int:
    return (((n & 0xffffffff) << b) | (n >> (32 - b))) & 0xffffffff

def SHA1(msg:bytearray)->list:
    
    #init vars
    h0 = 0x67452301
    h1 = 0XEFCDAB89
    h2 = 0X98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    #prepare message add 1 bit and k 0 bits
    message_length = len(msg)*8
    msg.append(1<<7)
    if len(msg)%64 > 56:
        msg.extend([0]*((64-len(msg)%64)+56))
    else:
        msg.extend([0]*(56-len(msg)%64 ))

    # add message length
    msg.extend(message_length.to_bytes(8, 'big'))


    start =  0
    chunk = read_chunk(msg,0)
    while len(chunk) !=0:
        #split into words with 32 bits
        words = []
        for i in range(0,16):
            words.append(chunk[i*4:(i+1)*4])
        #extend array to 80 elements
        for i in range(16,80):
            
            words.append(left_rotate(
                int.from_bytes(words[i-3],'big')^int.from_bytes(words[i-8],'big')^
                int.from_bytes(words[i-14],'big')^int.from_bytes(words[i-16],'big'),1)
                .to_bytes(4, 'big'))
        
        #init hash values
        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        #main loop
        for i in range(80):
            if i <= 19:
                f = (b & c) | ((~ b) & d)
                k = 0x5A827999
            elif 20 <= i and i <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= i and i <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            elif 60 <= i and i <=79:
                f = b ^ c ^ d
                k = 0xCA62C1D6
            temp = (left_rotate(a,5)+ f + e+ k + int.from_bytes(words[i],'big'))%2**32
            e = d
            d = c
            c = left_rotate(b,30)
            b = a
            a = temp
            
        #update vars
        h0 = (h0 + a)%2**32
        h1 = (h1 + b)%2**32
        h2 = (h2 + c)%2**32
        h3 = (h3 + d)%2**32
        h4 = (h4 + e)%2**32

        #read new chunk
        start+=64
        chunk = read_chunk(msg,start)

    hash = list(map(hex,[h0, h1, h2, h3, h4]))

    return  hash

if __name__ == '__main__':
    message = input("Input message: ")
    byte_arr = bytearray(message.encode('utf-8'))
    print("Hash value: ",SHA1(byte_arr))