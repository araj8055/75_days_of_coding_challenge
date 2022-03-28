class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lst=[]
        for i in range(0,len(nums)):
            c=nums[i]**2
            lst.append(c)
        return(sorted(lst))
