# https://leetcode.com/problems/implement-trie-prefix-tree/

"""
+ We are going to use nested dictionary
    + When I add new word, we add it in nested loop and ends with '.'
    + When I move deeper in dictionary -> assin value to current dictionary

    + When I am working with prefix function, I need to check every
character in word in nested dictionary or not. If it ends with '.'
character => True

Space complexity: O(N): N is length of word inserted
Time complexity: O(N): N is length of word inserted
"""

class Trie:

    def __init__(self):
        self.trie = {}    

    def insert(self, word: str) -> None:
        d = self.trie

        for c in word:
            if c not in d:
                d[c] = {}

            d = d[c]

        d['.'] = '.'

    def search(self, word: str) -> bool:
        d = self.trie

        for c in word:
            if c not in d:
                return False

            d = d[c]

        return '.' in d


    def startsWith(self, prefix: str) -> bool:
        d = self.trie

        for c in prefix:
            if c not in d:
                return False

            d = d[c]

        return True

        
# d = {
#     a: {
#         p: {
#             p: {
#                 l: {
#                     e: {
#                         .
#                     }
#                 },
#                 m: {
#                     e: {
#                         .
#                     }
#                 }
#             }
#         }
#     }
# }

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)