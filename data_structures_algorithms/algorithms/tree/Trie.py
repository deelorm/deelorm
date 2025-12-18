
from math import e


class Trie_Node:
    def __init__(self, children={}):
        self.children = children
        self.end_of_string = False

class Trie:
    def __init__(self):
        self.root = Trie_Node()

    def insert_string(self, word):
        current_node = self.root 
        for bit in word:
            string_bit = bit 
            node = current_node.children.get(string_bit)
            if node == None:
                node = Trie_Node()
                current_node.children.update({string_bit:node})
            current_node = node 
        current_node.end_of_string = True
        print('Word Inserted..')

    def search_string(self, word):
        current_node = self.root 
        for bit in word:
            string_bit = bit 
            node = current_node.children.get(string_bit)
            if node == None:
                return False 
            current_node = node 
        if current_node.end_of_string == True:
            return True 
        else:
            return False

    def delete_string(self, root_node, word, index):
        if index > len(word)-1 or root_node is None:
            return 

        string_bit = word[index]
        current_node = root_node.children.get(string_bit)
        delete_cond = False

        if len(current_node.children) > 1:
            self.delete_string(current_node, word, index+1)
            return False 

        if index == len(word)-1:
            if len(current_node.children) >= 1:
                current_node.end_of_string = False 
                return False 
            else:
                root_node.children.pop(string_bit)
                return True 

        if current_node.end_of_string == True and len(current_node.children) > 1:
            self.delete_string(current_node, word, index+1)
            return False 
        # else:
        #     current_node.end_of_string = False
        #     return True

        delete_cond = self.delete_string(current_node, word, index+1)
        print(delete_cond)
        if delete_cond == True:
            root_node.children.pop(string_bit)
            return True
        else:
            return False





trie = Trie()
#trie.insert_string('API')
trie.insert_string('APP')

# print(trie.search_string('APP'))
trie.delete_string(trie.root, 'APP', 0)
#print(trie.search_string('APP'))
#print(trie.root.children['A'].children)


