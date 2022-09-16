from typing import *


def nextPermutation(nums: List[int]) -> None:
    # 这个是根据题解里面的算法 进行复现的
    n = len(nums)
    i = -1
    for j in range(n - 1, 0, -1):
        if nums[j - 1] < nums[j]:
            i = j - 1
            break
    if i == -1:
        nums.reverse()
        return
    for j in range(n - 1, i, -1):
        if nums[j] > nums[i]:
            break
    nums[i], nums[j] = nums[j], nums[i]
    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[left], nums[right]
        left += 1
        right -= 1

