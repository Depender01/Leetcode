class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        window_sum = 0
        answer = float("inf")
        for right in range(len(nums)):
            window_sum +=nums[right]
           
            while window_sum >= target:
                length = right-left+1
                answer = min(answer,length)
                window_sum -= nums[left]
                left+=1
        if answer == float("inf"):
            return 0
        return answer
        

        
        