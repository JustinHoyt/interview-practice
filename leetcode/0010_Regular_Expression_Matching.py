from typing import *

class Solution:
    def isMatch(self, phrase: str, regex: str) -> bool:
        memo = {}
        def has_kleene_star(regex_idx):
            return True if regex_idx + 1 < len(regex) and regex[regex_idx + 1] == '*' else False
        
        def only_kleene_stared_chars_from(regex_idx):
            while regex_idx < len(regex):
                if not has_kleene_star(regex_idx): return False
                regex_idx += 2
            return True

        def matches(phrase_idx, regex_idx):
            return phrase[phrase_idx] == regex[regex_idx] or regex[regex_idx] == '.'

        def match_rec(phrase_idx, regex_idx):
            key = (phrase_idx, regex_idx)
            match = False
            if key in memo:
                return memo[key]

            if regex_idx >= len(regex) and phrase_idx >= len(phrase): return True
            if regex_idx >= len(regex): return False
            if phrase_idx >= len(phrase): return only_kleene_stared_chars_from(regex_idx)

            if has_kleene_star(regex_idx):
                match_kleene_char = False
                if matches(phrase_idx, regex_idx):
                    match_kleene_char = match_rec(phrase_idx + 1, regex_idx)
                skip_kleene_char = match_rec(phrase_idx, regex_idx + 2)
                match = match_kleene_char or skip_kleene_char
            else:
                if matches(phrase_idx, regex_idx):
                    match = match_rec(phrase_idx + 1, regex_idx + 1)
                else:
                    match = False

            memo[key] = match
            return match

        return match_rec(0, 0)


def test_happy_path_matches():
    assert Solution().isMatch('ab', 'ab') == True

def test_simple_kleene_star_matches():
    assert Solution().isMatch('aaa', 'a*') == True

def test_simple_wildcard_with_kleene_star_matches():
    assert Solution().isMatch('ab', '.*') == True

def test_kleene_star_zero_matches_at_start():
    assert Solution().isMatch('aab', 'c*a*b') == True

def test_kleene_star_zero_matches_at_end():
    assert Solution().isMatch('aab', 'a*bc*d*e*') == True

def test_kleene_star_zero_matches_at_ends():
    assert Solution().isMatch('aab', 'c*a*bc*') == True

def test_empty_regex():
    assert Solution().isMatch('aab', '') == False

def test_empty_phrase():
    assert Solution().isMatch('', 'a') == False

def test_empty_phrase_and_regex():
    assert Solution().isMatch('', '') == True

def test_kleene_does_not_over_match():
    assert Solution().isMatch('aab', 'a*ab') == True

def test_runtime_speed():
    assert Solution().isMatch('aaaaaaaaaaaaaaaab', 'a*a*a*a*a*a*a*a*a*a*a*a*a*c') == False


if __name__ == "__main__":
    test_happy_path_matches()