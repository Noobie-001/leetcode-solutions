class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_Sum=0
        max_Sum=nums[0]
        for i in range(len(nums)):
            curr_Sum+=nums[i]
            if curr_Sum>max_Sum:
                max_Sum=curr_Sum
            if curr_Sum<0:
                curr_Sum=0
        return max_Sum
        