# Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.
# For example, "is2 sentence4 This1 a3" will be the sentence "This is a sentence"

from collections import OrderedDict

shufrecd = input("Write works w number at the end of each word: ")
shufrecd = shufrecd.split(" ")

kosh = {}


for h in shufrecd:
    word = ""
    num = ""
    for l in h:
        if l.isdigit():
            num += l
            num = int(num)
        else:
            word += l
        
    kosh[num] = word

koshS = OrderedDict(sorted(kosh.items()))
print(koshS.values())

fullSent = ""
for w in koshS.values():
    fullSent = fullSent + w + " "
    

print(fullSent)

