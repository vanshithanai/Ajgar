# Check if palindrome

www = input("Kya check karna batao: ")
www = www.lower()
revwww = www[::-1]

if www == revwww:
    print("ulta seedha same")
else:
    print("ulta seedha not same")

