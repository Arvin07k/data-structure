class Solution:
    def fib(self, n: int) -> int:
        r=0
        y=1
        for i in range(n):
            r,y=y,r+y
        return r
        


        
