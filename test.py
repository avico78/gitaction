
from collections import deque
from typing import Any


# Avi - linkedlist 


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self) -> str:
        return self.data

class LinkedList:

    def __init__ (self,nodes=None):
        self.head=None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node

            for elem in nodes:
                node.next = Node(data=elem)  
                node = node.next
        
    def __repr__(self) -> str:
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")

        return "->".join(nodes)

    def __iter__(self) :
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self , node):
        node.next = self.head
        self.head=node
        
    
    def add_last(self , node):
    
        curr_node = self.head
        while curr_node is not None:
          
            prev = curr_node
            curr_node = curr_node.next   
        prev.next = node

    def insert_after(self,node_after,node)        :
        if self.head is None:
            raise Exception("list is empty")
        for curr_node in self:
              if curr_node.data == node_after:
                print("found",curr_node)
                node.next = curr_node.next
                curr_node.next = node
                return 

    def remove_node(self, node_to_remove):
        if self.head is None:
             Exception("Empty LL")
            
        
        # Case need to remove the head !
        if self.head.data == node_to_remove:
            self.head = self.head.next
            return
        # all other case -> require Traves the link
        prev_node = self.head
        for node in self:
            if node.data  == node_to_remove:
                prev_node.next= node.next
                return
            prev_node = node    





    def insert_before (self,node_before,node)        :
        if self.head.data == node_before:
            node.next = self.head 
            self.head = node
            return
        prev_node = None
        for curr_node in self:
            if curr_node.data == node_before:
                prev_node.next = node
                node.next = curr_node
                return           
            prev_node = curr_node



if __name__ == "__main__":

    llist = LinkedList(["a", "b", "c", "d", "e"])
    print("first list",llist)
    newNode =  Node("AA")
    llist.add_first(newNode)
    print("adding AA as first node:",llist)
    #adding LAST to end of the list

    llist.add_last(Node("LAST"))
    print("adding LAST to end of the list:",llist)
    # add node after specifc node
    llist.insert_after("AA",Node("AFTER"))   
    print("case adding new node before first one ")
    llist.insert_before("AA",Node("BEFORE_FIRST"))
    print("case adding new node before first one",llist)

    llist.remove_node("AA")
    print("Remove specifc node (AA) from the list",llist)
