class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mystack=[]
        result=[0]*len(temperatures)
        for i,temp in enumerate(temperatures):
            while mystack and temp>mystack[-1][0]:
                tempu,tempindex=mystack.pop()
                result[tempindex]=i-tempindex
            mystack.append([temp,i])
        return result
            

        
        