# Finding LCM of 2 numbers

dig = input("Enter the 2 numbers w a space in betwwen: ")
dig = dig.split(" ")

nums = [int(i) for i in dig]

big = max(nums)
small = min(nums)

lcm = False
for n in range(1,small):
    if (big * n) % small == 0:
        print("LCM is ", big * n)
        lcm = True
        break

if not lcm:
    print("LCM is ", big * small)



