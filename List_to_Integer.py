# The array-form of an integer num is an array representing its digits in left to right order.
# For example, for num = 1321, the array form is [1,3,2,1].
# Given num, the array-form of an integer, and an integer k,
# return the array-form of the integer num + k.

# Example 1:

# Input: num = [1,2,0,0], k = 34
# Output: [1,2,3,4]
# Explanation: 1200 + 34 = 1234



dig = [1,2,0,0]
k = input("Enter a number: ")
k = int(k)

num = ''
for i in dig:
    i = str(i)
    num = num + i

num = int(num)
sum = num + k


print(sum)



