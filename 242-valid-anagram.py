class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1={}
        if len(s)!=len(t):
            return False
        for ch in s:
            if ch in dict1:
                dict1[ch]+=1
            elif ch not in dict1:
                dict1[ch]=1
        for ch in t:
            if ch in dict1:
                dict1[ch]-=1
            elif ch not in dict1:
                return False
        for value in dict1.values():
            if value!=0:
                return False
        return True