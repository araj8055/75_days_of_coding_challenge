class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            d[i] = d.get(i,0)+1
        max_key = max(d,key=d.get)
        return max_key
