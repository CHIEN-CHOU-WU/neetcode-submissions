class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if a > 0:
                break
            l, r = i + 1, len(nums) - 1
            while l < r:
                rightSum = nums[l] + nums[r]
                if a + rightSum == 0:
                    res.append([a, nums[l], nums[r]]) if [a, nums[l], nums[r]] not in res else None
                    r -= 1
                    l += 1
                elif a + rightSum > 0:
                    r -= 1
                else:
                    l += 1
        return res