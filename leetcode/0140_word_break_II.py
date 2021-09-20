from collections import defaultdict
from typing import *
import math

class Solution:
    def wordBreak(self, phrase: str, wordDict: List[str]) -> List[str]:
        phrases: List[str] = []
        trie: Dict[str, Dict] = {}
        END = '.'

        def build_trie():
            nonlocal trie
            for word in wordDict:
                curr = trie
                for letter in word:
                    curr = curr.setdefault(letter, {})
                curr[END] = {}


        def build_phrase(node, i, sofar):
            nonlocal trie, phrases
            node = trie
            while i < len(phrase):
                letter = phrase[i]
                if letter in node:
                    node = node.get(letter)
                    sofar += letter
                else:
                    return

                if END in node:
                    if i == len(phrase) - 1:
                        phrases.append(sofar)
                        return
                    build_phrase(node, i + 1, sofar + ' ')
                i += 1


        build_trie()
        build_phrase(trie, 0, '')

        return phrases


def test_happy_path():
    assert sorted(Solution().wordBreak( "catsanddog", ["cat","cats","and","sand","dog"])) == sorted(["cat sand dog","cats and dog"])

def test_subwords():
    assert sorted(Solution().wordBreak( "pineapplepenapple", ["apple","pen","applepen","pine","pineapple"])) == sorted(["pine apple pen apple","pineapple pen apple","pine applepen apple"])

def test_no_results():
    assert Solution().wordBreak( "catsandog", ["cats","dog","sand","and","cat"]) == []


if __name__ == "__main__":
    test_happy_path()