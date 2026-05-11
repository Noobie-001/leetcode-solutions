class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product=1
        sum=0
        temp=n 
        while temp>0:
            r=temp%10
            sum=r+sum
            product=product*r
            temp//=10
        return (product-sum)
        