class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict1={}
        
        for ch in s:
            if ch in dict1:
                dict1[ch]+=1
            elif ch not in dict1:
                dict1[ch]=1
        for i in range(len(s)):
            if dict1[s[i]]==1:
                return i
            i+=1
        return -1
        