def asciiToByte(symbol):
    value = ord(symbol)
    bits = bin(value)[2:]
    diference = 8 - len(bits)
    repetition = "0" * diference
    return  repetition + bits

def asciiToHex(symbol):
    value = ord(symbol)
    return hex(value)[2:]

def byteToHex(byte):
    return hex(int(byte, 2))[2:]

def hexToByte(hex):
    bits = bin(int(hex, 16))[2:]
    diference = 8 - len(bits)
    repetition = "0" * diference
    return repetition + bits

def hexToASCII(hexa):
    return chr(int(hexa, 16))

def byteToASCCII(byte):
    return chr(int(byte, 2))