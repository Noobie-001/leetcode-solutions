class Solution(object):
    def twoSum(self, nums, target):
        d={}
        for i in range(len(nums)):
            
            complement=target-nums[i]
            if complement in d:
                return([d[complement], i])
            d[nums[i]] = i

#my unoptimised approach class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count=0
        for i in range(len(nums)):
            count=target-nums[i]
            if count in nums[i+1:]:
                indices=[i,nums.index((count),i+1)]