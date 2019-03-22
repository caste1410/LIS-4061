import ESDES
import toolsForSDES as tools
import time

array = []

def openfile(filename):
    with open(filename, 'r') as file:
        for line in file:
            array.append((line.strip()))
    array.sort()

def makeBruteForce(plaintext, cyphertext):
    key = ""
    randomKey = ""
    for i in tools.rk:
        for j in array:
            if ESDES.makeDecryption(cyphertext,i,j) == plaintext:
                key += j
                randomKey += i
                break
            else:
                continue
    return [randomKey, key]

def main():
    openfile("bits.txt")
    plaintext = "DIDYOUSEE"
    cyphertext = "814181e643e6ecbccb"
    print("Plaintext: ", plaintext)
    print("Cyphertext: ", cyphertext)
    begin = time.time()
    x = makeBruteForce(plaintext, cyphertext)
    print("Tiempo que tardo: ", time.time() - begin)
    print("Random Key: ", x[0])
    print("Key: ", x[1])


if __name__ == "__main__":
    main()
                


