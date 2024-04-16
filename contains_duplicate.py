def duplicate(num):
    return len(set(num)) != len(num)

arr = [1,2,3,4,5,6]

print(duplicate(arr))