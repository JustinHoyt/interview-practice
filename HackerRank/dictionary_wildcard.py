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
