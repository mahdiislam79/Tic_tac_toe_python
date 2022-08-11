def binary_search(sequence,x):
    low = 0
    high = len(sequence) - 1 
    while low<=high:
        mid = (low+high)//2
        mid_value=sequence[mid] # lo + (hi-lo)//2 # this is used to avoid overflow if I use other languages except python
        if mid_value == x:
            return mid
        elif mid_value < x:
            low=mid+1
        else:
            high = mid-1
    return None

list1 = [1,2,3,4,5,6,7,8,9]
x1=4
print(binary_search(list1,x1))


