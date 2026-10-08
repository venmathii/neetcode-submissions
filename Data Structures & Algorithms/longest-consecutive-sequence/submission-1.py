class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        result=0
        for i in s:
            length=1
            current=i
            if current-1 not in s:
              while current+1 in s:
                current=current+1
                length=length+1
              result=max(length,result)
        return result


          