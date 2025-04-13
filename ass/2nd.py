def rotate(nums, k):
    n = len(nums)
    if n == 0 or k == 0:
        return nums
    k = k % n
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])
    return nums


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(rotate(nums, k))  # Output: [5, 6, 7, 1, 2, 3, 4]





def find_leaders(arr):
    leaders = []
    max_so_far = -float('inf')
    for num in reversed(arr):
        if num >= max_so_far:
            leaders.append(num)
            max_so_far = num
    return leaders[::-1]


arr = [16, 17, 4, 3, 5, 2]
print(find_leaders(arr))  # Output: [17, 5, 2]


def rotate_left(nums, k):
    n = len(nums)
    if n == 0 or k == 0:
        return nums
    k = k % n
    nums.reverse()
    nums[n - k:] = reversed(nums[n - k:])
    nums[:n - k] = reversed(nums[:n - k])
    return nums

nums = [3, 7, 8, 9, 10, 11]
k = 3
print(rotate_left(nums, k))  # Output: [9, 10, 11, 3, 7, 8]