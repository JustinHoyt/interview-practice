class Trie:
    def __init__(self):
        self.letter_node = {}

    def contains(self, url):
        current_node = self.letter_node
        for letter in url:
            if letter not in current_node:
                return False
            else:
                current_node = current_node[letter]
        if "end" in current_node:
            return True
        else:
            return False

    def insert(self, url):
        current_node = self.letter_node
        for letter in url:
            if letter not in current_node:
                current_node[letter] = {}
            current_node = current_node[letter]
        current_node["end"] = {}

    def search_if_not_visited(self, url):
        if self.contains(url):
            print("already searched")
        else:
            print("searching!")
            self.insert(url)


trie = Trie()
trie.search_if_not_visited("www.google.com/images")
trie.search_if_not_visited("www.google.com")
trie.search_if_not_visited("www.google.com")
trie.search_if_not_visited("www.docs.google.cotrie.search_if_not_visited()")
trie.search_if_not_visited("www.youtube.com/video")
trie.search_if_not_visited("www.youtube.com")
