#credit for binary_tree class https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/chapter_04/p08_first_common_ancestor.py
#Java code taken from CTCI by Gayle Laakman

import binary_tree

def depth(node):
    depth = 0
    current = node
    while(current != None):
        current = current.parent
        depth += 1
    return depth
    

def goUpBy(node, k):
    current = node
    while(k > 0 and current != None):
        current = current.parent
        k -= 1
    return current

#Edge case that they're the same depth
def first_common_ancestor(node1, node2):
    if(node1 == None or node2 == None):
        raise Exception("One of the nodes to find common ancestor is null")

    delta = depth(node1) - depth(node2)
    first = node1 if delta > 0 else node2 #the node that is further down
    second = node2 if delta > 0 else node1 #the node closer to root

    first = goUpBy(first, abs(delta))

    while(first != second and first != None and second != None):
        first = first.parent
        second = second.parent
    
    #both nodes will be the same at this point 
    return first



if __name__ == "__main__":
    t = binary_tree.BinaryTree()
    n1 = t.insert(1, None)
    n2 = t.insert(2, n1)
    n3 = t.insert(3, n1)
    n4 = t.insert(4, n2)
    n5 = t.insert(5, n2)
    n7 = t.insert(7, n3)
    n8 = t.insert(8, n4)

    # t.inOrder(t.root)

    ancestor = first_common_ancestor(n5, n8)
    print("first common ancestor is : ", ancestor.key)