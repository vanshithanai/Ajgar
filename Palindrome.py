# Check if palindrome

www = input("Kya check karna batao: ")
www = www.lower()
revwww = www[::-1]

if www == revwww:
    print("Already palindrome")
else:
    pali = www + revwww[1:]
    print("This is your palindrome: ", pali)

