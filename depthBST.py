from minHeightTree import createMinTree, inOrder

class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def createLevelLinkedList(root):
    #results is a list of lists
    result = [[]]
    current = []
    if (root != None):
        current.append(root)
    while(len(current) > 0):
        #add previous level
        temp = parent
        result.append(temp)
        #Go to next level
        parents = current
        current = []
        for parent in parents:
            print(parent)
           
    return result

def main():
    arr = [13, 23, 33, 48, 55, 83, 99, 150, 214, 299]
    tree = createMinTree(arr, 0, 9)
    listoflists = createLevelLinkedList(tree)
    print(listoflists)

if __name__ == "__main__":
    main()

