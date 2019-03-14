import tools

def main():
    print(tools.asciiToByte("a"), tools.byteToASCCII(tools.asciiToByte("a")))
    print(tools.asciiToHex("a"), tools.hexToASCII(tools.asciiToHex("a")))
    print(tools.byteToHex("01100001"), tools.hexToByte("61"))

if __name__ == "__main__":
    main()
