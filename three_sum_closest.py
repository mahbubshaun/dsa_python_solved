from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        closest_sum = 0
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = n-1
            while j< k:
                closest_sum = abs(target - (nums[j] + nums[k] + nums[i]))


                if closest_sum > target:
                    k -= 1

                else:
                    j += 1
        return closest_sum

nums = [-1,2,1,-4]
target = 9
sol = Solution()
result = sol.threeSumClosest(nums, 1)
print(result)