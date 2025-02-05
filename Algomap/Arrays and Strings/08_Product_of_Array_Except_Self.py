class Solution(object):
    def productExceptSelf(self, nums):
        output = []
        
        # Prefixes
        prefixProduct = 1
        for i in range(len(nums)):
            output.append(prefixProduct)
            prefixProduct *= nums[i]
        
        # Suffixes
        suffixProduct = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= suffixProduct
            suffixProduct *= nums[i]

        return output
