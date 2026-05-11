class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse=0
        temp=x
        while temp>0:
            r=temp%10
            temp//=10
            reverse= r+reverse*10

        return reverse==x