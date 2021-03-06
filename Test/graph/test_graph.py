import unittest
import config
from DataStructures import edge as e
from DataStructures import listiterator as it
from DataStructures import dfs
from ADT import graph as g
from ADT import queue as q
from ADT import list as lt


class GraphTest (unittest.TestCase):

    def setUp (self):
        pass



    def tearDown (self):
        pass

    def comparenames (self, searchname, element):
        return (searchname == element['key'])

    def comparelst (self, searchname, element):
        return (searchname == element)


    def test_newEdge (self):
        edge = e.newEdge (1,1,1)
        print (edge)


    def test_edgeMethods (self):
        edge = e.newEdge ('Bogota','Cali')

        print (e.either(edge))
        print (e.other(edge, e.either(edge)))
        print (e.weight(edge))


    def test_insertVertex (self):
        graph = g.newGraph(7,self.comparenames)

        g.insertVertex (graph, 'Bogota')
        g.insertVertex (graph, 'Yopal')
        g.insertVertex (graph, 'Cali')
        g.insertVertex (graph, 'Medellin')
        g.insertVertex (graph, 'Pasto')
        g.insertVertex (graph, 'Barranquilla')
        g.insertVertex (graph, 'Manizales')


    def test_addEdges (self):
        graph = g.newGraph(7,self.comparenames)

        g.insertVertex (graph, 'Bogota')
        g.insertVertex (graph, 'Yopal')
        g.insertVertex (graph, 'Cali')
        g.insertVertex (graph, 'Medellin')
        g.insertVertex (graph, 'Pasto')
        g.insertVertex (graph, 'Barranquilla')
        g.insertVertex (graph, 'Manizales')

        g.addEdge (graph, 'Bogota', 'Yopal')
        g.addEdge (graph, 'Bogota', 'Medellin')
        g.addEdge (graph, 'Bogota', 'Pasto')
        g.addEdge (graph, 'Bogota', 'Cali')
        g.addEdge (graph, 'Yopal', 'Medellin')
        g.addEdge (graph, 'Medellin', 'Pasto')
        g.addEdge (graph, 'Cali', 'Pasto')
        g.addEdge (graph, 'Cali', 'Barranquilla')
        g.addEdge (graph, 'Barranquilla','Manizales')
        g.addEdge (graph, 'Pasto','Manizales')

        self.assertEqual (g.numEdges(graph), 10)
        self.assertEqual (g.numVertex(graph), 7)

        lst = g.vertices (graph)
        self.assertEqual (lt.size (lst), 7)

        lst = g.edges (graph)
        self.assertEqual (lt.size (lst), 10)

        degree = g.degree (graph, 'Bogota')
        self.assertEqual (degree, 4)

        edge = g.getEdge (graph, 'Bogota', 'Medellin')

        lst = g.adjacents (graph, 'Bogota')
        self.assertEqual (lt.size (lst), 4)

    def test_connectedcomponents (self):
        
        graph = g.newGraph(7,self.comparenames)

        g.insertVertex(graph, 'Laura')
        g.insertVertex(graph, 'Eduardo')
        g.insertVertex(graph, 'Andres')
        g.insertVertex(graph, 'Camila')
        g.insertVertex(graph, 'Antonio')
        g.insertVertex(graph, 'Luis')
        g.insertVertex(graph, 'Lina')
    
        g.addEdge(graph, 'Laura', 'Luis')
        g.addEdge(graph, 'Eduardo', 'Laura')
        g.addEdge(graph, 'Antonio', 'Laura')
        g.addEdge(graph, 'Camila', 'Lina')

        cc=dfs.countCC(graph)
        self.assertEqual (cc, 3)

    def test_connectedcomponents1 (self):
        
        graph = g.newGraph(1,self.comparenames)

        g.insertVertex(graph, 'Laura')

        cc=dfs.countCC(graph)
        self.assertEqual (cc, 1)

    def test_connectedcomponents0 (self):
        
        graph = g.newGraph(1,self.comparenames)

        cc=dfs.countCC(graph)
        self.assertEqual (cc, 0)

if __name__ == "__main__":
    unittest.main()
