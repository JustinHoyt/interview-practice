class Solution:
    def generateParenthesis(self, num_pairs):
        ans = []

        def backtrack(parens_string = '', left_count = 0, right_count = 0):
            if len(parens_string) == 2 * num_pairs:
                ans.append(parens_string)
                return

            if left_count < num_pairs:
                backtrack(parens_string + '(', left_count + 1, right_count)
            if left_count > right_count:
                backtrack(parens_string + ')', left_count, right_count + 1)

        backtrack()
        return ans


def test_happy_path():
    assert sorted(Solution().generateParenthesis(3)) == sorted(['()()()', '(()())', '(())()', '((()))', '()(())'])

def test_four():
    assert sorted(Solution().generateParenthesis(4)) == sorted(["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
)

if __name__ == "__main__":
    test_happy_path()

