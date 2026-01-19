from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        max_closest_sum = float('inf')
        current_closest = 0
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = n-1
            while j< k:
                current_sum = nums[j] + nums[k] + nums[i]
                if current_sum != 0:
                    current_closest = abs(target - current_sum)


                if current_closest < max_closest_sum:
                    max_closest_sum = current_closest


                if max_closest_sum > target:
                    k -= 1

                else:
                    j += 1
        return max_closest_sum

nums = [-1,2,1,-4]
target = 9
sol = Solution()
result = sol.threeSumClosest(nums, 1)
print(result)