# Self pratice recursion

# When to use recursion or iteration?
# =====================================================================================================================================================================
# Recursion is used when we need n amount of loops. When iteration becomes complicated. Although, we can recur on an iterative problem
# an efficient iteration is faster and more space efficient than recursion. Moreover, when recursion is the same time complexity it sacrifices
# space efficiency. Although, iteration is better for iterative problems recursion can improve readbility. An example where recursion makes sense
# are trees. You can imagine a computer with n directories and for each n directories there are n amount of subdirectories so on and so forth. An
# iterative approach would be complicated as we need to nest for loops n amount of times. The complexity of the problem scales exponentially. 
# Therefore using recursion to split up the problem into smaller subproblems until finding a base case and backtracking in the stack to merge with other
# subproblem answers to solve the big problem it becomes easier. We do not need to know n amount of loops we just need to know a basecase and how to break
# up the problem and to ensure merging each solution is done correctly. 

# Iteration is used if and only if the datastructure is simple and can be done with nested loops that are less than 4 in depth. Iteration can be used on 
# a multidimensional array because we know the furthest for loop would be a depth of 2. A scenario where we may need a depth of 3 loops is potentially an outer loop
# being a while loop where a condition needs to be met in order to stop cycling over the multidimensional array.
# =====================================================================================================================================================================
""" 
Note To Self: With each recursive call we must check the base case to start merging lists... 
adding the operand left or right of the list determines where the element is being 
added to the returned list... Ex: [1] + [2,3] = [1,2,3] and [1,2,3] + [1] = [1,2,3,1]
"""
def count(numRecur:int) -> int:
    ''' Counts the amount of recursion '''
    if numRecur == 0:
        return 0
    return 1 + count(numRecur - 1)

def countDV(numRecur:int, counter=0) -> int:
    ''' Counts the number of recursion utilizing default values '''
    if numRecur == 0:
        return counter
    return countDV(numRecur-1, counter + 1)

def recur(myList:list) -> list:
    ''' Recursively copies the input list'''
    if len(myList) == 1:
        return [myList[0]]
    return [myList[0]] + recur(myList[1:])


def reverse(myList:list) -> list:
    ''' Recursively copies the input list and reverses the result '''
    tmp = []
    if len(myList) == 1:
        return [myList[0]]
    return reverse(myList[1:]) + [myList[0]]

def odd(myList:list) -> list:
    ''' Returns a list of odd elements from the input list '''
    tmp = []
    if len(myList) == 1:
        return [] if myList[0] % 2 == 0 else [myList[0]]
    if myList[0] % 2 != 0:
        tmp.append(myList[0])
    return tmp + odd(myList[1:])

def even(myList:list) -> list:
    ''' returns a list of even elements from the input list '''
    tmp = []
    if len(myList) == 1:
        return [] if myList[0] % 2 == 0 else [myList[0]]
    if myList[0] % 2 != 0:
        tmp.append(myList[0])
    return tmp + odd(myList[1:])

def skip(myList:list) -> list:
    ''' based on the amount of index it will skip on every odd or even index '''
    tmp = []
    if len(myList) == 1:
        return []
    if len(myList) % 2 == 0:
        tmp.append(myList[0])
    return tmp + skip(myList[1:])

def skipTwice(myList:list) -> list:
    ''' skip two elements from the start then for every index that is two distance apart append'''
    tmp = []
    if len(myList) == 1:
        return [myList[0]]
    if (len(myList)-1) % 3 == 0:
        tmp.append(myList[0])
    return tmp + skipTwice(myList[1:])

def trueSkip(myList:list, counter = 1) -> list:
    ''' includes first element and skips from there '''
    tmp = []
    if len(myList) == 0:
        return []
    if counter % 2 != 0:
        tmp.append(myList[0])
    return tmp + trueSkip(myList[1:], counter + 1)

# Different types of Recursions
"""
Recursion falls into two cataegories: Direct and Indirect Recursion.
Direct Recursion directly calls itself in its body while Indirect 
Recursion calls another recursive function in a circular manner to subdivide the problem.

There are four main types of Direct Recursions: Tail, Head, Tree and Nested Recursion. 
Generally, variations such as Binary and Linear Recursion fall into Tree Recursion. 
Tail Recursion: Before calling the function it does n amount of instruction. 
Head Recursion: It must call itself no other operation is needed. 
Linear Recursion: The call function appears once in the body of the function. 
Binary Recursion: The call function appears twice in the body of the function.
Tree Recursion: The call function appears more than once in the body. 

Some variations of indirect recursion include mutual recursion, ... , etc. 
Mutual recursion has two function calling each other. You can imagine other 
terminology that expresses n amount of function calls dependent on other functions in a circular manner.
"""

def tailRecur(count:int) -> int:
    ''' You can imagine in a tree diagram the left side of the binary tree is executed first which are instructions carried out first then calls the function'''
    if count == 0:
        print("Countdown: ", count)
        return 0
    print("Countdown: ", count)
    return tailRecur(count - 1)

def headRecur(count:int) -> int:
    ''' You can imagine a binary tree that executes the left first before executing the right side which are other instructions'''
    if count == 0:
        return 0
    return headRecur(count - 1)

"""
Linear Data structures: Linked Lists or arrays. Left to right or right to left.
Binary Trees: It is a hierarchical data. Top to bottom. There are n amount of nodes. Root node is the top of the tree 
with n amount of children nodes left or right of it. Children may become the parent if it has children. 
Siblings are nodes that are on the same height of the tree. Parent nodes are nodes that have children. Leafs are nodes that
do not have children. They are the end of the tree at the maximum depth. Trees may have n amount of children but in a binary tree 
there are at most two children for every parent.
"""

# Tree Recursion
class Node:
    def __init__(self, data:int) -> None:
        '''' Initializes a node object to store data and information of left or right of the node '''
        self.data = data
        self.left = None
        self.right = None 

    def insert(self, data:int) -> None:
        if self.data:
            if data > self.data:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
            elif data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

def createBinaryTree():
    root = Node(None)
    while(True):
        myInput = input("Enter a number from 0-9 or type 'p' to print tree result or type 'esc' to exit: ")
        if len(myInput) == 1:
            if ord('0') <= ord(myInput) <= ord('9'):
                root.insert(myInput)
            elif myInput == 'p':
                print("Your Tree contains these elements: ")
                root.PrintTree()
            else:
                print("INVALID Input")
        else:
            if myInput == "esc":
                break
            elif myInput == "print":
                print("Your Tree contains these elements: ")
                root.PrintTree()
            else:
                print("INVALID Input")

# Nested Recursion
def nestedRecur(n:int) -> int:
    if n > 100:
        return n - 10
    return nestedRecur(nestedRecur(n+11))

# Indirect Recursion
def indirectRecurA(n:int) -> None: 
    if n > 0:
        print(n, ' ')
        indirectRecurB(n-1)

def indirectRecurB(n:int) -> None: 
    if n > 2:
        print(n, ' ')
        indirectRecurA(n-2)
# GeeksforGeeks Recursion problems

# Practice Question for Recursion | Set 1
# Explain the functionality of the following functions.

# Question 1
"""
    def fun1(x,y):
        if (x == 0): 
            return y
        else:
            return fun1(x-1, x+y)
"""
# This function returns the value of y. Because x decrements our y changes because y = x + y. We get our answer as we go down and return the y as we go back up the call stack. 

# Question 2

"""

# Minimum index finder
def minIndex(arr, s, e):
     
    sml = sys.maxsize
    mindex = 0
     
    for i in range(s, e):
        if (sml > arr[i]):
            sml = arr[i]
            mindex = i
             
    return mindex
 
def fun2(arr, start_index, end_index):
     
    if (start_index >= end_index):
        return
         
    min_index = minIndex(arr, start_index, end_index)
    arr[start_index], arr[min_index] = arr[min_index], arr[start_index]
    fun2(arr, start_index + 1, end_index)
"""

# We are sorting a list utilizing selection sort algorithm

# Challenge for self can you make the iterative approach?
def selectionSort(myList:list) -> None:
    for i in range(len(myList)):
        min_index = i
        for j in range(len(myList)-1,i-1,-1):
            if myList[min_index] > myList[j]:
                min_index = j
        myList[i], myList[min_index] = myList[min_index], myList[i]

# Workthrough without seeing the solution
def minIndex(myList:list, start:int, end:int) -> int:
    minIndex = start 
    for i in range(end, start-1, -1):
        if myList[i] < myList[minIndex]:
            minIndex = i 
    return minIndex

def selectionSortRecursion(myList:list, start:int, end:int) -> None:
    if start >= end:
        return 
    else:
        minIndx = minIndex(myList, start, end)
        myList[start], myList[minIndx] = myList[minIndx], myList[start] 
        selectionSortRecursion(myList, start + 1, end)

if __name__== "__main__":
    try:
        assert count(9) == 9, "TestCase 1: Func-count -> Wrong count of recursion"
        assert countDV(9) == 9, "TestCase 2: Func-countDV -> Wrong count of recursion"
        assert recur([1,2,3,4,5]) == [1,2,3,4,5], "TestCase 3: Func-recur -> List Does not Match"
        assert reverse([1,2,3,4,5]) == [5,4,3,2,1], "TestCase 4: Func-reverse -> List is not reversed"
        assert odd([1,2,3,4,5,6,7,8,9,10]) == [1,3,5,7,9], "TestCase 5: Func-odd -> List is not odd"
        assert skip([1,2,3,4,5,6,7,8,9,10,11]) == [2,4,6,8,10], "TestCase 6: Func-skip -> Fails to skip on even index"
        assert skip([1,2,3,4,5,6,7,8,9,10]) == [1,3,5,7,9], "TestCase 7: Func-skip -> Fails to skip on odd index"
        assert skipTwice([1,2,3,4,5,6,7,8,9]) == [3,6,9], "TestCase 8: Func-skipTwice -> Fails to skip twice"
        assert trueSkip([1,2,3,4,5]) == [1,3,5], "TestCase 9: Func-trueSkip -> Fails with odd amt of elements"
        assert trueSkip([1,2,3,4,5,6]) == [1,3,5], "TestCase 9: Func-trueSkip -> Fails with even amt of elements"
        assert tailRecur(10) == 0, "TestCase 10: Func-tailRecur -> Fails to countdown"
        assert headRecur(10) == 0, "TestCase 11: Func-headRecur -> Fails to dountdown"
        createBinaryTree()
        print("====== Continue on to our testcases ======")
        assert nestedRecur(95) == 91, "TestCase 12: Func-nestedRecur -> Fails to nest recursion"
        indirectRecurA(50)
        trueSkip_indirectRecur = [1,2,3,4,5,6,7]
        
        myList = [3,4,5,1,2,9,7]
        selectionSort(myList)
        assert myList == [1,2,3,4,5,7,9], "Test1: Func-selectionSort -> List is not ordered"
        myList = [3,4,5,1,2,9,7]
        selectionSortRecursion(myList, 0, len(myList)-1)
        assert myList== [1,2,3,4,5,7,9], "Test2: Func-selectionSortRecursion -> List is not ordered"

        print("Process finished with exit code 0")
    except AssertionError as a:
        print(a)
        print("Process finished with exit code 1")
