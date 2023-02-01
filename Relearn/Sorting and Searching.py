# Searching and Sorting Algorithms

# Searching Algorithms
"""
There are many searching algorithms. I will only focus on linear search, 
binary search, and Breadth First Search (BFS), 
Depth First Search (DFS), and Backtracking, 

"""

# Linear Search 
"""
Best-case: time: O(n), space: O(1), Worst-case: time = O(n), space = O(n)
1) We utilize a for loop or while loop
2) If recursive we utilize the target as the base case

Conclusion: Linear Search is a basic loop. When to use it? If the linear datastructure is simple and unsorted. 
            If we just want a simple solution and not care about efficiency (brute force). 
"""
from collections import defaultdict
def linearSearch_Recur(myList:list, key:int, arr_size = 0) -> int:
    if len(myList) == 0:
        return -1
    if myList[0] == key:
        return arr_size
    return linearSearch_Recur(myList[1:], key, arr_size + 1) 

def linearSearch_iterative(myList:list, target:int) -> int:
    index = 0 
    for i in range(len(myList)):
        if myList[i] == target:
            return index 
        index += 1 
    return -1

# Binary Search 
"""
Best-case: time: O(logn), space: O(1), Worst-case: time = O(logn), space = O(logn)
1) We divide the list and discard the left or right. 
2) We update the mid pointer and left or right. 
3) We continue to subdivide till we find the value we are looking for.

Conclusion: Binary Search is subdividing linear datastructure and discarding useless parts. When to use it? If the linear datastructure isn't complicated and is sorted.
            Is more efficient than a brute force approach. 
"""
def binarySearch(myList:list, target:int,) -> int:
    lptr, rptr = 0, len(myList) - 1
    while(lptr <= rptr):
        mid = (rptr+lptr)//2 
        if target == myList[mid]:
            return mid
        if target > myList[mid]:
            lptr = mid + 1 
        else:
            rptr = mid - 1 
    return -1

# Can you do it in recursion? 
def binarySearch_Recursion(myList:list, target:int, start:int, end:int):
    if start > end:
        return -1
    else:
        mid = (start+end)//2 
        if target == myList[mid]:
            return mid 
        if target > myList[mid]:
            return binarySearch_Recursion(myList,target, mid + 1, end)
        elif target < myList[mid]:
            return binarySearch_Recursion(myList,target, start, mid - 1)

# Can you do binarysearch if element is not present? Iterative
def binarySearch_iterative_missing(myList:list, target:int) -> int:
    lptr, rptr = 0, len(myList) - 1
    while(lptr <= rptr):
        mid = (lptr+rptr)//2 
        if target == myList[mid]:
            return mid 
        if target > myList[mid]:
            lptr = mid + 1
        else:
            rptr = mid - 1 
    return lptr

# Can you do binarysearch recursively if element is not present
def binarySearch_recursive_missing(myList:list, target:int, start:int, end:int) -> int:
    mid = (start+end)//2
    if start == end:
        if target > myList[0]:
            return mid + 1
        else:
            if mid == 0:
                return 0 
            else:
                return mid - 1 
    else:
        if target == myList[mid]:
            return mid
        if target > myList[mid]:
            return binarySearch_recursive_missing(myList, target, mid+1, end)
        else:
            return binarySearch_recursive_missing(myList, target, start, mid-1)

# Interpolation search
"""" 
Best-case: time = O(log(logn)) and space O(1)

Conclusion: We only use interpolation if the linear datastructure is in order and each element is uniform. 
            Uniform meaning each continigous element is equidistant from eachother by some value. 
            E.X: [1,3,5,7] It is in order and the sequence of elements are 2 values apart.
"""

# DFS
"""
Use a hash set to find base case. Keeps track of nodes we visited. When creating a dfs generally you do a for loop and recur and have the base case inside the for loop. 
When creating a graph ensure that there is one cycle. This is so we have a basecase. Every node must point to something which can be nothing or itself or other node. IT IS A KEY. 
"""

# DFS Facts
"""
DFS is more memory efficient and faster. DFS is not more optimal at finding the shortest path than BFS. DFS uses backtracking while BFS doesn't. BFS considers 
all neighbors level by level while traversing. An adjacency list is utilized in code to symbolize the graph. The adjacency list can be represented as a linked list or 
hashmap. BFS uses Queue data structure FIFO to find the and DFS uses Stack data structure LIFO. 
"""

graph = {
    '1' : ['2'],
    '2' : ['3', '4'],
    '3' : ['6'],
    '4' : ['3','5'],
    '6' : ['7'],
    '5' : [],
    '7' : ['3']
}

def dfs(visited, graph, node):
    print(node) 
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(visited, graph, neighbor) 


# must included disconnected graphs
class Graph:
    def __init__ (self) -> None:
        self.graph = defaultdict(list)

    def addEdge(self, currNode:str, otherNode) -> None:
        if otherNode == None:
            self.graph[currNode] = []
        else:
            self.graph[currNode].append(otherNode)
        
    def printDFS(self, node: str, memory: set) -> None:
        memory.add(node)
        print(node, end = " ")
        for i in self.graph[node]:
            if i not in memory:
                self.printDFS(i, memory) 

    def dfs(self, visited:set):
        for n in self.graph:
            if n not in visited:
                self.printDFS(n, visited)

# BFS
"""
To make BFS we need the start node. An empty list to keep track of seen values and a list to have queue.
Append the start node to the seen and put it in the queue to be popped.
We dequeue from the beginning and enque the edges for that key. When
queue is empty we can be done with the while loop. 
"""
class Graph_BFS:
    def __init__(self):
        self.graph = defaultdict(list) 

    def addEdge(self, curr, next):
        if next == None:
            self.graph[curr] = []
        else:
            self.graph[curr].append(next)
    
    def BFS(self, start)->list:
        visited_vertices = []
        queue = []

        visited_vertices.append(start)
        queue.append(start) 

        while queue:
            n = queue.pop(0) 
            print(n, end = " ")
            for v in self.graph[n]:
                if v not in visited_vertices:
                    queue.append(v) 

"""
"""
def bfs_1(graph, start, end):
    queue = []
    visited = []
    queue.append(start)
    visited.append(start)

    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            return path
        for adjacent in graph[node]:
            if adjacent not in visited:
                visited.append(adjacent)
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
        

if __name__== "__main__":
    try:
        assert linearSearch_Recur([1,2,3,4,5,6], 7) == -1, "TestCase 1: Func-linearSearch_Recur -> Failed did not return -1"
        assert linearSearch_Recur([1,2,3,4,5,6], 3) == 2, "TestCase 2: Func-linearSearch_Recur -> Failed did not 2"
        assert linearSearch_iterative([1,2,3,4,5,6], 7) == -1, "TestCase 3: Func-linearSearch_iterative -> Failed did not return -1"
        assert linearSearch_iterative([1,2,3,4,5,6], 4) == 3, "TestCase 4: Func-linearSearch_iterative -> Failed to return 3"
        assert binarySearch([0,1,2,3,4,5],5) == 5, "TestCase 5: Func-binarySearch -> Failed to return 5"
        assert binarySearch([0,1,2,3,4,6],5) == -1, "TestCase 6: Func-binarySearch -> Failed to return -1"
        assert binarySearch([1,2,3,4,5,6,7,8,9,10],8) == 7, "TestCase 7: Func-binarySearch -> Failed to return -1"
        myList = [1,2,3,4,5,6,7]
        assert binarySearch_Recursion(myList, 7, 0, len(myList)-1) == 6, "TestCase 8: Func-binarySearch_Recursion -> Failed to return 6"
        assert binarySearch_Recursion(myList, 8, 0, len(myList)-1) == -1, "TestCase 9: Func-binarySearch_Recursion -> Failed to return -1"
        assert binarySearch_iterative_missing(myList,8) == 7, "TestCase 10: Func-binarySearch_iterative_missing -> Failed to return 7"
        assert binarySearch_iterative_missing(myList,0) == 0, "TestCase 11: Func-binarySearch_iterative_missing -> Failed to return 0"
        assert binarySearch_recursive_missing(myList,8,0,len(myList)-1) == 7, "TestCase 12: Func-binarySearch_recursive_missing -> Failed to return 7"
        assert binarySearch_recursive_missing(myList,0,0,len(myList)-1) == 0, "TestCase 13: Func-binarySearch_recursive_missing -> Failed to return 0"
        visited = set()
        dfs(visited, graph, '1')
        assert visited == {'1','2','3','6','7','4','5'}, "TestCase 14: Func-dfs -> Failed to DFS"
        visited = set()
        myGraph = Graph()
        myGraph.addEdge('1','2')
        myGraph.addEdge('1','3')
        myGraph.addEdge('2', '4')
        myGraph.addEdge('3', None)
        myGraph.addEdge('4', None)
        myGraph.addEdge('5', '6')
        myGraph.addEdge('6', None)
        myGraph.addEdge('7', None)
        myGraph.addEdge('10','10')
        myGraph.dfs(visited)
        print()

        g = Graph_BFS()
        g.addEdge('5','3')
        g.addEdge('5','7')
        g.addEdge('3','2')
        g.addEdge('3','4')
        g.addEdge('4','8')
        g.addEdge('7','8')
        g.addEdge('2', None)
        g.addEdge('8', None)
        g.BFS('5')
        assert visited == {'7', '2', '10', '3', '4', '5', '1', '6'}, "TestCase 15: Func-Graph -> Failed to DFS with disconnected graphs"
        print()
        graph = {
            '5' : ['3','7'],
            '3': ['2', '4'],
            '4' : ['8'],
            '7' : ['8'],
            '2' : [],
            '8' : []}
        shortest_path = bfs_1(graph, '5', '8')
        print(shortest_path)

        #assert shortestpath_unweighted == ['1','3','7'], "TestCase 15: Func-Graph_BFS -> Failed to find shortest path"
        print("Process finished with exit code 0")
    except AssertionError as a:
        print(a)
        print("Process finished with exit code 1")
