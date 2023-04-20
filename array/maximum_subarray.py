class Solution:
    def maxSubArray(self, nums):
        # initializing maximum sum  of nums and current sum
        max_nums = nums[0]
        curr_sum = 0
        for i in nums:
            # avoiding negative sums
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += i
            # finding maximum amoung current sum and previous sum
            max_nums = max(max_nums, curr_sum)
        return max_nums