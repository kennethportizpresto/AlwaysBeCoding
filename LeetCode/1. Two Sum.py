class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        myDict = {}
        for i in range(len(nums)):
            diff = target - nums[i] 
            if diff in myDict:
                return [myDict[diff], i]
            myDict[nums[i]] = i

#Time Complexity = O(a) we scale our time based on our length of nums
#Space Complexity = O(a) our auxiliary memory is utlizing a amount of elements in our nums
