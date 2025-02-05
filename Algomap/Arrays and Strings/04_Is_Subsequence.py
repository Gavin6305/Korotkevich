class Solution(object):
    def isSubsequence(self, s, t):
        # Account for edge cases
        if len(s) == 0:
            return True
        elif len(s) > len(t):
            return False
        
        # Keep taking away from s for each common encounter
        sub = s
        for c in t:
            if sub[0] == c:
                sub = sub[1:]
                if len(sub) == 0:
                    return True
        return False
