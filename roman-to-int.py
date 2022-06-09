class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        if len(s) > 15:
            print("Error. The input roman number must be between 1 and 15")
            return
        if any(c not in "IVXLCDM" for c in s):
            print("Error. The input roman number must contains only the follow letters: I, V, X, L, C, D, M")
            return
        for i in range(len(s)):
            if i == len(s)-1:
                if s[i] in "I":
                    num += 1
                elif s[i] in "V":
                    num += 5
                elif s[i] in "X":
                    num += 10
                elif s[i] in "L":
                    num += 50
                elif s[i] in "C":
                    num += 100
                elif s[i] in "D":
                    num += 500
                else:
                    num += 1000
            elif s[i] in "M":
                num += 1000
            elif s[i] in "D":
                num += 500
            elif s[i] in "C" and s[i + 1] not in "DM":
                num += 100
            elif s[i] in "C" and s[i + 1] in "DM":
                num -= 100
            elif s[i] in "L":
                num += 50
            elif s[i] in "X" and s[i + 1] not in "LC":
                num += 10
            elif s[i] in "X" and s[i + 1] in "LC":
                num -= 10
            elif s[i] in "V":
                num += 5
            elif s[i] in "I" and s[i + 1] not in "VX":
                num += 1
            else:
                num -= 1
        return num


sol = Solution()
result = sol.romanToInt("")

print(result)
