'''
Given a string T, the idea is to decompose it into a list of substrings called phrases.
these phrases follow three rules:
1. The concatenation of all of them is the original string T.
2. Every new phrase is either:
  a. A single character
  b. A previously seen phrase, or:
  c. A previously seen phrase with a single character appended to it
3. Each new phrase is as long as possible

Examples:
"goooooogle" -> ["g", "o", "oo", "ooo", "gl", "e"]
"banana" -> ["b", "a", "n", "an", "a"]
"lalaland" -> ["l", "a", "la", "lan", "d"]
"lalala" ->["l", "a", "la", "la"]

Interesting edge cases:
- string can be length 0
- there may be duplicates in the result list
'''

def add_to_trie_suboptimal(phrase, trie):
    curr = trie
    for letter in phrase:
        if letter in curr:
            curr = curr[letter]
        else:
            curr[letter] = {}
            return True

    return False

def generate_phrases_suboptimal(word):
    trie = {}
    phrases = []

    i = 0
    while i < len(word):
        phrase = ""
        is_valid = True

        while is_valid and i < len(word):
            phrase = phrase + word[i]
            if add_to_trie(phrase, trie):
                phrases.append(phrase)
                is_valid = False
            i += 1
    return phrases


def add_to_trie(word, idx, trie):
    is_valid_prefix = True
    while is_valid_prefix and idx < len(word):
        if word[idx] in trie:
            trie = trie[word[idx]]
        else:
            trie[word[idx]] = {}
            is_valid_prefix = False
        idx += 1

    return idx

def generate_phrases(word):
    trie = {}
    phrases = []

    i = 0
    while i < len(word):
        end_idx = add_to_trie(word, i, trie)
        phrases.append(word[i:end_idx])
        i = end_idx

    return phrases

print(generate_phrases("lalaland"))
print(generate_phrases("lalala"))
print(generate_phrases(""))