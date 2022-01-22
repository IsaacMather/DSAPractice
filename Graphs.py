#couple ways to do this, adjacency matrix and with adjacency list

def adjacency_matrix():
    #adjacency matrix is nice because it is simple and easy to see what is
    # connected to what.
    #thing is, it's a sparse matrix, so most of the cells are empty and so
    # therefore it is not a very efficient way to store data
    #in fact, in python you have to go out of your way to create a matrix
    # stucture like the grid form shown in the example
    #adjacency matrixes are good when the number of edjes is large, like for
    # example every vertice is connected to every other vertice. Most problems
    # in the real world are sparse.
    pass


def adjacency_list():
    #more efficient way to store a graph is a adjacency list. we keep a
    # master list of all the vertices in th Graph object, and then each vertex
    # object in the graph maintain a list of all the other vertices it is
    # connected to. We will use a dictionary where the keys are the vertices and
    # the values are the weights
    #advantage of the adjacency list is it allows us to compactly represent a
    # sparse graph
    pass


 class Graph:
     def __init__(self):
         self.vertList = {}
         self.numVertices = 0

     def addVertes(self, key):
         self.numVertices self.numVertices + 1
         newVertex = Vertex(key)
         self.vertList[key] = newVertex
         return newVertex

     def getVertex(self, n):
         if n in self.vertList:
             return self.vertList[n]
         else:
             return None

     #complete graph class here


#so a graph is made of vertices, so let's make a Vertex class!
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, neighbor, weight=0):
        self.connectedTo[neighbor] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x for x in
                                                      self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getID(self):
        return self.id

    def getWeight(self, neighbor):
        return self.connectedTo[neighbor]
