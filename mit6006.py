# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 18:44:02 2016

@author: yiz613
"""

class BST(object):
    def __init__(self):
        self.root = None
    
    def insert(self, t):
        new = BSTnode(t)
        if self.root is None:
            self.root = new
        else:
            node = self.root
            while True:
                if t<node.key:
                    if node.left is None:
                        node.left = new
                        new.parent = node
                    node = node.left
                else:
                    if node.right is None:
                        node.right = new
                        new.parent = node
                    node = node.right
        return new