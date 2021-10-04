arr = [ 222, 113, 0,23,23,12,456]

def bubbleSortfunction(arr):
    n = len(arr)
    for x in range(n-1):
        for i in range(0, n-x-1):
            if arr[i] > arr[i + 1] :
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


bubbleSortfunction(arr)
print ("Sorted array ")
for x in range(len(arr)):
    print ("% d" % arr[x]),
