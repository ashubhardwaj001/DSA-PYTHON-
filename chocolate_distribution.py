def min_diff_chocolates(nums, m):
    nums.sort()  # Sort the array
    
    min_diff = float('inf')  # Initialize min_diff to infinity
    
    # Iterate through the first m elements in the sorted array
    for i in range(len(nums) - m + 1):
        diff = nums[i + m - 1] - nums[i]
        
        # Update min_diff if the difference is smaller
        if diff < min_diff:
            min_diff = diff
    
    return min_diff

# Test the function
nums = [7, 3, 2, 4, 9, 12, 56]
m = 3
print("Minimum difference:", min_diff_chocolates(nums, m))  # Output: Minimum difference: 2
