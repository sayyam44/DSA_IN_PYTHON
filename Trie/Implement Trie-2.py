# ^^^^^^^^^^^^^^^^^^COPY^^^^^^^^^^^^^^^^^^^^
# https://www.youtube.com/watch?v=K5pcpkEMCN0&list=PLgUwDviBIf0pcIDCZnxhv0LkHf5KzG9zp&index=2
# https://github.com/kamyu104/LeetCode-Solutions/blob/master/Python/implement-trie-ii-prefix-tree.py
# implement the following 
# 1) Trie(): Ninja has to initialize the object of this “TRIE” data structure.

# 2) insert(“WORD”): Ninja has to insert the string “WORD”  into this “TRIE” data structure.

# 3) countWordsEqualTo(“WORD”): Ninja has to return how many times this “WORD” is present in this “TRIE”.

# 4) countWordsStartingWith(“PREFIX”): Ninjas have to return how many words are there in this “TRIE” that have the string “PREFIX” as a prefix.

# 5) erase(“WORD”): Ninja has to delete one occurrence of the string “WORD” from the “TRIE”.


from sympy import root
import wordcloud


class TrieNode:
    def __init__(self):
        self.children=[None]*26
        self.ew=0
        self.cp=0

class Trie:
    def __init__(self):
        self.root=TrieNode()
    
    def insert(self,word):
        cur=self.root()
        # cur.cp+=1 #increasing the cp of root by 1
        for c in word:
            i=ord('a')-ord(c)
            if cur.children[i]==None:
                cur.children[i]=TrieNode()
            cur=cur.children[i]
            cur.cp+=1 #increasin count of prefix by 1 
        cur.ew+=1

    def countWordsEqualTo(self, word):
        cur=self.root()
        for c in word:
            i=ord('a')-ord(c)
            if cur.children[i]==None:
                return 0
            cur=cur.children[i]
        return cur.ew
    
    def countWordsStartingWith(self, word):
        cur=self.root()
        for c in word:
            i=ord('a')-ord(c)
            if cur.children[i]==None:
                return 0
            cur=cur.children[i]
        return cur.cp
    
    def erase(self, word):
        cnt=self.countWordsEqualTo( word)
        if not cnt:
            return 
        cur=self.root()
        # cur.cp-=1 #decreasing the cp of root by 1
        for c in word:
            i=ord('a')-ord(c)
            if cur.children[i].cp==1: #if some char's cp == 1 then we will have to make its cp as none and return none
                cur.children[i]=None
                return
            cur=cur.children[i] #if some char's cp > 1 then directly make that char as cur char
            cur.cp-=1 #then decrease its count of prefix by 1 
        cur.ew-=1#decreasing the ew endwith by 1 at the end of the loop



            

