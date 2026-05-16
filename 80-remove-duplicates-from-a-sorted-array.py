class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start=2
        if len(nums)<=2:
            return len(nums)
        for i in range(2,len(nums)):
            if nums[i]!=nums[start-2]:
                nums[start]=nums[i]
                start+=1
        return start

          