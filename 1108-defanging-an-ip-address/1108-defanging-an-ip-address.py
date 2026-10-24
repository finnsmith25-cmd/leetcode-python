class Solution:
    def defangIPaddr(self, address: str) -> str:
        myaddress = address.replace('.', '[.]')
        return myaddress