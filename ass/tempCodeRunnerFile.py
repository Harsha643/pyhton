def rotate_left(nums, k):
    n = len(nums)
    if n == 0 or k == 0:
        return nums
    k = k % n
    nums.reverse()
    nums[n - k:] = reversed(nums[n - k:])
    nums[:n - k] = reversed(nums[:n - k])
    return nums

# Example usage:
nums = [3, 7, 8, 9, 10, 11]
k = 3
print(rotate_left(nums, k))  # Output: [9, 10, 11, 3, 7, 8]