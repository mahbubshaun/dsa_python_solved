from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = n-1
            while j< k:
                if nums[j] + nums[k] == -nums[i]:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j< k and nums[j] == nums[j-1]:
                        j += 1
                    while j<k and nums[k] == nums[k+1]:
                        k -= 1
                elif nums[j] + nums[k] > -nums[i]:
                    k -= 1

                else:
                    j += 1
        return result

nums = [-2, 0, 1, 1, 2]
target = 9
sol = Solution()
result = sol.threeSum(nums)
print(result)