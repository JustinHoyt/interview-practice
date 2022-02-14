from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        if len(strs) == 0:
            return prefix

        for idx, letter in enumerate(strs[0]):
            for word in strs:
                if idx >= len(word) or word[idx] != letter:
                    return prefix

            prefix += letter

        return prefix


def test_happy_path():
    assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == "fl"


def no_match():
    assert Solution().longestCommonPrefix(["flower", "low", "flight"]) == ""


def match_to_end():
    assert Solution().longestCommonPrefix(["flower", "flow", "flowers"]) == "flow"


if __name__ == "__main__":
    test_happy_path()
