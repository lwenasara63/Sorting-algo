arr = [ 222, 113, 0 , 23 , 23 , 12 ,456]

def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for x in range(1, len(arr)):
 
        key = arr[x]
 
        j = x-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
 

insertionSort(arr)
for x in range(len(arr)):
    print ("% d" % arr[x])
