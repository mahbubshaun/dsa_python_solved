from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []
        for i in range(n):
            j = i+1
            k = n-1
            while j< k:
                if nums[j] + nums[k] == -nums[i]:
                    result.append([nums[i], nums[j], nums[k]])
                    break
                if nums[j] + nums[k] > -nums[i]:
                    k -= 1

                if nums[j] + nums[k] < -nums[i]:
                    j += 1



        return result

nums = [0,0,0,0]
target = 9
sol = Solution()
result = sol.threeSum(nums)
print(result)