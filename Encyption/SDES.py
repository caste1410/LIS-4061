import tools

def makeEncrytion(plaintext, key):
    firstKey, secondKey = tools.makeSubKeys(key)
    initialPermutation = tools.makePermutation(plaintext, tools.IP)
    firstRound = tools.generateFK(initialPermutation,firstKey)
    switchFR = tools.switch(firstRound)
    secondRound = tools.generateFK(switchFR, secondKey)
    cypherText = tools.makePermutation(secondRound,tools.RP)
    return cypherText

def makeDecryption(cyphertext,key):
    firstKey, secondKey = tools.makeSubKeys(key)
    initialPermutation = tools.makePermutation(cyphertext, tools.IP)
    firstRound = tools.generateFK(initialPermutation,secondKey)
    switchFR = tools.switch(firstRound)
    secondRound = tools.generateFK(switchFR, firstKey)
    plaintext = tools.makePermutation(secondRound,tools.RP)
    return plaintext

def main():
    key = "1011011010"
    plainText = "10110110"
    cyphertext = makeEncrytion(plainText,key)
    plaintext = makeDecryption(cyphertext,key)
    print("Cyphertext: "+ cyphertext)
    print("Plaintext: " + plaintext)

if __name__ == "__main__":
    main()