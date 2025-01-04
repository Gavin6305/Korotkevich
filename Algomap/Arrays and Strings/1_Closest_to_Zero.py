class Solution(object):
    def findClosestNumber(self, nums):
        closest = nums[0]
        for num in nums:
            if abs(num) <= abs(closest):
                if abs(num) == abs(closest):
                    closest = max(num, closest)
                else:
                    closest = num
        return closest
