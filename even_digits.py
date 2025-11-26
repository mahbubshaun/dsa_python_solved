class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_even_digits = 0
        for x in nums:
            digits = len(str(abs(x)))
            if digits % 2 == 0:
                max_even_digits += 1
        return max_even_digits


list = [555,901,482,1771]
s = Solution()
print(s.findNumbers(list))