class Solution:
    def gcd(self,a,b):
        if b==0:
            return a
        return self.gcd(b,a%b)
    def gcdOfOddEvenSums(self, n: int) -> int:
        oddSum=n*n
        evenSum=n*(n+1)
        return self.gcd(evenSum, oddSum)
        