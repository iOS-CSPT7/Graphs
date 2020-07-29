"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """

        self.vertices[vertex_id] = set()
        pass  # TODO

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """

        self.vertices[v1].add(v2)
        pass  # TODO

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """

        return self.vertices[vertex_id]
        # TODO

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """


        # make a queue 
        q = Queue()
        # enqueue our start node 
        q.enqueue(starting_vertex)
        # make a set to track visited nodes 
        visited = set()
        # while queue still has hings in it 

        while q.size() > 0:
            current_node = q.dequeue()
        # dq from fornt of the line, this is our current node 
        # check if we've visited, if nott
            if current_node not in visited: 
                visited.add(current_node)
                print(current_node)
                neighbors = self.get_neighbors(current_node)
        # mark it as visited 
        # get its neighbors 
        # iterate over neighbors
                for neighbor in neighbors: 
                    q.enqueue(neighbor) 
        # add to queue 

        # starting_vertex = 1 

        # q = Queue()
        # visied = set(1)

        # current_node = 1 

        # neighbors = set(2)
        pass  # TODO

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # make a stack 

        s = Stack()
        # push our starting node onto the stack 
        s.push(starting_vertex)
        # make a set to track the nodes we've visited 
        visited = set()
        # as long as our stack isn't empty 
        while s.size() > 0: 
        # pop off the top, this is our current node 
            current_node = s.pop()
        # check if we have visited this before, and if not : 
            if current_node not in visited: 
        # mark it as visited 
                visited.add(current_node)
                print(current_node)
                neighbors = self.get_neighbors(current_node)
        # get its neighbors 
                for neighbor in neighbors:
                    s.push(neighbor)
        # iterate over neighbors 
        # and add them to our stack 
        pass  # TODO

    # def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        # visited = set()

        # def dft(vertex):
        #     if vertex in visited: 
        #         return 
        #     else: 
        #         visited.add(vertex)
            
        #     for neighbor in self.get_neighbors(vertex):
        #         dft(neighbor)
        # dft(starting_vertex)
        
        # Tims solution:
    def dft_recursive(self, vertex, visited = None):

        if visited == None: 
            visited = set()
        if vertex not in visited: 
            visited.add(vertex)
            neighbors = self.get_neighbors(vertex)
            if len(neighbors) == 0:
                return visited 
            for neighbor in neighbors:
                self.dft_recursive(neighbor, visited)  

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # visited = set()

        # q = Queue()

        # q.enqueue([starting_vertex])

        # while q.size() > 0:
        #     v = q.dequeue()
        #     last = v[-1]

        #     if last in visited: 
        #         continue 
        #     else: 
        #         visited.add(last)
        #     for neighbor in self.get_neighbors(last):
        #         next_path = v.copy()
        #         next_path.append(neighbor)

        #         if neighbor == destination_vertex: 
        #             return next_path
        #         q.enqueue(next)
        # pass  # TODO
        # TIms: 
        # make a queue
        q = Queue()
        # make a set to track visited 
        visited = set()
        # enqueue a Path to the starting vertex

        path = [starting_vertex]
        q.enqueue(path)
        while q.size() > 0:
        # as long as queue isn't empty 

            current_path = q.dequeue()
        # dequeue from front of the line 
        # current_node is the last thing in the current path 
            current_node = current_path[-1]
        #check if this is the target node 
            if current_node == destination_vertex:
        # if so return 
                return current_path
        # check if we've visited yet, if not: 
            if current_node not in visited: 
        # mark as visited: 
                visited.add(current_node)

        # get the current node's neighbors 
                neighbors = self.get_neighbors(current_node)
        # iterate over the neighbors .
                for neighbor in neighbors:
        # add the neighbor to the path
                    neighbor_path = current_path.copy()
                    neighbor_path.append(neighbor)
                    
        # enqueue the neighbor's path 
                    q.enqueue(neighbor_path)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        visited = set()

        s = Stack()

        s.push([starting_vertex])

        while s.size() > 0:
            v = s.pop()
            last = v[-1]

            if last in visited: 
                continue 
            else: 
                visited.add(last)
            for neighbor in self.get_neighbors(last):
                next_path = v.copy()
                next_path.append(neighbor)
                if neighbor == destination_vertex:
                    return next_path
                s.push(next_path)
        
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited = set()

        def dft(path):
            last = path[-1]
            if last in visited: 
                return None 

            else: 
                visited.add(last)
            if last == destination_vertex:
                return path
            for neighbor in self.get_neighbors(last):
                next_path = path.copy()
                next_path.append(neighbor)

                found = dft(next_path)

                if found: 
                    return found 
            return None
        return dft([starting_vertex])

        # Tims' : 
    
    # def dfs_recursive(self, starting_vertex, path = [], destination_vertex,  visited = None):
    #     if visited == None: 
    #         visited = set()

    #     if starting_vertex not in visited: 
    #         visited.add(starting_vertex)

    #     if len(path) == 0:
    #         path.append(starting_vertex)

    #     if starting_vertex == destination_vertex: 
    #         return path 

    #     neighbors = self.get_neighbors(starting_vertex)

    #     for neighbor in neighbors:
    #         if neighbor not in visited: 
    #             # recurse
    #             result = self.dfs_recursive(neighbor, path + [neighbor], destination_vertex,  visited)
    #             if result is not None: 
    #                 return result 
    #     return None
 

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
