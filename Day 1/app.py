class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Dictionary to store the numbers we've seen and their indices
        # Format: {number: index}
        num_map = {} 
        
        for i, num in enumerate(nums):
            # Calculate the number we need to reach the target
            complement = target - num 
            
            # Check if we have already seen this complement
            if complement in num_map:
                # If yes, return the index of the complement and the current index
                return [num_map[complement], i]
            
            # Otherwise, "remember" this number and its index for future iterations
            num_map[num] = i
            
        return [] # Return empty list if no solution is found (though the problem guarantees one)