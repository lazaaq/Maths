banyak = int(input("berapa banyak data? : "))
arr=[]
for i in range(0,banyak) :
    a = int(input(f"data ke {i+1} : "))
    arr.append(a)
def insertion_sort(arr) : 
    for i in range(0, len(arr)) :
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

insertion_sort(arr)
print ("Sorted array: ")
for i in range(len(arr)):
    print ("%d" %arr[i])