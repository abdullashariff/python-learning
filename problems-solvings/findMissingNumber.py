arr = [1,2,4,5]
actualNumner = len(arr)+1 # arr length + missing number

# sumOfArr = 0
# for n in arr:
#     sumOfArr+=n
sumOfArr = sum(arr)

sumOfNum= (actualNumner * (actualNumner+1))//2
print('missingNo', sumOfNum - sumOfArr)