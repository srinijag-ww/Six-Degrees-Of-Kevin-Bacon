import os

class Graph(object):
    # Initializing empty graph
    def __init__(self):
        self.adj_list = dict()    # Initial adjacency list is empty dictionary
        self.vertices = set()    # Vertices are stored in a set
        self.degrees = dict()    # Degrees stored as dictionary

    # Checks if (node1, node2) is edge of graph. Output is 1 (yes) or 0 (no).
    def isEdge(self,node1,node2):
        if node1 in self.vertices:        # Check if node1 is vertex
            if node2 in self.adj_list[node1]:    # Then check if node2 is neighbor of node1
                return 1            # Edge is present!

        if node2 in self.vertices:        # Check if node2 is vertex
            if node1 in self.adj_list[node2]:    # Then check if node1 is neighbor of node2
                return 1            # Edge is present!

        return 0                # Edge not present!

    # Add undirected, simple edge (node1, node2)
    def addEdge(self,node1,node2):

        # print('Called')
        if node1 == node2:            # Self loop, so do nothing
            # print('self loop')
            return
        if node1 in self.vertices:        # Check if node1 is vertex
            nbrs = self.adj_list[node1]        # nbrs is neighbor list of node1
            if node2 not in nbrs:         # Check if node2 already neighbor of node1
                nbrs.add(node2)            # Add node2 to this list
                self.degrees[node1] = self.degrees[node1]+1    # Increment degree of node1

        else:                    # So node1 is not vertex
            self.vertices.add(node1)        # Add node1 to vertices
            self.adj_list[node1] = {node2}    # Initialize node1's list to have node2
            self.degrees[node1] = 1         # Set degree of node1 to be 1

        if node2 in self.vertices:        # Check if node2 is vertex
            nbrs = self.adj_list[node2]        # nbrs is neighbor list of node2
            if node1 not in nbrs:         # Check if node1 already neighbor of node2
                nbrs.add(node1)            # Add node1 to this list
                self.degrees[node2] = self.degrees[node2]+1    # Increment degree of node2

        else:                    # So node2 is not vertex
            self.vertices.add(node2)        # Add node2 to vertices
            self.adj_list[node2] = {node1}    # Initialize node2's list to have node1
            self.degrees[node2] = 1         # Set degree of node2 to be 1

    # Give the size of the graph. Outputs [vertices edges wedges]
    #
    def size(self):
        n = len(self.vertices)            # Number of vertices

        m = 0                    # Initialize edges/wedges = 0
        wedge = 0
        for node in self.vertices:        # Loop over nodes
            deg = self.degrees[node]      # Get degree of node
            m = m + deg             # Add degree to current edge count
            wedge = wedge+deg*(deg-1)/2        # Add wedges centered at node to wedge count
        return [n, m, wedge]            # Return size info

    # Print the graph
    def output(self,fname,dirname):
        os.chdir(dirname)
        f_output = open(fname,'w')

        for node1 in list(self.adj_list.keys()):
            f_output.write(str(node1)+': ')
            for node2 in (self.adj_list)[node1]:
                f_output.write(str(node2)+' ')
            f_output.write('\n')
        f_output.write('------------------\n')
        f_output.close()

    def path(self, src, dest):
        """ implement your shortest path function here """
        shortest_path = []
        visited = set([src])
        pathTo = dict()

        # Your code comes here
        queue = [src]
        found = False
        while len(queue) != 0:
            current = queue.pop(0)
            for nbr in self.adj_list[current]:
                if nbr == dest:
                    pathTo[nbr] = current
                    found = True
                    break
                if nbr not in visited:
                    pathTo[nbr] = current
                    queue.append(nbr)
                    visited.add(nbr)
            if found:
                break
        if len(pathTo) > 0:
            current = dest
            while current in pathTo:
               shortest_path.insert(0, current)
               current = pathTo[current]
            shortest_path.insert(0, src)

        #print("Path = ", shortest_path)
        return shortest_path

    def levels(self, src):
        """ implement your level set code here """
        level_sizes = [1, 0, 0, 0, 0, 0, 0]

        # Your code comes in here
        visited = set([src])

        # Your code comes here
        queue = [ (src, 0) ]
        found = False
        while len(queue) != 0:
            current, level = queue.pop(0)
            if (level == 6 ):
                nextLevel = level
            else:
                nextLevel = level + 1
            for nbr in self.adj_list[current]:
                if nbr not in visited:
                    level_sizes[nextLevel] = level_sizes[nextLevel] + 1
                    queue.append((nbr, nextLevel))
                    visited.add(nbr)

        #print (level_sizes)
        return level_sizes
