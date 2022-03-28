class Solution:
    def pivotIndex(self, arr: List[int]) -> int:
        n=len(arr)
        sum1 = sum(arr)
        left = 0
        for i  in range(len(arr)):
            right = sum1 - arr[i] - left
            if left == right:
                return i
            else:
                left += arr[i]
        return -1
