class Solution(object):
    def removeElement(self, nums, val):
        read =0
        write = 0
        while read < len(nums):
            if nums[read] != val:
                nums[write]=nums[read]
                write+=1
            read+=1
        return write 
        