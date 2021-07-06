from typing import *

class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1:
            return s
        result = ''
        max_offset = (num_rows - 1) * 2
        offset_odd = max_offset
        offset_even = 0
        for row in range(min(num_rows, len(s))):
            prev_idx = row
            result += s[row]
            for i in range(1, len(s)):
                offset = offset_odd if (i % 2 == 1) else offset_even
                offset = max_offset if (row == 0 or row == num_rows - 1) else offset
                if prev_idx + offset >= len(s):
                    break
                result += s[prev_idx + offset]
                prev_idx += offset

            offset_odd -= 2
            offset_even += 2
        return result


def test_1_row():
    assert Solution().convert('PAYPALISHIRING', 1) == "PAYPALISHIRING"

def test_2_rows():
    assert Solution().convert('PAYPALISHIRING', 2) == "PYAIHRNAPLSIIG"

def test_3_rows():
    assert Solution().convert('PAYPALISHIRING', 3) == "PAHNAPLSIIGYIR"

def test_4_rows():
    assert Solution().convert('PAYPALISHIRING', 4) == "PINALSIGYAHRPI"

def test_5_rows():
    assert Solution().convert('PAYPALISHIRING', 5) == "PHASIYIRPLIGAN"

def test_6_rows():
    assert Solution().convert('PAYPALISHIRING', 6) == "PRAIIYHNPSGAIL"

def test_7_rows():
    assert Solution().convert('PAYPALISHIRING', 7) == "PNAIGYRPIAHLSI"

def test_100_rows():
    assert Solution().convert('PAYPALISHIRING', 100) == "PAYPALISHIRING"

if __name__ == "__main__":
    test_100_rows()