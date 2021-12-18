from basic_hash import lose_lose_hash, do_hash_process

class ValuePair:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f'[{self.key} - {self.value}]'


class ListNode:

    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self):
        self.length = 0
        self.head = None
    
    def append(self, node):
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self.length += 1


class HashLinkedListTable:
    
    def __init__(self):
        self.table = [None] * 37

    def put(self, key, value):
        position = lose_lose_hash(key)
        if self.table[position] is None:
            self.table[position] = LinkedList() 
        self.table[position].append(ListNode(ValuePair(key, value)))

    def get(self, key):
        position = lose_lose_hash(key)
        if self.table[position]:
            current = self.table[position].head
            while current:
                if current.val.key == key:
                    return current.val
                current = current.next
        return None
    
    def remove(self, key):
        position = lose_lose_hash(key)
        if self.table[position]:
            prev = None
            current = self.table[position].head
            while current:
                if current.val.key == key:
                    if prev:
                        prev.next = current.next
                    else:
                        self.table[position].head = current.next
                prev = current
                current = current.next  


    def display(self):
        count = 0
        for i in range(len(self.table)):
            if self.table[i]:
                current = self.table[i].head
                while current:
                    print(current.val)
                    count += 1
                    current = current.next
        print("count:", count)


if __name__ == '__main__':
    do_hash_process(HashLinkedListTable)
