from timer import timer
from functools import cache


class Solution:
    @timer
    def longestStrChain(self, words: list[str]) -> int:
        word_set = set(words)

        @cache
        def longest_str_chain(word: str) -> int:
            if word not in word_set or word == '':
                return 0

            return max( (longest_str_chain(word[:i] + word[i+1:]) + 1 for i in range(len(word))) )

        return max(map(longest_str_chain, words))


def test_happy_path():
    assert Solution().longestStrChain(["a","b","ba","bca","bda","bdca"]) == 4
    assert Solution().longestStrChain(['xbc',"pcxbcf","xb","cxbc","pcxbc"]) == 5
    assert Solution().longestStrChain(["abcd","dbqca"]) == 1
    assert Solution().longestStrChain(["a"]) == 1


if __name__ == "__main__":
    test_happy_path()

