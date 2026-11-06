class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # My thought process:
        # The array is really two halves stuck together: the x's are nums[0..n-1]
        # and the y's are nums[n..2n-1]. The answer just alternates between them,
        # so x1, y1, x2, y2, ... For any position i, the x is at nums[i] and its
        # matching y is exactly n steps further along, at nums[i + n].
        #
        # How I approached it:
        # 1. Start with an empty result list.
        # 2. Loop i from 0 to n-1 (one pass over the first half).
        # 3. Each time, add nums[i] (the x) and then nums[i + n] (its paired y).
        # 4. Return the result. That's O(n) time and O(n) extra space for the output.

        res = []
        for i in range(n):
            res.append(nums[i])      # x_i from the first half
            res.append(nums[i + n])  # y_i from the second half, n positions later
        return res  