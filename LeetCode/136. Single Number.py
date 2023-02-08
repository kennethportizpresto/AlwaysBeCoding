class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = 0
        for i in nums:
            tmp = tmp ^ i
        return tmp

#time = O(n)
#space = O(1)
