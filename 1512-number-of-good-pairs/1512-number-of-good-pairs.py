class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        #okay so i imagine i will have to use a nested for loop
        #although i know that generally has comp complexity of O(n^2) so lets check if more efficient approach
        #okay brute force sol makes most sense to me so
        seenNums = {}
        count = 0
        for i in nums:
            count += seenNums.get(i, 0)
            seenNums[i] = seenNums.get(i,0) + 1 # same idea as the two for loops with one generally indexed a step befroe/after for comparing
        return count