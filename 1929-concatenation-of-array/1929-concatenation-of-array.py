class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        #going to keep computational complexity low - aprrox (O(n+n))
        answer = [] # intiialising my empty array
        for i in range (2): # running this twice 'concatenation of two nums array'
            for n in nums: # iterates through nums
                answer.append(n) # adds num to my empty array each time
        return (answer)