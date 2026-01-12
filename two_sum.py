from typing import List


class Solution:
    #O(N2)
    # time complexity O(N2)
    # Space Complexity O(1)
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     size = len(nums)
    #     for i in range(size):
    #         for j in range(i+1, size):
    #             if nums[i] + nums[j] == target:
    #                 return [i+1, j+1]
    #     return []

    # Two pointer Technique
    # time complexity O(N)
    # Space Complexity O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        size = len(numbers)
        i = 0
        j = size -1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            if numbers[i] + numbers[j] > target:
                j -= 1
            if numbers[i] + numbers[j] < target:
                i += 1
        return []


    #Alternative Technique: Binary Search - Pending



nums = [2,7, 11, 15]
obj = Solution()
res = obj.twoSum(nums, 9)
print(res)