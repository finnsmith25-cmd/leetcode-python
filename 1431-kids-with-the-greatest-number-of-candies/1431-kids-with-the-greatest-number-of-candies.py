class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Find the most candies any kid has right now.
        # This is the number each kid has to reach (ties count).
        max_candies = max(candies)

        # Give each kid all the extra candies and check if they reach the max.
        # The other kids' counts don't change, so the current max is the only target.
        return [c + extraCandies >= max_candies for c in candies]