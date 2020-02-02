# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 14:12:06 2019

@author: User Ambev
"""


import joblib
from .Base import *
import networkx as nx

class ModelPipeline():
    
    @classmethod
    def load(cls, loading_path, **joblibargs):
        return joblib.load(loading_path, **joblibargs)
    
    def save(self, saving_path, **joblibargs):
        joblib.dump(self, saving_path, **joblibargs)

    def __init__(self, input_nodes, output_nodes):
        if not isinstance(input_nodes, list):
        	raise TypeError('input_nodes must be list')

    	if not isinstance(output_nodes, list):
        	raise TypeError('output_nodes must be list')
        
        assert all([isinstance(node, Capsula) for node in input_nodes+output_nodes])
        self.build_graph(output_node)
        self.check_graph()

        
    
    def build_graph(self, output):

    	def create_graph(output, graph):
		    if not output in graph:
		        graph.add_node(output)
		    for node in output.input_nodes:
		        if node.input_nodes:
		            if not node in graph:
		                graph.add_node(node)            
		            graph.add_edge(node,output)
		            create_graph(node,graph)
		        else:
		            if not node in graph:
		                graph.add_node(node)            
		            graph.add_edge(node,output)
		            
	    graph = nx.DiGraph()
    	for output in self.output_nodes
	    	create_graph(output, graph)
	    self.graph = graph
	    return
        
    def fit(self):
        
        self.output_node.fit()
        
        return self 	
    
    def transform(self):

    	self.output_node.transform()
                            
    def check_graph(self, input_nodes):
    	#check for connectedness and input nodes as endpoints
		if not self.graph.is_connected():
			raise AssertionError('graph is disconnected')
		degrees = self.graph.degree
		degree1_nodes = set([node if (degree == 1 and node != self.output_node)  for node, degree in degrees])
		


		if (degree1_nodes - set(input_nodes)) != set({}) :
			not_input_nodes = degree1_nodes - set(input_nodes)
			raise AssertionError('{} are not an isntane of Inputer'.format(not_input_nodes))