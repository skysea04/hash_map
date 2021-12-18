def lose_lose_hash(key):
    hash = 0
    for c in key:
        hash += ord(c)
    return hash % 37


class HashTable:

    def __init__(self):
        self.table = [None] * 37

    def put(self, key, value):
        position = lose_lose_hash(key)
        self.table[position] = value
    
    def get(self, key):
        return f'[{key} - { self.table[lose_lose_hash(key)] }]'

    def remove(self, key):
        self.table[lose_lose_hash(key)] = None
    
    def display(self):
        count = 0
        for i in range(len(self.table)):
            if self.table[i]:
                print(i, ':', self.table[i])
                count += 1
        print("count:", count)


def do_hash_process(HashClass):

    hash_table = HashClass()
    hash_table.put('Skysea', 'skysea0000@gmail.com')
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

    # None person
    # print(hash_table.get('arcade'))
    # hash_table.remove('Ton')
    # hash_table.remove('Skyseb')
    print(hash_table.get('Ton'))
    print(hash_table.get('WeiChen'))

    print("-" * 40)
    try:
        hash_table.display()
    except Exception:
        print("No display function")


if __name__ == '__main__':
    do_hash_process(HashTable)