# how to solve any graphs problem 

# 1. describe the problem using graphs terminology 

# what are your nodes? 
# what are your edges? 
# are there connected components? 


# 2. build your graph OR define a get_neighbors function 

# 3. choose your graph algorithm and run 




# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that begin_word is not a transformed word.


# Step 1 : graph terminology 

# Nodes: words 
# Edges: 1- letter differences 

# Step2: build the graph
# get neighbord
# add vertices

# step3 choose algorithm 
# BFS shortest transformation sequence 

# read in the words 

import string 
f = open("words.text", 'r')

words = f.read().split('\n')
f.close()

word_set = set()

for word in words: 
    word_set.add(word.lower())

def get_neighbors(word): 

    neighbors = [] 
    # for every letter in the word: 
   
    # for every letter in the alphabet: 
    for i in range(len(word)):
        for alpha_letter in string.ascii_lowercase: 
    # swap out the word-letter with the alphabet letter
            # turn into a list
            word_list = list(word)
            word_list[i] = alpha_letter

            # turn the word list back into a string

            maybe_neighbor= "".join(word_list)

            if maybe_neighbor in word_set and maybe_neighbor != word:
                neighbors.append(maybe_neighbor)
    return neighbors 

    # if the new word is in our dictionary, then it is a neighbor
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


def find_ladders(start_word, end_word):
    # q
    # visited set 
    q = Queue()
    visited = set()
    q.enqueue([start_word])

    while q.size() > 0:
        current_path = q.dequeue()
        current_node = current_path[-1]

        if current_node == end_word:
            return current_path

        if current_node not in visited:
            neighbors = get_neighbors(current_node)

            for neighbor in neighbors:
                path_copy = list(current_path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)


promt(find_ladders("hit", "cog"))