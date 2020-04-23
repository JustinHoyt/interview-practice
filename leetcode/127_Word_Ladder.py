from collections import deque
from collections import defaultdict

class Solution1(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        queue = deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(Solution1().ladderLength(beginWord, endWord, wordList))

class Solution2(object):
    def findLadders(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        result = []
        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            newlayer = defaultdict(list)
            for word in layer:
                if word == endWord:
                    result.extend(k for k in layer[word])
                else:
                    for i in range(len(word)):
                        for char in 'abcdefghijklmnopqrstuvwxyz':
                            new_word = word[:i] + char + word[i+1:]
                            if new_word in wordList:
                                newlayer[new_word]+=[tmp_word + [new_word] for tmp_word in layer[word]]

            wordList -= set(newlayer.keys())
            layer = newlayer

        return result

print(Solution2().findLadders(beginWord, endWord, wordList))