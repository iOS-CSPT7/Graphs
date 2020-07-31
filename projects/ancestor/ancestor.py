
import collections 


# class Stack():
#     def __init__(self):
#         self.stack = []
#     def push(self, value):
#         self.stack.append(value)
#     def pop(self):
#         if self.size() > 0:
#             return self.stack.pop()
#         else:
#             return None
#     def size(self):
#         return len(self.stack)


# def earliest_ancestor(ancestors, starting_node):
#     parents_by_child = {} 
    
#     for parent, child in ancestors:
#         if child in parents_by_child:
#             parents_by_child[child].append(parent)
#         else: 
#             parents_by_child[child] = [parent]
    
#     if starting_node not in parents_by_child:
#         return - 1

#     path_queue = collections.deque()

#     last_path = [starting_node]

#     path_queue.append(last_path)

#     while len(path_queue) > 0:
#         last_path = path_queue.popleft()
#         oldest_ancestor = last_path[-1]

#         if oldest_ancestor in parents_by_child:
#             parents_by_child[oldest_ancestor].sort(reverse=True)
#             for parent in parents_by_child[oldest_ancestor]:
#                 new_path = last_path.copy()
#                 new_path.append(parent)

#                 path_queue.append(new_path)
#     return last_path[-1]




    # node is a person
    # when are two nodes connected? child -> parent 

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:
    def __init__(self):
        self.graph = {}
    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = set()

    def add_edge(self, node1, node2):
        self.graph[node1].add(node2)

    def get_neighbors(self, node):
        return self.graph[node]

    def size(self):
        return len(self.graph)

    
def build_graph(ancestors):
    g = Graph()

    for parent, child in ancestors:

        g.add_node(parent)
        g.add_node(child)
        g.add_edge(child, parent)

    return g 

def earliest_ancestor(ancestors, starting_node):
    g = build_graph(ancestors)

    s = Stack()
    visited = set()

    s.push([starting_node])

    max_path_len = 1
    most_ancient = -1 
    while s.size() > 0:
        current_path = s.pop()
        current_node = current_path[-1]


        if len(current_path) > max_path_len or (len(current_path) == max_path_len and current_node < most_ancient):
            max_path_len = len(current_path)
            most_ancient = current_node 

        if current_node not in visited: 
            visited.add(current_node)

            parents = g.get_neighbors(current_node)

            for parent in parents: 
                # parent_copy = current_path + [parent]

                # s.push(current_path)
                parent_copy = list(current_path)
                parent_copy.append(parent)
                s.push(parent_copy)