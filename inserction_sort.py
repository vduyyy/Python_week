def insertionSort(arr): 
    for i in range(1, len(arr)): 
        temp = arr[i] 
        j = i-1
        while j >=0 and temp < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = temp 
arr = [5,9,10,7,6,8] 
insertionSort(arr) 
for i in range(len(arr)): 
    print ("%d" %arr[i]) 