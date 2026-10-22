# Pattern: simulation / modulo checks, O(n) time, O(n) space
# My first submission, testing that LeetHub pushes to GitHub correctly.

class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        answer = []
        # I loop from 1 to n inclusive, since the output is 1-indexed
        for i in range(1, n + 1):
            # I check 15 first, otherwise multiples of 15 would stop at "Fizz"
            if i % 15 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer