class Solution:
    from typing import List

    def sortedSquares(self, nums: List[int]) -> List[int]:
        siz = len(nums) #0(1)
        neg = [] #0(1)
        pos = [] #0(1)

        #seperate postitive and negative  #0(n)
        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)

        #case 1: no negative numbers  #0(n)
        if len(neg) == 0:
            return [x * x for x in pos]

        #case 2: no positive numbers #0(n)
        if len(pos) == 0:
            res = [x *x for x in neg]
            res.reverse()
            return res
        #case 3: both exist
        neg = [x *x for x in neg][::-1] #sq, reverse #0(n)
        pos = [x *x for x in pos] #sq #0(n)

        n,m = len(neg), len(pos) #0(1)
        res = [] #0(1)

        #id

        i = j =0 #0(1)
        while i< n and j<m: #0(n)
            if neg[i] <= pos[j]:
                res.append(neg[i])
                i += 1
            else:
                res.append(pos[i])

        while i<n: #0(n)
            res.append(neg[i])
            i += 1

        while j<m:
            res.append(pos[j])
            j +=1
        return res


#time complexity is 0(n)

