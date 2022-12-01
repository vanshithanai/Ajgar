# greatest integer func of sqr root
import sys

pradan = input("Ank pradan kijiye: ")
pradan = int(pradan)

for i in range(sys.maxsize):
    if i*i > pradan:
        print(i-1)
        break



