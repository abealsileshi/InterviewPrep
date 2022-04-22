
def flippingBits(n):
    # temp1 = 0b00000000000000000000
    # temp1 = temp1 | n
    print("This is the binary number: ", ~0)
    # for i in range(len(lela)):
        
    #     if lela[i] == 1:
    #         temp += "0"
    #     else:
    #         temp += '1'
    # print("This is the FLIPPED binary number: ", temp)
    
              
    return ~n

if __name__ == '__main__':
    res1 = flippingBits(2147483647)
    print('Expected output: 2147483648', "Your output: ", res1)
    # res2 = flippingBits(0)
    # print("Expected output: 4294967295", "Your output: ", res2)

    # def flippingBits(n):
    # lela = format(n, '32b')
    # print("lela: ", lela)
    # lela = int(lela)
    # bn = bin(n)
    # bn = str(bn)
    # temp = ""
    # temp1 = 0b00000000000000000000
    # temp1 = temp1 | lela
    # # print("This is the binary number: ", temp1)
    # lela = str(lela)
    # for i in range(len(lela)):
        
    #     if lela[i] == 1:
    #         temp += "0"
    #     else:
    #         temp += '1'
    # # print("This is the FLIPPED binary number: ", temp)
    # n = int(temp, 2)
              
    # return n
