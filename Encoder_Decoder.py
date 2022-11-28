buds = input("Kuch batao: ")
decodedict = {"A" : "p", 
              "B" : "o",
              "C" : "i",
              "D" : "u",
              "E" : "y",
              "F" : "k"}

buds = buds.upper()
new = ""
for letter in buds:
    new = new + decodedict[letter]

print(new)