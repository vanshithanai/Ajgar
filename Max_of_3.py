

numbers = input("Enter 3 integers separated with spaces: ")
nums = numbers.split()

a = int(nums[0])
b = int(nums[1])
c = int(nums[2])
max = 0

if a > b:
    max = a
else:
    max = b


if c > max:
    max = c


print(max, " is the largest of the three numbers")





