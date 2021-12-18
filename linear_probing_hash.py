from basic_hash import lose_lose_hash, do_hash_process


class ValuePair:

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    def __str__(self):
        return f'[{self.key} - {self.value}]'


class LinearProbingHash:

    def __init__(self):
        self.table = [None] * 37
    
    def put(self, key, value):
        position = lose_lose_hash(key)
        while self.table[position] and self.table[position].key:
            position += 1
        self.table[position] = ValuePair(key, value)
        
    def get(self, key):
        position = lose_lose_hash(key)
        if self.table[position]:
            while not self.table[position] or self.table[position].key != key:
                position += 1
                if position == len(self.table):
                    return None
            if self.table[position].key == key:
                return self.table[position]
        return None

    def remove(self, key):
        position = lose_lose_hash(key)
        while self.table[position] and self.table[position].key != key:
            position += 1
        if self.table[position] and self.table[position].key == key:
            self.table[position] = ValuePair()

    def display(self):
        count = 0
        for i in range(len(self.table)):
            if self.table[i]:
                print(i, ':', self.table[i])
                count += 1
        print("count:", count)
            

do_hash_process(LinearProbingHash)