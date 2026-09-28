class Solution(object):
    def longestOnes(self, nums, k):
        left = 0
        right = 0
        answer = 0
        z = 0 # number of zeroes 
        for right in range(len(nums)):
            if nums[right] == 0:
                z +=1
            while z>k:
                if nums[left]==0:
                    z-=1
                left+=1
            length = right-left+1
            answer=max(answer,length)
        return answer


        