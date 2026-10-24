'''
accounts = [[1,2,3],[3,2,1]]
so we have 2 customers represented by the two arrays
for loop - to sum up each array
then maybe an if/else comparing the arrays
'''

class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        maxwealth = 0 #intialising our comparison value holder
        for i in range(len(accounts)): # iterates through entire accounts
            totalwealth = sum(accounts[i]) # for each account fins total wealth
            maxwealth = max(maxwealth, totalwealth) #checks maxwealth versus current total weatlh
        return maxwealth # outputs the highest value of either our maxwealth or newly assigned max wealth