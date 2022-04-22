class DynamicArray(object):
    def __init__(self):
        # num of elements in dynamic array
        self.size = 0
        # max capacity of the dynamic array
        self.capacity = 1
        self.array = self._create_array(self.capacity)
    
    def _len_(self):
        return self.size
    
    def _getitem_(self, index):
        if not 0 <= index < self.size:
            raise IndexError('Given index: {0} is larger than array size {1}'.format(index, self.size))
        
        return self.array[index]
    
    def _create_array(self, length):
        return [None] * length

    def _resize(self, new_capacity):
        new_array = self._create_array(new_capacity)

        #reassign the elements in the old array into the new array
        for i in range(self.size):
            new_array[i] = self.array[i]
        
        self.array = new_array
        self.capacity = new_capacity
    
    def append(self, element):
        print("This is self.size " , self.size)
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.size] = element
        self.size +=1
    
    def pop(self):
        element = None

        if self.size > 0:
            element = self.array[self.size - 1]
            self.array[self.size - 1] = None
            self.size -= 1

        if self.size < self.capacity // 4:
            self._resize(self.capacity // 2)
        
        return element


def main():
    print("In Python file!")
    array1 = DynamicArray()
    array1.append(4)
    array1.append(7)

if __name__ == "__main__":
    main()
