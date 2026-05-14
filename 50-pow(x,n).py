class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n<0:
            return self.myPow(1/x,-n)
        return x*self.myPow(x,n-1)
        

//better approach
class Solution:
    def findPow(self,x,n):
        if x==0:
            return 1
        a=self.findPow(x,n//2)
        if n%2==0:
            return a*a
        else:
            return a*a*x 

    def myPow(self, x: float, n: int) -> float:
        if n>0:
            return self.findPow(x,n)
        if n<0:
            return self.myPow(1/x,-n )
        return x*self.myPow(x,n-1)
        