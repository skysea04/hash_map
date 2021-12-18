from basic_hash import do_hash_process


def djb2_hash(key):
    hash = 5381
    for c in key:
        hash = hash * 33 + ord(c)
    return hash % 1013


class HashTable:
    
    def __init__(self):
        self.table = [None] * 1013

    def put(self, key, value):
        position = djb2_hash(key)
        self.table[position] = value
    
    def get(self, key):
        return f'[{key} - { self.table[djb2_hash(key)] }]'

    def remove(self, key):
        self.table[djb2_hash(key)] = None
    
    def display(self):
        count = 0
        for i in range(len(self.table)):
            if self.table[i]:
                print(i, ':', self.table[i])
                count += 1
        print("count:", count)


do_hash_process(HashTable)