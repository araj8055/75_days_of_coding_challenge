class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        sum1=0
        for i in range(0,len(nums)-1):
            if(nums[i]<nums[i+1]):
                sum1 += nums[i+1]-nums[i]
        return sum1
