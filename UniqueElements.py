inp = input("Enter your numbers:")
inp = inp.split(" ")

arr = [int(i) for i in inp]
arr.sort()

print(arr)

k = 0
nums = []

for a in range(len(arr)):
    if arr[a] == arr[a+1]:
        # a ko aage badha do
    else:
        k += 1
        nums = nums.append(arr[a])

# Sort asc/desc, fir check w previous value - 0 se -1 ja raha kya karuuu
# If same, ignore. if alag then increase k and add that to "nums" wala list
# baaki list leave blank ya fir Len(original) - Len(nums) jitna _ or wtv daldo

