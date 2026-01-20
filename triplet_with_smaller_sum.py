from typing import List


class Solution:
    def countTriplets(self, n, sum, arr):
        arr.sort()
        print(arr)
        i = 0
        j = 1
        k = 2
        count = 0
        while k< len(arr):
            if arr[i] + arr[j]+ arr[k] < sum:
                count += 1
            else:
                j += 1
                k += 1


nums = [-2, 0, 1, 3]
obj = Solution()
res = obj.countTriplets(4, 2, nums)
print(res)