import json

class EncoderDecoder(object):

    def __init__(self):
        self.encodeDict = json.load(open("encodeDict.json"))
        self.decodeDict = {v: k for k, v in self.encodeDict.items()}

    def encoder(self):
        try:
            real = input("Enter text to be encoded: ")
            real = real.upper()
            fake = ""
            for letter in real:
                fake = fake + self.encodeDict[letter]

            print(fake)

        except Exception as Err:
            print("Error in Encoder: ", Err)


    def decoder(self):
        try:
            farzi = input("Enter text to be decoded: ")
            farzi = farzi.lower()
            asli = ""
            for chotu in farzi:
                asli = asli + self.decodeDict[chotu]

            print(asli)
        
        except Exception as Err:
            print("Error in Decoder: ", Err)


def main():
    try:
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

    except Exception as BigErr:
        print("Tut gaya thoda main: ", BigErr)

if __name__ == "__main__":
    main()

