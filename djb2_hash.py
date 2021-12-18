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
    
    def show(self):
        count = 0
        for i in range(len(self.table)):
            if self.table[i]:
                print(i, ':', self.table[i])
                count += 1
        print("count:", count)


hash_table = HashTable()
hash_table.put('Skysea', 'arcade0000@gmail.com')
hash_table.put('Lucas', 'lucas0101@gmail.com')
hash_table.put('Ariana', 'ariana0202@gmail.com')
hash_table.put('Andy', 'andy0303@gmail.com')
hash_table.put('Tony', 'tony0404@gmail.com')
hash_table.put('WeiChen', 'weichen0505@gmail.com')
hash_table.put('Ton', 'wyt0606@gmail.com')
hash_table.put('Sol', 'sol0707@gmail.com')
hash_table.put('YCLee', 'yclee0808@gmail.com')
hash_table.put('YuehHsin', 'yuehhsin0909@gmail.com')

print(hash_table.get('Skysea'))
print(hash_table.get('Lucas'))
print(hash_table.get('WeiChen'))

print("-" * 40)
hash_table.show()