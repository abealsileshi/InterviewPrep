class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def __str__(self):
        return str(self.data)

def createMinTree(arr, start, end):
    if(start > end):
        return None
    
    mid = (start + end)/2
    n = TreeNode(arr[mid])
    n.left = createMinTree(arr, start, mid -1)
    n.right = createMinTree(arr, mid +1, end)
    return n

def inOrder(node):
    if(node != None):
        inOrder(node.left)
        print(node.data)
        inOrder(node.right)

def main():
    arr = [13, 23, 33, 55, 83, 99, 150, 214]
    tree = createMinTree(arr, 0, 7)
    inOrder(tree)

if __name__ == "__main__":
    main()