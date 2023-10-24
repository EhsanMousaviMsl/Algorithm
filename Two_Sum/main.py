def two_sum(arr,target):
    dic = {} #value:index
    for i, n in enumerate(arr):
        diff = target - n
        if diff in dic:
            return[dic[diff],i]
        dic[n] = i
        
array = [2,3,5,9]
target = 8

print(two_sum(array,target))
