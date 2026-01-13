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
    #     for x in arr:
    #         if x == 0:
    #             total_0 += 1
    #
    #     #fill the array
    #     for i in range(size):
    #         if i < total_0:
    #             arr[i] = 0
    #         else:
    #             arr[i] = 1
    #
    #     return arr

    # Two pointer Technique attempt 1
    def segregate0and1(self, arr):
        # time complexity O(N)
        # Space Complexity O(1)
        size = len(arr)
        i = 0
        j = size -1
        while i < j:
            #Look fot misplaced 1s using i and 0s using j
            if arr[i] == 0:
                i += 1

            # keep moving j left if its value is 1
            elif arr[j] == 1:
                j -= 1
            #found misplaced i and j
            else:
                # Swap i and j
                # temp = arr[i]
                # arr[i] = arr[j]
                # arr[j] = temp
                #Pythonic swap elements
                arr[i], arr[j] = arr[j], arr[i]
                j -= 1
                i += 1
        return arr





nums = [0, 0, 1, 1, 0]
obj = Solution()
res = obj.segregate0and1(nums)
print(res)