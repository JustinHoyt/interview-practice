from typing import List, Tuple
from functools import reduce, partial

pipe = partial(reduce, lambda f, g: lambda x: g(f(x)))

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def get_next_line(start_idx) -> Tuple[int, List[str]]:
            line = ""
            for i in range(start_idx, len(words)):
                if len(words[i]) + len(line) > maxWidth:
                    return i, line.strip()

                line += f'{words[i]} '

            return -1, line.strip()


        def justify_line(line: str, is_final: bool) -> str:
            if is_final or len(line.split(' ')) == 1:
                return line + (' ' * (maxWidth - len(line)))

            result = ''
            num_words = len(line.split(' '))
            num_chars = len(''.join(line.split(' ')))
            num_whitespace = maxWidth - num_chars
            evenly_distributed_spaces = num_whitespace // (num_words - 1)
            leftover_spaces = num_whitespace % (num_words - 1)

            for i, word in enumerate(line.split(' ')):
                result += (word + ' ' * evenly_distributed_spaces)
                if leftover_spaces > 0:
                    result += ' '
                    leftover_spaces -= 1

            return result.strip()


        i = 0
        results = []
        while i != -1:
            i, line = get_next_line(i)
            final = i == -1
            results.append(justify_line(line, is_final=final))

        return results



def test_happy_path():
    assert Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16) == \
    [
       "This    is    an",
       "example  of text",
       "justification.  "
    ]


def test_last_line_left_justified():
    assert Solution().fullJustify(["What","must","be","acknowledgment","shall","be"], maxWidth = 16) == \
    [
      "What   must   be",
      "acknowledgment  ",
      "shall be        "
    ]


def test_single_word():
    assert Solution().fullJustify(["This"], maxWidth = 16) == \
    [
       "This            ",
    ]


def test_large_case():
    assert Solution().fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20) == \
    [
      "Science  is  what we",
      "understand      well",
      "enough to explain to",
      "a  computer.  Art is",
      "everything  else  we",
      "do                  "
    ]


if __name__ == "__main__":
    test_happy_path()

