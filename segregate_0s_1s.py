class Solution:
    # def segregate0and1(self, arr):
    #     # Brute Force: Sort the array
    #     # time complexity O (N LOG N)
    #     # Space Complexity O(1)
    #     arr.sort()
    #     return arr

    # # Counting Technique
    # def segregate0and1(self, arr):
    #     # time complexity O(N)
    #     # Space Complexity O(1)
    #     size = len(arr)
    #     #Count 0s
    #     total_0 = 0
    #
    #     for i in range(size):
    #         if arr[i] == 0:
    #             total_0 += 1
    #
    #     #fill with 0s
    #     for i in range(total_0):
    #         arr[i] = 0
    #
    #     # fill with 1s
    #     for j in range(i +1, size):
    #         arr[j] = 1
    #
    #     return arr

    # Two pointer Technique
    def segregate0and1(self, arr):
        # time complexity O(N)
        # Space Complexity O(1)
        size = len(arr)
        i = 0
        j = size -1


        return arr





nums = [1, 1, 1, 1]
obj = Solution()
res = obj.segregate0and1(nums)
print(res)