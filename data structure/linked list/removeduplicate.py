class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=0
        fast=0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        second=0
        while True:
            slow=nums[slow]
            second=nums[second]
            if slow==second:
                return slow
#FLOYD ALGORITHM
        

        

