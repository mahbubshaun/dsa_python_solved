class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        i = 0
        j= len(numbers) -1

        while(i < j):
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            if numbers[i] + numbers[j] > target:
                j = j-1
            if numbers[i] + numbers[j] < target:
                i = i+1
        return []




nums = [2, 7, 11, 15]
target = 9
sol = Solution()
result = sol.twoSum(nums, target)
print(result)

