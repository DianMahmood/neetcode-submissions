class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cS, cT = {}, {}
        for i in range(len(s)):
            cS[s[i]] = cS.get(s[i], 0) + 1
            cT[t[i]] = cT.get(t[i], 0) + 1
        for c in cS:
            if cS[c] != cT.get(c, 0):
                return False
        return True