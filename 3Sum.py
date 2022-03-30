class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dic={}
        nums.sort()
        ans=[]
        for i in range(len(nums)-2):
            start = i+1
            end=len(nums)-1
            for j in range(i,len(nums)-1):
                if start == end:
                    break
                if nums[i]+nums[start]+nums[end]==0:
                    ans.append((nums[i],nums[start],nums[end]))
                    start += 1
                elif nums[i]+nums[start]+nums[end]<0:
                    start += 1
                elif nums[i]+nums[start]+nums[end]>0:
                    end -= 1
        ans=set(ans)
        return list(ans)
