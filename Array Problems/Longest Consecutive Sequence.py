class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq=set(nums) # Converted to sets

        res=0
        for i in nums:
            j=i #Storing the value in J so that we can increment and check consecutive ones
            if j-1 not in uniq:
                while j in uniq:
                    j=j+1
                res=max(res,j-i)      #Difference gives us the consecutive count
        return res