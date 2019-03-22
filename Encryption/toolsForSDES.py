rk = ["123","132","213","231","312","321"]
P10 = (3, 5, 2, 7, 4, 10, 1, 9, 8, 6)
P8 = (6, 3, 7, 4, 8, 5, 10, 9)
P4 = (2, 4, 3, 1)
IP = (2, 6, 3, 1, 4, 8, 5, 7)
RP = (4, 1, 3, 5, 7, 2, 8, 6)
EP = (4, 1, 2, 3, 2, 3, 4, 1)
S0 =    [["01", "00", "11", "10"],
        ["11", "10", "01", "00"],
        ["00", "10", "01", "11"],
        ["11", "01", "11", "10"]]

S1 =    [["00", "01", "10", "11"],
        ["10", "00", "01", "11"],
        ["11", "00", "01", "00"],
        ["10", "01", "00", "11"]]
def makePermutation(value, permutation):
     permutedValue = ""
     for i in permutation:
         permutedValue += value[i-1]
     return permutedValue

def makeLS(keyPermuted):
     lsArray = []
     keyCopy = keyPermuted
     for i in range (1,3):
         halfKeyLeft = keyCopy[:int(len(keyCopy)//2)]
         halfKeyRight = keyCopy[int(len(keyCopy)//2):]
         keyLS = halfKeyLeft[i:] + halfKeyLeft[:i]
         keyRS = halfKeyRight[i:] + halfKeyRight[:i]
         lsArray.append(keyLS + keyRS)
         keyCopy = lsArray[i-1]
     return lsArray

def split(value):
    return [value[:len(value)//2],value[len(value)//2:]]

def xor(a, b):
    result = ""
    for i in range(len(a)):
        result += str(int(a[i]) ^ int(b[i]))
    return result

def getBoxValue(values, boxes):
    result = ""
    for value in values:
        i = 0
        row = int((value[0] + value[3]), 2)
        column = int((value[1] + value[2]), 2)
        result += boxes[i][row][column]
        i += 1
    return result

def makeSubKeys(key):
    permutation10 = makeLS(makePermutation(key, P10))
    firstKey = makePermutation(permutation10[0], P8)
    secondKey = makePermutation(permutation10[1], P8)
    return [firstKey, secondKey]

def generateFK(permutedPT, key):
    firstSplit = split(permutedPT)
    permutationEP = makePermutation(firstSplit[1],EP)
    xorEPK = xor(permutationEP,key)
    secondSplit = split(xorEPK)
    valueBox = getBoxValue(secondSplit,[S0,S1])
    permutation4 = makePermutation(valueBox, P4)
    xorP4LIP = xor(permutation4, firstSplit[0])
    result = xorP4LIP + firstSplit[1]
    return result

def switch(frOutput):
    return frOutput[len(frOutput)//2:] + frOutput[:len(frOutput)//2]

def rowTransposition(plaintext, key, rnd=1):
  matrix = list(zip(*[list(plaintext[i:i+len(key)]) for i in range(0, len(plaintext), len(key))]))
  matrix = list(map(lambda x : "".join(matrix[int(x)-1]), key))
  if rnd > 1:
    matrix = list(map(lambda x : shift(matrix[x], x), range(len(key))))
  return "".join(matrix)

def rowTranspositionInnverse(cyphertext, key, rnd=1):
  matrix = [[key[i//len(key)]] + list(cyphertext[i:i+len(key)]) for i in range(0, len(cyphertext), len(key))]
  if rnd == 1:
    matrix = list(map(lambda x : [matrix[x][0]] + shift(matrix[x][1:], len(key) -x), range(len(key))))
  matrix = list(map(lambda x : "".join(x), list(zip(*sorted(matrix)))[1:]))
  return "".join(matrix)

def shift(text, shifts):
  return text[shifts:] + text[:shifts]
    
    
