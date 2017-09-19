def min(arr):
    m = arr[0]
    for i in range(len(arr)):
        if arr[i] < m:
            m = arr[i]
    return m

def arifm(arr):
    x = arr[0]
    for i in range(len(arr)):
        x += arr[i]
    y = x / len(arr)
    return y

a = min([1,3,5,7,9,2,4,6,8,5,4,3])
b = arifm([1,2,3,4,5])

print(a)
print(b)

input()