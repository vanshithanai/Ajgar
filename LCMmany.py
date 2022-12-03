dig = input("Enter the numbers w a space in betwwen: ")
dig = dig.split(" ")

nums = [int(i) for i in dig]

allprod = 1
for v in nums:
    allprod = allprod * v

min = min(nums)
bigs = [p for p in nums if p!= min]

for q in range(min,allprod+1,min):
    lcm = True
    for h in bigs:
        if q % h != 0:
            lcm = False
            break
    
    if lcm:
        print(q)
        break











