"""
Sorting algorithms... Utilizing the builtin method is more optimal.
All parameters are pass by reference in python.
"""

# Selection Search
"""
Lets say we have books. We start at the leftmost book. We scan from left to right after the leftmost book to see if there is a book smaller than this one. 
If found switch. Next, The next book after the leftmost book becomes our new leftmost book. We repeat the process. We do this until there are no more book. 
"""
def selectionsort_iterative(myList:list)->None:
    ''' Time = O(n^2) and space = O(1)'''
    for i in range(len(myList)):
        myIndex = i
        for j in range(len(myList)-1, i, -1):
            if myList[j] < myList[myIndex]:
                myIndex = j 
        myList[i], myList[myIndex] = myList[myIndex], myList[i] 

def minIndex_helper(myList:list, index:int) -> int:
    minIndex = index 
    for j in range(len(myList)-1, index, -1):
        if myList[j] < myList[minIndex]:
            minIndex = j  
    return minIndex
    
def selectionsort_recursion(myList:list, index) -> None:
    ''' time: O(n + m) where n is the amount of time to recur and m is the amount of time to iterate space: O(n) where n is the stack memory '''
    if index >= len(myList)-1:
        return 
    else:
        minIndex = minIndex_helper(myList, index)
        myList[index], myList[minIndex] = myList[minIndex], myList[index] 
        selectionsort_recursion(myList, index+1)

# Insertion_sort
"""
This algorithm is used when organizing cards in your hand. We start at the leftmost card. We check the next card and see if the previous card is bigger. If so, we swap the cards until 
there are no cards bigger than the current card. After swapping we look at the new card we have not seen yet. We are essentally sorting the left side of the array and everytime we have
a new card we sort the left side again.  
"""
def insertionsort_iterative(myList:list) -> None:
    ''' time = O(n^2) space = O(1) '''
    for i in range(len(myList)):
        currIndex = i 
        while(currIndex > 0 and myList[currIndex-1] > myList[currIndex]):
            myList[currIndex], myList[currIndex-1] = myList[currIndex-1], myList[currIndex]
            currIndex -= 1

# Bubble_sort
"""
time = O(n^2) space = O(1)
We sort the list by looking at two items at a time. We switch if the curr and next item are out of place. We continue to look at two items at a time as we go towards the right. 
The right side of the array should accumulated sorted elements while we actively check the left side to right. As the right side becomes sorted we lesson our checking 
"""
def bubblesort(myList):
    for i in range(len(myList)-1): # We need to make sure all n elements are in the right place
        for j in range(0,len(myList)-i-1): # swapping occurs here but only n elements are in order from the rightmost side
            if myList[j] > myList[j+1]:
                myList[j], myList[j+1] = myList[j+1], myList[j]


# Merge_sort
"""
time complexity = O(n * logn) space = O(n)
Two ways to implement merge_sort
We return the array or we dont. Either way the original array is pass by reference therefore has changed. 

Explain: We divide the whole list like in binary search. However... we focus on the left side first and subdivide that part till it gets sorted. The first recursive call 
prevents us from sorting the right side until we sort the left first. Once sorted we went up the stack to store the resulting sorted leftside array or modified the list by using a local
list within a stack. The second recursive call now prevents us from merging the left and right till we sort the right side. 
Once sorted we went up the stack to store the resulting sorted rightside array or modified the list by using a local list within each stack. 
We then merge the left and right by comparing the full left and full right side of the list. 

Simple Explaination:
1) Split list in half
2) Call merge sort on each half to sort them recursively
3) Merge both sorted halves into one sorted array


psuedocode
1) if our length of array is greater than one keep dividing. Else we reach the base case and we go up the stack.
2) We define our middle. This middle updates for every recursion we preform. 
3) The first recursive call prevents us from sorting the right side of the array. 
4) The first recursive call forces us to divide the left side.
5) We recombine by comparing the left and right value of the left side of the array. 
6) Under each recursive call we utilize both the first and second recursive call but all this happens in the left array stack
7) Once recombination is complete the first recursive call stores the first half of the array to a variable. We went up to the "merge both sides" stack.
8) However, The second recursive call prevents us from recombining in the "merge both sides" stack
9) In the right side stack we sort the right side.
10) Once sorted and we are at the "merge both side" stack we compare both sides and update the array
11) Don't forget to return the array when we reach our base case

Visual of what is happening
=============================
Merge Both sides stack: [[unsorted left..], [unsorted right..]]

left side stack: [[unsorted,..] [unsorted,..]] -> [[unsorted] [unsorted]] -> [[element], [element]] -> [[sorted], [sorted]] [[sorted,..], [sorted,..]] -> [sorted..]
Merge Both sides stack: [[sorted..] [unsorted right]]

right side stack: [[unsorted,..] [unsorted,..]] -> [[unsorted] [unsorted]] -> [[element], [element]] -> [[sorted], [sorted]] [[sorted,..], [sorted,..]] -> [sorted..]
Merge Both sides stack: [[sorted..] [sorted..]]

Continue the code in the Merge Both sides stack: [sorted..]
=============================
"""
def mergesort_return(myList:list) -> list:
    if len(myList) > 1: # this is the base case once we have one element left in the list we go up the stack because one element is already sorted
        mid = len(myList)//2
        L = mergesort_return(myList[:mid]) # Initially these two recursive calls divide the overall list by left and right. 
        R = mergesort_return(myList[mid:]) # As we go down the stack we subdivide the left side only and recombine the left. As we go up the stack we recombine all sorted left elements. 
        # When done recombining we commence to the second recursive call at the parent stack and do the same process with the right side of the overall list. 

        # this code below modifies the original array by utilizing local subarrays 
        i,j,k = 0,0,0 # we can put this code in a merge helper function to improve readability
        while(i < len(L) and j < len(R)):
            if L[i] < R[j]:
                myList[k] = L[i] 
                i += 1
            else:
                myList[k] = R[j] 
                j += 1
            k += 1

        while(i < len(L)):
            myList[k] = L[i] 
            i += 1
            k += 1
        while(j < len(R)):
            myList[k] = R[j] 
            j += 1
            k += 1
    return myList

def mergesort_return_none(myList:list, lptr:int, rptr:int) -> None:
    if lptr < rptr:
        mid = (lptr+rptr)//2
        mergesort_return_none(myList, lptr, mid)
        mergesort_return_none(myList, mid+1, rptr)

        L = [0] * (mid - lptr + 1) # or we could of just done L = myList[:mid] and R = myList[mid:]
        R = [0] * (rptr - mid)

        for i in range(len(L)):
            L[i] = myList[lptr + i] # must add lptr because lptr index changes
        
        for j in range(len(R)):
            R[j] = myList[mid + 1 + j] # must add mid + 1 because we are on the right side

        i = j = 0 
        k = lptr # must be lptr because our starting index is either 0 or the mid
        while(i < len(L) and j < len(R)):
            if L[i] <= R[j]:
                myList[k] = L[i]
                i += 1
            else:
                myList[k] = R[j] 
                j += 1 
            k += 1
        
        while(i < len(L)):
            myList[k] = L[i]
            i += 1
            k += 1

        while(j < len(R)):
            myList[k] = R[j] 
            j += 1 
            k += 1
     
def mergesort_return_none_noptr(myList:list) -> list:
    if len(myList) > 1:
        mid = len(myList)//2
        L = myList[:mid]
        R = myList[mid:]
        mergesort_return_none_noptr(L)
        mergesort_return_none_noptr(R)

        i,j,k = 0, 0, 0

        while (i < len(L) and j < len(R)):
            if L[i] < R[j]:
                myList[k] = L[i] 
                i += 1
            else:
                myList[k] = R[j] 
                j += 1 
            k += 1
        while (i < len(L)):
            myList[k] = L[i] 
            i += 1
            k += 1
        while (j < len(R)):
            myList[k] = R[j] 
            j += 1 
            k += 1


# Quicksort
"""
time complexity: worst case is O(n^2) it depends on the pivot element best case is O(n * log(n))
1) choose a pivot element (anywhere but mostly the last one)
2) Store all elements less than the pivot in a subarray
3) Store all element greater than the pivot in another subarray
4) Call quicksort recursively on left subarray
5) Call quicksort recursively on right subarray

Coding: 
- Pointer going left to right is i. 
- Pointer going right to left is j. 
- Pivot pointer is p. Let's assume our pivot is the last element

Three scenarios...
1) switching elements around before switching the pivot to correct place:
We use pointer i and continue to right. If element bigger than p is found we stop. We check pointer j. 
We use pointer j and continue to the left. If element smaller than pivot found. We switch i and j. 
2) We continue to do this until i is at pivot or j passes i. If i meets pivot we dont do anything. Pivot is where it needs to be
3) If j crosses i we switch i with pivot or if j can no longer go left and is pointing at i.

Recursively... the pivot changes location and we look at left and right of it and sort... Wheever the pivot changes to is the correct spot. 

Code -> Basically the same as mergesort however our mid is the pivot. We must redefine the pivot each recursion. To find the pivot we need a helper function.

"""
def divide(arr, left, right):
    i = left
    j = right 

    while(i<j):
        while (i < right and arr[i] < arr[right]):
            i += 1
        while (j > left and arr[j] > arr[right]):
            j -= 1
        if (j>i):
            arr[i],arr[j] = arr[j], arr[i]
    if arr[i] > arr[right]:
        arr[i], arr[right] = arr[right], arr[i]
    return i

def quicksort(arr, left, right):
    if (left < right):
        pivot = divide(arr, left, right)
        quicksort(arr, left, pivot-1)
        quicksort(arr, pivot+1, right)

"""
The last two sorting algorithms rely on two recursive calls to divide the list into two parts and sort each part. Before doing recursive calls we must define what it means to be mid.
For merge we define mid with len(arr)//2 or (lptr+rptr)//2. We then sort when recombining. For quicksort we use pivot as mid. We must use a helper func to find the pivot.
"""

if __name__== "__main__":
    try:
        x = [3,2,1,5,6,4,7]
        selectionsort_iterative(x)
        assert x == [1,2,3,4,5,6,7], "1) Func-selectionsort_iterative -> Fails to sort"

        x = [3,2,1,5,6,4,7]
        selectionsort_recursion(x,0)
        assert x == [1,2,3,4,5,6,7], "2) Func-selectionsort_recursion -> Fails to sort"

        x = [3,2,1,5,6,4,7]
        insertionsort_iterative(x)
        assert x == [1,2,3,4,5,6,7], "3) Func-insertionsort_iterative -> Fails to sort"

        x = [3,2,1,5,6,4,7]
        bubblesort(x) 
        assert x == [1,2,3,4,5,6,7], "4) Func-bubblesort -> Fails to sort"

        x = [3,2,1,5,6,4,7]
        mergesort_return(x)
        assert x == [1,2,3,4,5,6,7], "5) Func-mergesort_return -> Fails to sort"
        assert mergesort_return(x) == [1,2,3,4,5,6,7], "6) Func-mergesort_return -> Fails to sort and return array"

        x = [3,2,1,5,6,4,7]
        mergesort_return_none(x,0,len(x)-1)
        assert x == [1,2,3,4,5,6,7], "7) Func-mergesort_return_none -> Fails to sort and return none"

        x = [3,2,1,5,6,4,7]
        mergesort_return_none_noptr(x)
        assert x == [1,2,3,4,5,6,7], "8) Func-mergesort_return_none_noptr -> Fails to sort and return none"

        x = [3,2,1,5,6,4,7]
        quicksort(x,0, len(x)-1)
        assert x == [1,2,3,4,5,6,7], "9) Func-quicksort -> Fails to sort"
        print("Process finished with exit code 0")

    except AssertionError as a:
        print(a)
        print("Process finished with exit code 1")