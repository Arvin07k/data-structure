class Solution:
    def calPoints(self, operations: List[str]) -> int:
        mystack=[]
        for r in operations:
            if r == "C":
                mystack.pop()
            elif r=="+":
                mystack.append(mystack[-1]+mystack[-2])
            elif r=="D":
                mystack.append(mystack[-1]*2)
            else:
                mystack.append(int(r))
        return sum(mystack)