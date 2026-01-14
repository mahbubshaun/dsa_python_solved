from typing import List


class Solution:
        def removeDuplicates(self, nums: List[int]) -> int:
            #Two pointer technique: fast and slow pointer
            #i will be responsible for uinique index, j will be responsibe for checking duplicates elements

            i = 1
            j = 1
            size = len(nums)
            while j < size:
                if nums[j] == nums [j-1]:
                    j += 1

                else:
                    #found the unique elements. replace i with j element, increase j

                    nums[i] = nums[j]
                    j += 1
                    i += 1
            return i




nums = [1,2]
obj = Solution()
res = obj.removeDuplicates(nums)
print(res)