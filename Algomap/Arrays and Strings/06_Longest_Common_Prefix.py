class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = ""
        prevPrefix = ""
        prefixLen = 0
        
        while True:
            for string in strs:
                # Return previous if first prefixLen chars does not match current common prefix
                if prefixLen > len(string) or string[:prefixLen] != prefix:
                    return prevPrefix

            # All strings contain prefix, so increase prefix length
            prevPrefix = prefix
            prefixLen += 1
            prefix = strs[0][:prefixLen]
        
        return prefix
