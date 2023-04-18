def fromStringToBinary(string) :
    res = ''.join(format(i, '08b') for i in bytearray(string, encoding ='utf-8'))
    return res