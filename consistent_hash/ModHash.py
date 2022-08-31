#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 rzavalet <rzavalet@noemail.com>
#
# Distributed under terms of the MIT license.

"""
An implementation of a Hash using mod.
Please implement the requiered methods.
"""

from HashScheme import HashScheme
import hashlib

class ModHash(HashScheme):

    def __init__(self):
        """
        You have to decide what members to add to the class
        """
        self.__scheme_name = 'Modular Hash'
        self.nodes = []
        

    def get_name(self):
        return self.__scheme_name
    
    """
    Return a hash using md5.
    """
    def __get_hash(self, value):
        hash_md5 = int(hashlib.md5(value.encode()).hexdigest(), 16) % self.get_size() 
        return hash_md5

    """
    Returns the number nodes.
    """
    def get_size(self):
        number_buckets = len(self.nodes)
        return number_buckets

    """
    Auxiliary method to print out information about the hash
    """
    def dump(self):
        for i in range(self.get_size()):
            print("Hash: {0}, Node: {1}".format(i+1, self.nodes[i]))    

    """
    Possibly just increment a counter of number of nodes. You may also
    need to update Store to react in certain way depending on the
    scheme_name.
    """
    def add_node(self, new_node):
        self.nodes.append(new_node) 
        

    def remove_node(self, node):
        """
        Possibly just decrement a counter of number of nodes. You may also
        need to update Store to react in certain way depending on the
        scheme_name.
        """
        try: 
           self.nodes.remove(node)
        except ValueError:
            return 1

        return 0;

    def hash(self, value):
        """
        Convert value to a number representation and then obtain mod(number_of_nodes)
        """
        if len(self.nodes) == 0:
            return None
        
        hash_nodes = self.nodes[self.__get_hash(value)]
        
        return hash_nodes
