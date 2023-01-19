def broken_search(nums, target) -> int:
    start_index = 0
    end_index = len(nums) - 1
    while start_index <= end_index:
        middle = (start_index + end_index) // 2
        if nums[middle] == target:
            return middle
        elif ((nums[middle] < target <= nums[end_index]) == False) or (nums[start_index] <= target < nums[middle]):
            end_index = middle - 1
        else:
            start_index = middle + 1
    return -1


"""def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6"""

n = 2
target = 1
nums = [5, 1]
print(broken_search(nums, target))