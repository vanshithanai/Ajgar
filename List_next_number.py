# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].


num = [1, 2, 3]

dig = ''
for i in num:
    i = str(i)
    dig = dig + i

dig = int(dig)
next = dig + 1

nexts = str(next)
final = []

for i in nexts:
    i = int(i)
    final.append(i)


print(next)
print(final)



