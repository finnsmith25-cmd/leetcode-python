class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        
        counter = 0 #this will store my sum each iteration
        list = []

        for i in nums:
            counter = i + counter #here we will at array point [i] to our sum
            list.append(counter)#adds to our array list
        return(list) # this returns our summation list for each iteration

