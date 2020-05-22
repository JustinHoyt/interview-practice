from collections import defaultdict

def is_member(words, query):
    for word in words:
        if is_match(query, word):
            return True

    return False

def is_match(query, word):
    if len(query) != len(word):
        return False

    for query_char, word_char in zip(query, word):
        if query_char != word_char and query_char != '*':
            return False

    return True

print(is_member(["foo", "bar", "baz"], "foo"))



class Dictionary:
    def __init__(self, words):
        self.trie = defaultdict(dict)
        [ self.add(word) for word in words ]

    def is_match(self, query):
        def word_match(node, idx=0):
            if idx == len(query):
                return "." in node

            letter = query[idx]
            if query[idx] == "*":
                return True in [ word_match(child, idx+1) for child in node.values() ]

            if letter not in node:
                return False

            return word_match(node[letter], idx+1)

        return word_match(self.trie)

    def add(self, word):
        curr = self.trie
        for idx, letter in enumerate(word):
            if letter not in curr:
                curr[letter] = {}

            curr = curr[letter]

        curr["."] = {}

dictionary = Dictionary(["foo", "bar", "baz"])
print(dictionary.is_match("foo"))
print(dictionary.is_match("f**"))
print(dictionary.is_match("f*o"))
print(dictionary.is_match("***"))
print(dictionary.is_match("*z*"))