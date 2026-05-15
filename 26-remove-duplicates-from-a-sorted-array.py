#logically correct but not fit for this problem 
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        expectedNums=[]
        for i in range(len(nums)):
            if nums[i] not in expectedNums:
                expectedNums.append(nums[i])
        return expectedNums
        
#better approach
class Solution: 
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        k=1
        for i in range (1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[k]=nums[i]
                k+=1
        return k