import toolsForSDES as tools
import SDES
import letterConversion as conversion
import random

def generateBinaries(lista):
    binaries = []
    for i in lista:
        binaries.append(conversion.asciiToByte(i))
    return binaries
def makeCypherSDES(lista, key):
    cypherArray = []
    for i in lista:
        cypherArray.append(SDES.makeEncrytion(i, key))
    return cypherArray

def makeTextHex(lista):
    texthex = []
    for i in lista:
        texthex.append(conversion.byteToHex(i))
    return texthex
def makeCypherText(lista):
    result = ""
    for i in lista:
        result += i
    return result

def makeHexTextToBin(cyphertext):
    binaries = []
    for i in range(0,len(cyphertext), 2):
        x = i + 2
        binaries.append(conversion.hexToByte(cyphertext[i:x]))
    return binaries

def makeDecSDES(lista, key):
    cypherArray = []
    for i in lista:
        cypherArray.append(SDES.makeDecryption(i, key))
    return cypherArray
 
def makeText(lista):
    text = ""
    for i in lista:
        text += conversion.byteToASCCII(i)
    return text



def makeEncryption(plaintext, randomkey, key):
    plaintext = tools.rowTransposition(plaintext,randomkey)
    plaintext = tools.rowTransposition(plaintext,randomkey, 2)
    bpTransposition = generateBinaries(list(plaintext))
    cypherSDES = makeCypherSDES(bpTransposition,key)
    hexchar = makeTextHex(cypherSDES)
    cyphertext = makeCypherText(hexchar)
    return cyphertext

def makeDecryption(cyphertext, randomkey, key):
    cypherBits = makeHexTextToBin(cyphertext)
    desSDES = makeDecSDES(cypherBits, key)
    text = makeText(desSDES)
    text = tools.rowTranspositionInnverse(text,randomkey)
    plaintext = tools.rowTranspositionInnverse(text,randomkey,2)
    return plaintext


def main():
    key = "1000101010"
    rk = random.choice(tools.rk)
    ptn = "DIDYOUSEE"
    print("Key: ", key)
    print("Random Key: ", rk)
    print("Plaintext: ", ptn)
    cyphertext = makeEncryption(ptn, rk, key)
    print("Cyphertext: ", cyphertext)
    plaintext = makeDecryption(cyphertext, rk, key)
    print("Original text: ", plaintext)






if __name__ == "__main__":
    main()
