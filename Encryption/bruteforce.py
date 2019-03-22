array =  []
def openfile(filename):
    array = []
    with open(filename, 'r') as file:
        for line in file:
            array.append((line.strip()))
    array.sort()



