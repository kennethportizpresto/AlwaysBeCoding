class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
   
        ptr = 0
        while (ptr < len(nums)):
            if nums[ptr] == val:
                nums.remove(nums[ptr]) 
            else:
                ptr += 1

# time = O(n)
# space = O(1)
