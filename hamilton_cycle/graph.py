''' Python program for solution of hamiltonian cycle problem

    Source: https://www.geeksforgeeks.org/hamiltonian-cycle/ '''

class Graph():
    def __init__(self, vertices):
        n_vertices = len(vertices)
        self.graph = [[0 for column in range(n_vertices)]
                            for row in range(n_vertices)]
        self.V = n_vertices
        self.labels = vertices

    ''' Check if this vertex is an adjacent vertex
        of the previously added vertex and is not
        included in the path earlier '''
    def isSafe(self, v, pos, path):
        # Check if current vertex and last vertex
        # in path are adjacent
        if self.graph[ path[pos-1] ][v] == 0:
            return False

        # Check if current vertex not already in path
        for vertex in path:
            if vertex == v:
                return False

        return True

    # A recursive utility function to solve
    # hamiltonian cycle problem
    def hamCycleUtil(self, path, pos, debug = False):

        # base case: if all vertices are
        # included in the path
        if pos == self.V:
            # Last vertex must be adjacent to the
            # first vertex in path to make a cycle
            if self.graph[ path[pos-1] ][ path[0] ] == 1:
                return True
            else:
                return False

        # Try different vertices as a next candidate
        # in Hamiltonian Cycle. We don't try for 0 as
        # we included 0 as starting point in hamCycle()
        for v in range(1,self.V):

            if self.isSafe(v, pos, path) == True:

                path[pos] = v

                if debug:
                    print(path)

                if self.hamCycleUtil(path, pos+1, debug) == True:
                    return True

                # Remove current vertex if it doesn't
                # lead to a solution
                path[pos] = -1

        return False

    def hamCycle(self, debug = False):
        path = [-1] * self.V

        ''' Let us put vertex 0 as the first vertex
            in the path. If there is a Hamiltonian Cycle,
            then the path can be started from any point
            of the cycle as the graph is undirected '''
        path[0] = 0

        if self.hamCycleUtil(path,1, debug) == False:
            if debug:
                print ("Solution does not exist\n")
            return False

        if debug:
            self.printSolution(path)
        self.path = path
        return True

    def printSolution(self, path):
        print ("Solution Exists: Following",
                 "is one Hamiltonian Cycle")
        for vertex in path:
            print (self.labels[vertex], end = "\n")
        print (path[0], "\n")

    ''' Custom print function to print cycle as "assignment '''
    def printAssignment(self, drivers, dates):
        last = -1
        for vertex in self.path:
            label = self.labels[vertex]
            if label in dates:
                print("\"" + self.labels[last] + "\",\"" + self.labels[vertex] + "\"", end = "\n")
            last = vertex