class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        if n==0:
            return 0
        max_len=1
        set1=set({})
        set1.add(s[0])
        i=0
        j=1
        while j <n :
            while s[j] in set1:
                set1.discard(s[i])
                i+=1
            set1.add(s[j])
            j+=1
            max_len=max(max_len,(j-i))
        return max_len