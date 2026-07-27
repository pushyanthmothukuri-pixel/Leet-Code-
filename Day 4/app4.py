class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # Initialize the max_sum and current_sum with the first element
        max_sum = nums[0]
        current_sum = nums[0]
        
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # Decide whether to add the current number to the running sum, 
            # or start a new subarray from the current number
            current_sum = max(nums[i], current_sum + nums[i])
            
            # Update the global maximum sum if the current running sum is larger
            max_sum = max(max_sum, current_sum)
            
        return max_sum