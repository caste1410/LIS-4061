import toolsForSDES as tools
import SDES
import letterConversion as conversion

def main():
    key = "1011011010"
    plainText = "10110110"
    cyphertext = SDES.makeEncrytion(plainText,key)
    plaintext = SDES.makeDecryption(cyphertext,key)
    print("Cyphertext: "+ cyphertext)
    print("Plaintext: " + plaintext)

if __name__ == "__main__":
    main()
