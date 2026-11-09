class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Put the jewel types in a set so each lookup is O(1).
        # Case matters ('a' and 'A' are different types), and sets compare exactly.
        jewel_set = set(jewels)

        # Go through every stone you have and count the ones whose type is a jewel.
        count = 0
        for s in stones:
            if s in jewel_set:
                count += 1
        return count