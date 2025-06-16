class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict={}
        r=0
        maxi=0
        for i in nums:
            dict[i]=1+dict.get(i,0)
            if dict[i] > maxi:
                result =i
            maxi=max(maxi,dict[i])
        return result


#BOYER-MOORE ALGO (O(1))        
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = 0
        count = 0
        for num in nums:
            if count == 0:
                result = num
            count += 1 if num == result else -1
        return result
