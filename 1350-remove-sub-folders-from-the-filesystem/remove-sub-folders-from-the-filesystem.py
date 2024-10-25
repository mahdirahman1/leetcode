class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert_folder(self, folder):
        curr = self.root
        for fd in folder:
            if fd not in curr.children:
                curr.children[fd] = TrieNode()
            curr = curr.children[fd]
        curr.endFolder = True

    def remove_subfolders(self):
        self.res = []
        curr = self.root
        def dfs(node, curr):
            if node.endFolder:
                self.res.append("".join(curr))
                return
            
            for sub in node.children:
                new_ = curr.copy()
                new_.append("/"+sub)
                dfs(node.children[sub], new_)
        
        dfs(curr, [])
        return self.res

class TrieNode:
    def __init__(self, endFolder = False):
        self.endFolder = endFolder
        # dictionary, key = folder name, value = TrieNode
        self.children = defaultdict(TrieNode)

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # use a trie to store the folder structure
        # if a folder ends, set a Flag
        # after adding all folders to the trie, do a dfs and add shortest folders
        # i.e first time you see a folder end, add that to answer and continue dfs
        for i, fd in enumerate(folder):
            folder[i] = fd.split("/")[1:]
        
        trie = Trie()
        # insert all folders in the trie
        for fd in folder:
            trie.insert_folder(fd)

        # get subfolders using trie
        return trie.remove_subfolders()

