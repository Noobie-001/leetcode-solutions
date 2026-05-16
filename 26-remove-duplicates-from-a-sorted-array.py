#logically correct but not fit for this problem 
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        expectedNums=[]
        for i in range(len(nums)):
            if nums[i] not in expectedNums:
                expectedNums.append(nums[i])
            nums[:]=expectedNums
        return len(nums)
        
#better approach
class Solution: 
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        start=0
        for i in range (1,len(nums)):
            if nums[i]!=nums[start-1]:
                nums[start]=nums[i]
                start+=1
        return start+1   
    
