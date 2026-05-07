class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        countSmallNums=[0]*len(nums)
        for i in range (0, len(nums)):
            for j in range(0, len(nums)):
                if nums[j]<nums[i]:
                    countSmallNums[i]+=1
        return countSmallNums

        