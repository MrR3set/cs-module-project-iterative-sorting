# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        while cur_index < len(arr): # Use while loop to find the smallest index in the remaining unsorted values
            if arr[cur_index] < arr[smallest_index]: # Check if the current evaluated element is smalled than the smallest element so far
                smallest_index = cur_index
            cur_index+=1
        # TO-DO: swap
        # Orthodox swapping technique
        temp = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp
        # Your code here
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    swapped = True # Asigning initial value just to do the while loop atleast once as the great python is to fancy to have do while loops
    while swapped:
        swapped = False # Asign the swapped value as false 
        for i in range(0,len(arr)-1): # Iterate the array until we reach the first sorted element
            if arr[i] > arr[i+1]: # Swap elements if the first one is bigger than the second one
                # Orthodox method for swaping values
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp
                swapped = True # Define swapped as true, to know that we swapped elements
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here
    # Check the array if it is empty if so return the empty array
    if len(arr) <= 0:
        return arr 
    # If the max value was not passed search for the max value iteraing trough the array.
    if maximum is None: 
        maximum = arr[0]
        for element in arr:
            if element > maximum:
                maximum = element
    # Define a new array with max len = maximum element
    buckets = [0]*(maximum+1) 
    # Write the bucket array based on the initial arr
    for element in arr: 
        buckets[element] += 1
        if element < 0: # Check for negative exceptions in the array 
            return f"Error, negative numbers not allowed in Count Sort"
    arr=[] # Empty the array so we can rewrite it
    for i in range(0,len(buckets)): # Loop trough the bucket array and write on arr acording to its value
        while buckets[i] > 0:
            arr.append(i)
            buckets[i]-=1

    return arr


print(counting_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))