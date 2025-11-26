class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        max_count = 0
        for x in nums:
            if x == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
        return max_count




list = [1,1,0,1,1,1]
s = Solution()
print(s.findMaxConsecutiveOnes(list))

#
# time complexity: 0(n)
#
# space complexity: 0(1)
#
# What is space complexity?
#
# It measures extra memory your algorithm uses in addition to the input.
#
# Input nums is given (not counted).
#
# We only consider new variables/structures created inside the function.
#
# Space usage in this code:
#
# count → just one integer
#
# max_count → just one integer
#
# x (loop variable) → one integer at a time, reused
#
# No arrays, no hash maps, no recursion stack (no extra memory growing with n).
#
# So the memory required does not depend on the size of nums. Whether nums has 10 elements or 10 million, you’re still using just a few fixed variables.
#
# Therefore:
#
# Auxiliary space = O(1) (constant space).
#
# Time complexity = O(n) (you must check each element once).