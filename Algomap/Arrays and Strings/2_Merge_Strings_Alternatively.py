class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = ""
        i = 0
        while True:
            # len1 > len2
            if len(word1) > len(word2):
                if i < len(word2):
                    result += word1[i]
                    result += word2[i]
                else:
                    result += word1[-(len(word1) - i):]
                    return result

            # len1 < len2
            elif len(word1) < len(word2):
                if i < len(word1):
                    result += word1[i]
                    result += word2[i]
                else:
                    result += word2[-(len(word2) - i):]
                    return result

            # len1 == len2
            else:
                if i < len(word1):
                    result += word1[i]
                    result += word2[i]
                else:
                    return result
            
            i += 1
        return None
