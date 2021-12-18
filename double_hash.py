from basic_hash import do_hash_process

class ValuePair:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f'[{self.key} - {self.value}]'



class DoubleHashTable:
    # initialize hash Table
    def __init__(self):
        self.size = 12
        
        # initialize table with all elements 0
        self.table = [None] * self.size
        self.elementCount = 0
        self.comparisons = 0
   
   
    # method that checks if the hash table is full or not
    def isFull(self):
        if self.elementCount == self.size:
            return True
        else:
            return False
      
    
    # First hash function
    def h1(self, key):
        hash = 0
        for c in key:
            hash += ord(c)
        return hash % self.size
       
    # Second hash function
    def h2(self, key):
        hash = 0
        for c in key:
            hash += ord(c)
        return 5 - (hash % 5)
           
   
    # method to resolve collision by double hashing method
    def doubleHashing(self, key):
        posFound = False
        # limit variable is used to restrict the function from going into infinite loop
        # limit is useful when the table is 80% full
        limit = self.size
        i = 1
        # start a loop to find the position
        while i <= limit:
            # calculate new position by quadratic probing
            newPosition = (self.h1(key) + i*self.h2(key)) % self.size
            # if newPosition is empty then break out of loop and return new Position
            if self.table[newPosition] == None:
                posFound = True
                break
            else:
                # as the position is not empty increase i
                i += 1
        return posFound, newPosition
 
       
    # method that inserts element inside the hash table
    def put(self, key, value):
        # checking if the table is full
        if self.isFull():
            print("Hash Table Full")
            return False
           
        posFound = False
       
        position = self.h1(key)
           
        # checking if the position is empty
        if self.table[position] == None:
            # empty position found , store the element and print the message
            self.table[position] = ValuePair(key, value)
            print(f"Email of {key} is at position {position}")
            self.elementCount += 1
       
        # If collision occured 
        else:
            print(f"Collision has occured for {key}'s email at position {position} finding new Position.")
            while not posFound:
                posFound, position = self.doubleHashing(key)
                if posFound:
                    self.table[position] = ValuePair(key, value)
                    #print(self.table[position])
                    self.elementCount += 1
                    #print(position)
                    #print(posFound)
                    print(f"Email of {key} is at position {position}")
 
        return posFound
       
 
    # searches for an element in the table and returns position of element if found else returns False
    def get(self, key):
        found = False
        position = self.h1(key)
        self.comparisons += 1

        if(self.table[position] != None):
            if(self.table[position].key == key):
                print(f"Person {key} found at position {position} and total comparisons are 1")
                return position
           
            # if element is not found at position returned hash function
            # then we search element using double hashing
            else:
                limit = self.size
                i = 1
				
                # start a loop to find the position
                while i <= limit:
                    # calculate new position by double Hashing
                    position = (self.h1(key) + i*self.h2(key)) % self.size
                    self.comparisons += 1
                    # if element at newPosition is equal to the required element
                   
                    if(self.table[position] != None):
                        if self.table[position].key == key:
							
                            found = True
                            break
                       
                        elif self.table[position].key == None:
                            found = False
                            break
                           
                        else:
                            # as the position is not empty increase i
                            i += 1
							
							
            if found:
                print(f"Person {key} found at position {position} and total comparisons are {i+1}")
                return position
				# return True
        else:
            print("Record not Found")
            return found           
   
   
    # method to display the hash table
    def display(self):
        for i in range(self.size):
            if self.table[i]:
                print("Hash Value:", i, "\t", self.table[i])
        print("count:", self.elementCount)

do_hash_process(DoubleHashTable)