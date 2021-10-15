from typing import *

class Solution:
    def is_same_output(self, str1: str, str2: str):
        def next_char(word, idx):
            backspace_count = 0
            while idx >= 0 and (word[idx] == "<" or backspace_count > 0):
                backspace_count += 1 if word[idx] == "<" else -1
                idx -= 1

            return idx

        i = next_char(str1, len(str1) - 1)
        j = next_char(str2, len(str2) - 1)

        while i >= 0 and j >= 0:
            if str1[i] != str2[j]:
                return False

            i = next_char(str1, i-1)
            j = next_char(str2, j-1)

        return i == j

    # if working with a language with mutable strings.
    # python does not have this, so it is converted to a list to replicate the idea.
    def is_same_output_modify_in_place(self, str1: str, str2: str):
        str_list1 = list(str1)
        str_list2 = list(str2)
        pos = 0
        for i in range(len(str_list1)):
            if str_list1[i] == '<':
                pos -= 1
                pos = max(0,pos)
            else:
                str_list1[pos] = str_list1[i] 
                pos += 1

        pos = 0
        for i in range(len(str_list2)):
            if str_list2[i] == '<':
                pos -= 1
                pos = max(0,pos)
            else:
                str_list2[pos] = str_list2[i] 
                pos += 1
        
        return ''.join(str_list1[:pos]) == ''.join(str_list2[:pos])



def test_happy_path():
    assert Solution().is_same_output("world", "<<worrr<<ld") == True
    assert Solution().is_same_output("w<<i", "c<<irrr<<ld<<<") == True
    assert Solution().is_same_output("w<<i", "c<<irrr<<ldd<<<") == False
    assert Solution().is_same_output_modify_in_place("world", "<<worrr<<ld") == True
    assert Solution().is_same_output_modify_in_place("w<<i", "c<<irrr<<ld<<<") == True
    assert Solution().is_same_output_modify_in_place("w<<i", "c<<irrr<<ldd<<<") == False

def test_empty_case():
    assert Solution().is_same_output("", "<<wr<<") == True
    assert Solution().is_same_output("", "") == True
    assert Solution().is_same_output("", "a<<") == True
    assert Solution().is_same_output("", "<<<") == True
    assert Solution().is_same_output("<<<", "<<worrr<<ld") == False
    assert Solution().is_same_output_modify_in_place("", "<<wr<<") == True
    assert Solution().is_same_output_modify_in_place("", "") == True
    assert Solution().is_same_output_modify_in_place("", "a<<") == True
    assert Solution().is_same_output_modify_in_place("", "<<<") == True
    assert Solution().is_same_output_modify_in_place("<<<", "<<worrr<<ld") == False


if __name__ == "__main__":
    test_happy_path()
