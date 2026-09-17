class Solution(object):
    def findMaxAverage(self, nums, k):
        n= len(nums)
        if k <=0 or k>n:
            return None
        window_sum = sum(nums[:k])
        best = window_sum
        for i in range(k,n):
            window_sum += nums[i]   # incoming element -- sum kra hai isko 
            window_sum -= nums[i-k] # outgoing element -- removed form the window 

            best = max(best,window_sum)
        avg=float(best)/k
        return avg
        