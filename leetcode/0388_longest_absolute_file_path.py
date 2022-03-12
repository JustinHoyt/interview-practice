from collections import defaultdict
from typing import Tuple, Dict

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        root = defaultdict(dict)
        tokens = input.split('\n')

        longest_length = 0
        def length_longest_path(curr: Dict[str, Dict], token_idx=0, depth=-1, sofar='') -> Tuple[int, int]:
            nonlocal longest_length
            if '.' in sofar:
                longest_length = max(len(sofar), longest_length)

            while token_idx < len(tokens) and depth + 1 == tokens[token_idx].count('\t'):
                stripped_token = tokens[token_idx].strip('\t')
                curr[stripped_token] = {}
                depth, token_idx = length_longest_path(curr[stripped_token], token_idx + 1, depth + 1, f'{sofar}/{stripped_token}')

            return depth - 1, token_idx


        length_longest_path(root)
        return longest_length - 1 if longest_length > 0 else 0


def test_happy_path():
    assert Solution().lengthLongestPath('dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext') == 32


def test_single_dir():
    assert Solution().lengthLongestPath('dir') == 0


if __name__ == "__main__":
    test_happy_path()

