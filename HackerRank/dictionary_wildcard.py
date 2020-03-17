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


class TrieNode:
    def __init__(self, last_letter=False):
        self.children = defaultdict(TrieNode)
        self.last_letter = last_letter

class Dictionary:
    def __init__(self, words):
        self.trie = TrieNode()
        [ self.add(word) for word in words ]
        
    def is_match(self, query):

        def word_match(node, idx=0):
            letter = query[idx]
            if idx == len(query) - 1:
                if letter == "*":
                    return len(node.children) > 0

                return node.children[letter].last_letter
            
            if query[idx] == "*":
                return True in [ word_match(child, idx+1) for child in node.children.values() ]

            if letter not in node.children:
                return False

            return word_match(node.children[letter], idx+1)
            
        return word_match(self.trie)

    def add(self, word):
        curr = self.trie
        for idx, letter in enumerate(word):
            if letter not in curr.children:
                curr.children[letter] = TrieNode()

            if idx == len(word) - 1:
                curr.children[letter].last_letter = True
            
            curr = curr.children[letter]

dictionary = Dictionary(["foo", "bar", "baz"])
print(dictionary.is_match("foo"))
print(dictionary.is_match("f**"))
print(dictionary.is_match("f*o"))
print(dictionary.is_match("***"))
print(dictionary.is_match("*z*"))