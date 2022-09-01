# Leetcode 208

# This is where we are initializing TrieNode
class TrieNode:
    def __init__(self):
        # children is the characters of words
        self.children = {}
        # end of word defines when the word ends
        self.endOfWord = False

# Lets create Trie data structure
class Trie:
    # first of all let's initialize it 
    def __init__(self):
        # as you can see self.root now has the TrieNode
        # kagebunshinno jutsu, right?
        self.root = TrieNode()

    # now we try to insert the word in the trie
    def insert(self, word: str) -> None:
        # let's initialize the TrieNode
        cur = self.root
        # simply go through every character of the word
        for c in word:
            # check if the character is in the children
            if c not in cur.children:
                # if it is not, then initialize it there
                cur.children[c] = TrieNode()
            # if it is, we just set last character to it
            cur = cur.children[c]
        # and set the endOfWord to be True
        cur.endOfWord = True

    # fun part, let's start searching inside the Trie
    def search(self, word: str) -> bool:
        # as always initialize it
        cur = self.root
        # now go through the word
        for c in word:
            # if it is not in our children
            if c not in cur.children:
                # return false (we don't have it)
                return False
            # otherwise set the last character to the cur
            cur = cur.children[c]
        # and now return cur.endOWord
        # it's False by default, if the word doesn't end there, it's still False
        # otherwise we return True
        return cur.endOfWord

    # starts with return true so long as we have that part in it
    def startsWith(self, prefix: str) -> bool:
        # as always initialize it
        cur = self.root
        # go through the prefix
        for c in prefix:
            # check if the prefix is in the children
            if c not in cur.children:
                # if not exists, return False
                return False
            # if it exists, set it to current children
            # so we would exit the loop
            cur = cur.children[c]
        # and return True
        return True
        