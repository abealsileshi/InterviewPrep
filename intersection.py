class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node
    
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if isinstance(values, list):
            self.add_multiple_nodes(values)
        else:
            self.addNode(values)
    
    def addNode(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
    
    def add_multiple_nodes(self, values):
        if not isinstance(values, list):
            raise Exception("The linked list must be added as a list")
        
        for value in values:
            self.addNode(value)

    def add_node_as_head(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.head = Node(value, self.head)
        return self.head

    def __str__(self):
        return '->'.join([str(node) for node in self])

    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count
    
    #why exactly do we need __iter__?
    def __iter__ (self):
        current = self.head
        while(current):
            yield (current) 
            current = current.next

    @property
    def values(self):
        #how does it access all nodes in self?
        return[node.value for node in self]
    
    #below function made with the help of https://www.learnsteps.com/algorithms-coding-linked-list-python/
    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.value == data:
                found = True
            else:
                current = current.next
        if current is None:
            current = None
        return current
    
    @staticmethod
    def getKthNode(linklist, k):
        current = linklist.head
        while(k > 0):
            current = current.next
            k = k - 1
        return current
    
    def findIntersection(self, linklist1, linklist2):
        print(linklist1)
        print(linklist2)

        if linklist1 is None:
            print("here1")
            return None
        
        if linklist2 is None:
            print("here2")
            return None

        size1 = len(linklist1)
        tail1 = linklist1.tail
        size2 = len(linklist2)
        tail2 = linklist2.tail

        if(tail1 != tail2):
            print("Tails aren't equal, there can't be an intersection")
            return None
        
        shorter = linklist1 if size1 < size2 else linklist2
        longer = linklist2 if size1 < size2 else linklist1

        diff = size2 - size1
        diff = abs(diff)

        #Why do LinkedList.method ? because we are inside of the class
        longer = LinkedList.getKthNode(longer, diff)
        shorter = LinkedList.getKthNode(shorter, 0)

        print(shorter)
        print(longer)
        count = 0
        while(shorter != longer):
            shorter = shorter.next
            longer = longer.next
            # print(count)
            count += 1
        
        print("The intersecting node is: ", str(longer))
        return longer


        
def main():
    linked_list1 = [10, 20, 30, 40, 50, 60, 70]
    ll = LinkedList(linked_list1)
    # ll.add_multiple_nodes(linked_list1)
    ll2 = LinkedList(15)
    ll2.addNode(25)
    ll2.addNode(35)

    common = ll.search(40)
    ll2.addNode(common)
    print("This is ll", str(ll))
    print("This is ll2", str(ll2))
    ll2.tail = ll.tail

    if ll2.search(40) == ll.search(40):
        print("they are equal")
    else:
        print("theyre not equal")

    intersection = ll2.findIntersection(ll, ll2)
    print(intersection)

if __name__ == "__main__":
    main()
