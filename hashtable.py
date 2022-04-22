
class HashTable:

    def __init__(self):
        self.size = 10
        self.hashmap = [[] for _ in range(0, self.size)]
        # print(self.hashmap)

    
    def hashing_func(self, key):
        hashed_key = hash(key) % self.size
        return hashed_key
    
    def set(self, key, value):
        hash_key = self.hashing_func(key)
        key_exists = False
        slot = self.hashmap[hash_key]
        for i, kv in enumerate(slot):
            #k is for key, v for value, since kv is a tuple
            k, v = kv
            if key == k:
                key_exists = True
                break
        
        if key_exists:
            slot[i] = ((key, value))
        else:
            slot.append((key, value))
    
    def get(self, key):
        hash_key = self.hashing_func(key)
        slot = self.hashmap[hash_key]
        for kv in slot:
            k, v = kv
            if key == k:
                return v
            else:
                raise KeyError('Does not exist')

    def __setitem__(self, key, value):
        return self.set(key, value)
    
    def __getitem__(self, key):
        return self.get(key)



H = HashTable()
H.set('key1', 'value1')
H.set('key2', 'value2')
H.set('key3', 'value2')
H.set('key3', 'chaining')
H.set('key4', 'value4')
H.set('key5', 'value5')
H.set('key6', 'value6')
H.set('key7', 'chaining7')
H.set('key8', 'value8')
H.set('key9', 'value9')
H.set('key10', 'chaining10')
H.set('key11', 'value11')
H.set('key12', 'value12')
# print(H.get('key1'))
print(H.hashmap)

# H['key4'] = 'value4'
# print(H['key4'])