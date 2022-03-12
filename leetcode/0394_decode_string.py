from typing import Tuple

class Solution:
    def decodeString(self, s: str) -> str:
        def _decode_string(idx = 0) -> Tuple[int, str]:
            result = ''
            while idx < len(s):
                if s[idx] == ']':
                    return idx, result
                elif s[idx].isalpha():
                    result += s[idx]
                    idx += 1
                else:
                    repeat_str = ''
                    while s[idx].isnumeric():
                        repeat_str += s[idx]
                        idx += 1

                    idx += 1 # skip '['
                    idx, substr = _decode_string(idx)
                    result += substr * int(repeat_str)
                    idx += 1 # skip ']'

            return idx, result


        _, decoded_str = _decode_string()
        return decoded_str


def test_happy_path():
    assert Solution().decodeString('ff3[a]2[bc]') == 'ffaaabcbc'
    assert Solution().decodeString('3[a2[bc]a]') == 'abcbcaabcbcaabcbca'


if __name__ == "__main__":
    test_happy_path()

