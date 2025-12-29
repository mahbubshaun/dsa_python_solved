class Solution(object):
    def removeDuplicates(self, nums):
        i = j =1
        n = len(nums)
        while(j<n):
            if (nums[j] == nums[j-1]):
                j += 1
                continue
            nums[i] = nums[j]
            i += 1
            j+=1
        return i










nums = [1,2]
target = 9
sol = Solution()
result = sol.removeDuplicates(nums)
print(result)