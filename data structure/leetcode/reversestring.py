class Solution:
    def reverseString(self, s: List[str]) -> None:
        self.recstring(s,0,len(s)-1)

    def recstring(self,s,start,end):
        if start>end:
            return
        s[start],s[end]=s[end],s[start]
        self.recstring(s,start+1,end-1)

