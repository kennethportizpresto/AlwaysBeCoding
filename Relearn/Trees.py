# Binary Trees
"""
A binary tree contains a node that has a value and can have a left or right value. Since its a nonlinear datastructure we must use recursion.  
"""

class node:
    """
    preorder, inorder, and postorder are all dfs traversals.
    Level order is bfs traversals.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 
    def addEdge(self, value):
        if (self.value):
            if (value < self.value):
                if self.left is None:
                    self.left = node(value)
                else:
                    self.left.addEdge(value)
            elif (value > self.value):
                if (self.right is None):
                    self.right = node(value)
                else:
                    self.right.addEdge(value) 
        else:
            self.value = value

    # preorder binary tree traversal
    """
    root -> leftside -> rightside
    """
    def preOrderTraversal(self, root):
        res = [] 
        if (root):
            res.append(root.value)
            res += self.preOrderTraversal(root.left) 
            res += self.preOrderTraversal(root.right) 
        return res

    # Inorder binary tree traversal
    """
    Leftside -> root -> rightside
    """
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left) # We take the left side and add the right element from the left side so [1] + [2,3,4] 
            res.append(root.value) # Once we are back in the main stack we add the root in the middle
            res += self.inorderTraversal(root.right) # we sort the right side and ad the right side to the left on the main stack

            # OR just do this --> res = self.inorderTraversal(root.left)  + [root.value] + self.inorderTraversal(root.right)
        return res

    # postorder binary tree traversal
    """
    leftside -> rightside -> root
    """
    def postOrderTraversal(self, root):
        res = [] 
        if (root):
            res += self.postOrderTraversal(root.left) 
            res += self.postOrderTraversal(root.right)
            res.append(root.value) 
        return res

    def print_tree(self):
        if (self.left):
            self.left.print_tree() 
        print(self.value, end = " ")
        if (self.right):
            self.right.print_tree() 

    def bfs(self, root):
        if root is None:
            return
        queue = [root]

        while (queue):
            cur_node = queue.pop(0)
            print(cur_node.value, end = " ")
            if cur_node.left is not None:
                queue.append(cur_node.left)

            if cur_node.right is not None:
                queue.append(cur_node.right)
    
    def dfs_min_depth(self, root):
        if root is None:
            return 0 
        if root.left is None and root.right is None:
            return 1
        if root.left is None:
            return self.dfs_min_depth(root.right)+1
        if root.right is None:
            return self.dfs_min_depth(root.left)+1
        return min(self.dfs_min_depth(root.left), self.dfs_min_depth(root.right))+1
    

if __name__== "__main__":
    try:
        root = node(27)
        root.addEdge(14)
        root.addEdge(35)
        root.addEdge(10)
        root.addEdge(19)
        root.addEdge(31)
        root.addEdge(42)
        root.print_tree()
        print()
        assert root.inorderTraversal(root) == [10, 14, 19, 27, 31, 35, 42], "Func-node-inorderTraversal fails to produce the right list"
        assert root.preOrderTraversal(root) == [27, 14, 10, 19, 35, 31, 42], "Func-node-preOrderTraversal fails to produce the right list"
        assert root.postOrderTraversal(root) == [10, 19, 14, 31, 42, 35, 27], "Func-node-postOrderTraversal fails to produce the right list"
        root.bfs(root)
        print() 

        print(root.dfs_min_depth(root))
        print("Process finished with exit code 0")         
    except AssertionError as a:
        print(a)
        print("Process finished with exit code 1")