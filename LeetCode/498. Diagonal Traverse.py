from collections import defaultdict
class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        result = []
        if not mat:
            return None
        outerIndex = len(mat)
        innerIndex = len(mat[0])
        myList = defaultdict(list)
        
        for i in range(outerIndex):
            for j in range(innerIndex):
                if i+j not in myList:
                    myList[i+j].append(mat[i][j])
                elif i+j in myList:
                    myList[i+j].append(mat[i][j]) 
                    
        for k,v in myList.items():
            if k % 2 == 0:
                result += v[::-1]
            else:
                result += v
        return result

# time = O(n^2)
# space = O(n)
