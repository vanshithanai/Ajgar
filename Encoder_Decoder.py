class EncoderDecoder(object):

    def __init__(self):
        self.encodeDict = {"A" : "p", 
                "B" : "o",
                "C" : "i",
                "D" : "u",
                "E" : "y",
                "F" : "k"}

        self.decodeDict = {v: k for k, v in self.encodeDict.items()}

    def encoder(self):
        real = input("Enter text to be encoded: ")
        real = real.upper()
        fake = ""
        for letter in real:
            fake = fake + self.encodeDict[letter]

        print(fake)

    def decoder(self):
        farzi = input("Enter text to be decoded: ")
        farzi = farzi.lower()
        asli = ""
        for chotu in farzi:
            asli = asli + self.decodeDict[chotu]

        print(asli)


def main():
    ENDE = EncoderDecoder()
    cnt = 0
    while True:
        task = input("Enter 1 if you want to Encode, 2 for Decode: ")
        if task == "1":
            ENDE.encoder()
            break
        elif task == "2":
            ENDE.decoder()
            break
        else:
            print("Try Again")
            cnt = cnt + 1
            if cnt > 2:
                break  
        
    print("Bhak")

if __name__ == "__main__":
    main()

