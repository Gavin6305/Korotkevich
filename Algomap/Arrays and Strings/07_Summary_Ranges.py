class Solution(object):
    def summaryRanges(self, nums):
        # Edge cases
        if len(nums) == 0:
            return []

        result = []

        beginNum = nums[0]
        lastNum = nums[0]

        rangeLength = 0

        i = 1
        while i < len(nums):
            current = nums[i]
            # If current num is not in range, reset and append
            if current != lastNum + 1:
                # "a" if a == b
                if rangeLength == 0:
                    result.append(str(beginNum))
                # "a->b" if a != b
                else:
                    result.append(str(beginNum) + "->" + str(lastNum))
                # Reset range variables
                beginNum = current
                lastNum = current
                rangeLength = 0
            # If current num is in range, keep setting lastNum in range to current num
            else:
                lastNum = current
                rangeLength += 1
            
            i += 1
        
        # Last range
        if beginNum != lastNum:
            result.append(str(beginNum) + "->" + str(lastNum))
        else:
            result.append(str(beginNum))

        return result
