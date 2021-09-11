from typing import *

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def addBinaryRec(a, b):
            if b == 0: return a

            temp_result = a ^ b
            carry = (a & b) << 1
            
            return addBinaryRec(temp_result, carry)
        
        return bin(addBinaryRec(int(a, 2), int(b, 2)))[2:]

def test_happy_path():
    assert Solution().addBinary('1101', '0111') == '10100'


if __name__ == "__main__":
    test_happy_path()