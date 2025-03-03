#Rehab Ahmed Sharaf Al-Dein
#Section 4

def insertionSort(arr):
    n = len(arr)
    
    if n <= 1:
        return
    for j in range(1,n):
        key = arr[j]
        i =j- 1
        while i>=0 and arr[i]>key:
            arr[i+1] = arr[i]
            i-=1
        arr[i+1] = key
        
        
arr=[13,12,11,6,5]
insertionSort(arr) 
print(arr)       