class Solution:
    def countDigits(self, num: int) -> int:
        count=0
        temp=num
        while temp>0:
            r=temp%10
            if num%r==0:
                count+=1
            temp//=10
        return count