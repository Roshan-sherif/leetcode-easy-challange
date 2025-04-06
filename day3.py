class Solution(object):
    def findMaxAverage(self, nums, k):
        maximum_avg=float('-inf')
        for i in range(len(nums)-k+1):
            window= nums[i:i+k]
            current_avg= sum(window)/4
            maximum_avg=max(maximum_avg,current_avg)
        return maximum_avg    