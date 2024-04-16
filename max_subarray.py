def maxSubArray(nums):
    maxSum = nums[0]
    currentSum = nums[0]
    start = 0
    end = 0
    tempStart = 0
    
    for i, num in enumerate(nums[1:], 1):
        if num > currentSum + num:
            tempStart = i
            currentSum = num
        else:
            currentSum += num
            
        if currentSum > maxSum:
            maxSum = currentSum
            start = tempStart
            end = i
    
    return nums[start:end + 1]

# Test the function
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maxSubArray = maxSubArray(nums)
maxSum = sum(maxSubArray)

print(f"Maximum Subarray: {maxSubArray}")
print(f"Maximum Subarray Sum: {maxSum}")
