class Solution(object):
    def romanToInt(self, s):
        # dict for symbol values
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        result = 0
        
        i = 0

        # Loop through s
        while i < len(s):
            # current symbol
            currentSym = s[i]
            # next symbol
            nextSym = s[i+1] if i + 1 < len(s) else None

            # I before V and X
            if currentSym == 'I' and (nextSym == 'V' or nextSym == 'X'):
                result += values[nextSym] - values[currentSym]
                i += 1
                
            # X before L and C
            elif currentSym == 'X' and (nextSym == 'L' or nextSym == 'C'):
                result += values[nextSym] - values[currentSym]
                i += 1
            
            # C before D and M
            elif currentSym == 'C' and (nextSym == 'D' or nextSym == 'M'):
                result += values[nextSym] - values[currentSym]
                i += 1

            # In order
            else:
                result += values[currentSym]
            
            i += 1
          
        return result
