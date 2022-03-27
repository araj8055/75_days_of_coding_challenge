class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n=len(nums)
        count=0
        for i in range(0,n):
            if nums[i]!=0:
                nums[count]=nums[i]
                count += 1
        while count<n:
            nums[count]=0
            count += 1
