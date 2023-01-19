from typing import List

def is_target_left_side(nums: List[int], start_index: int, end_index: int, target: int, middle: int) -> bool:
    return ((nums[start_index] <= nums[middle]) and (nums[start_index] <= target < nums[middle])) \
    or ((nums[start_index] <= nums[middle]) == False) and ((nums[middle] < target <= nums[end_index]) == False)

def broken_search(nums: List[int], target: int) -> int:
    start_index: int = 0
    end_index: int = len(nums) - 1
    while start_index <= end_index:
        middle: int = (start_index + end_index) // 2
        if nums[middle] == target:
            return middle
        elif is_target_left_side(nums, start_index, end_index, target, middle):
            end_index = middle - 1
        else:
            start_index = middle + 1
    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6