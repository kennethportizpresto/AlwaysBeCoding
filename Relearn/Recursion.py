# Self pratice recursion
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

        print("Process finished with exit code 0")
    except AssertionError as a:
        print(a)
        print("Process finished with exit code 1")
