class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # I put the jewel types in a set so each membership check takes O(1) time
        jewel_set = set(jewels)

        # I go through every stone and count the ones whose type is in my jewel set.
        # Letters are case-sensitive, so 'a' and 'A' count as different types, and
        # the set comparison handles that with no extra work.
        count = 0
        for stone in stones:
            if stone in jewel_set:
                count += 1

        # I return how many of my stones are jewels
        return count