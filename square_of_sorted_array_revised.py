from typing import List


class Solution:
        def sortedSquares(self, nums: List[int]) -> List[int]:
            size = len(nums)
            i = 0
            j = size -1
            result = [None] * size
            counter = 1

            #if the size 1, just return the squared result array
            if size == 1:
                result[0] = nums[0] * nums[0]
                return result

            # Run loop until j and i cross
            while j> i:
                squared_i = nums[i] * nums[i]
                squared_j = nums[j] * nums[j]
                if squared_i < squared_j:
                    result[size-counter] = squared_j
                    j -= 1
                    counter +=1
                else:
                    result[size-counter] = squared_i
                    counter += 1
                    i +=1
            if squared_i < squared_j:
                result[size - counter] = squared_i
            else:
                result[size-counter] = squared_j
            return result






nums = [1]
sol = Solution()
result = sol.sortedSquares(nums)
print(result)