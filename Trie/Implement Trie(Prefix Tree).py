# ^^^^^^^^^^^^^COPY^^^^^^^^^^^^^^^^^
#https://leetcode.com/problems/implement-trie-prefix-tree/submissions/ 
# https://www.youtube.com/watch?v=oobqoCJlHA0

#TO EVERY WORD INSERTED INTO THE TRIE WE WILL CREATE AN ARRAY OF 26 LENGTH EMPTY LIST
class TrieNode:
    def __init__(self):
        self.children=[None]*26 #for storing the 26 chars and their values
        self.endofword=False #this turns true if we reach character that is  end of the word 

        #inserting 'a' node in the childern will look like
        #children['a']=TrieNode() i.e. for each char we are creating a TireNode()

class Trie:
    def __init__(self):
        self.root=TrieNode() #creating the root node as a trienode we are gonna get rest of the node from this root node
    
    def insert(self,word):
        cur=self.root #initially start cur at the root
        for c in word:
            i = ord(c) - ord("a")
            if cur.children[i] == None: #if value at ith position of children is None 
                cur.children[i]=TrieNode() #then make children's ith position as TrieNode()
                #TO EVERY WORD INSERTED INTO THE TRIE WE WILL CREATE AN ARRAY OF 26 LENGTH EMPTY LIST
            cur=cur.children[i] #uf we already have some char at ith position in the array then directly make cur to that char at ith pos in the Trie
        cur.endofword= True #when we insert the last char of the word we make endofword as True to mark it
    
    def search(self,word):
        cur=self.root
        for c in word:
            i = ord(c) - ord("a")
            if cur.children[i] == None:
                return False #if any char c of word is not in children then return False
            cur=cur.children[i] #if c is present in word then move cur directly to that c
        return cur.endofword #after coming out of the loop now check if cur that is pointing to the 
        #last char of word right now is True if it is then return True

    def startswith(self,prefix):
        cur=self.root
        for c in prefix:
            i = ord(c) - ord("a")
            if cur.children[i] == None:
                return False
            cur=cur.children[i]#directly move to that char from where the prefix starts and check
            #for the whole prefix word through the loop
        return True #if the cur reaches to any position without getting false then return True
