
import collections 


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


def earliest_ancestor(ancestors, starting_node):
    parents_by_child = {} 
    
    for parent, child in ancestors:
        if child in parents_by_child:
            parents_by_child[child].append(parent)
        else: 
            parents_by_child[child] = [parent]
    
    if starting_node not in parents_by_child:
        return - 1

    path_queue = collections.deque()

    last_path = [starting_node]

    path_queue.append(last_path)

    while len(path_queue) > 0:
        last_path = path_queue.popleft()
        oldest_ancestor = last_path[-1]

        if oldest_ancestor in parents_by_child:
            parents_by_child[oldest_ancestor].sort(reverse=True)
            for parent in parents_by_child[oldest_ancestor]:
                new_path = last_path.copy()
                new_path.append(parent)

                path_queue.append(new_path)
    return last_path[-1]