# https://leetcode.com/problems/design-add-and-search-words-data-structure/
# https://www.youtube.com/watch?v=BTf05gs_8iU
class TrieNode:
    def __init__(self):
        self.children={} #a:Trienode
        self.word=False #marker

class WordDictionary:
    def __init__(self):
        self.root=TrieNode()
    
    def addWord(self, word: str) -> None:
        cur=self.root
        for i in word:
            if i not in cur.children:
                cur.children[i]=TrieNode()
            cur=cur.children[i]
        cur.word=True
    
    def search(self, word: str) -> bool:
        def dfs(j,root):
            cur=root
            for i in range(j,len(word)): #j becasue we want to start from the index where the dot began
                c=word[i]
                if c=='.': #recursion by dfs if we have a dot
                    for child in cur.children.values(): #here cur.children.values() gives the characters 
                        if dfs(i+1,child): #i+1 starting index from where the dot begins #child tells tha which node we are iterating through right now 
                            return True
                        return False

                
                else:
                    if c not in cur.children:
                        return False
                    cur=cur.children[c]
            return cur.word #if cur.word is true then only return true
        retrun dfs(0,self.root)


