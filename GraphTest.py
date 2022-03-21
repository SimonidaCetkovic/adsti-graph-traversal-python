from Node import Node
from Graph import Graph
from unittest import TestCase

class TestSolution(TestCase):
    def test_solution(self):
        catNode = Node(True)
        catsNode = catNode.setChild('s', True)
        catcNode = catNode.setChild('c', False)
        catchNode = catcNode.setChild('h', True)
        cateNode = catNode.setChild('e', False)
        caterNode = cateNode.setChild('r', True)
    
        graph = Graph()
        response = graph.dfs('cat', catNode)
        
        self.assertEqual(response, ['cat', 'cats', 'catch', 'cater'])