class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.entries = 0
        
        if capacity >= MIN_CAPACITY:
            self.table = [None] * capacity
        else:
            self.table = [None] * MIN_CAPACITY

    def get_num_slots(self):
        return len(self.table)
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here


    def get_load_factor(self):
        return self.entries / len(self.table)
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        
        item = HashTableEntry(key, value)
        index = self.hash_index(key)
        self.entries += 1
        if self.table[index]:
            position = self.table[index]
            while position.next and position.key != key:
                position = position.next
            if position.key == key:
                position.value = value
            else:
                position.next = item
        else:
            self.table[index] = item
            


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        position = self.table[index]
        if position == None:
            print('Key not found')
        else:
            while self.table[index].key != key and position.next != None:
                position = position.next 
        
            self.entries -= 1
            if self.table[index].next:
                self.table[index] = position.next  
            else: 
                self.table[index] = None
        
            


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        if self.table[self.hash_index(key)] == None:
            return None
        else:
            pos = self.table[self.hash_index(key)]
            while key != pos.key and pos.next:
                pos = pos.next
            if pos.key == key:
                return pos.value
            else:
                return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        self.capacity = new_capacity
        self.entries = 0
        old_table = self.table
        self.table = [None] * self.capacity
        for i in range(len(old_table)):
            if old_table[i].next:
                pos = old_table[i]
                while pos != None:
                    self.put(pos.key, pos.value)
                    pos = pos.next
            else:
                self.put(old_table[i].key, old_table[i].value)



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'1 Twas brillig, and the slithy toves'")
    ht.put("line_2", "2 Did gyre and gimble in the wabe:")
    ht.put("line_3", "3 All mimsy were the borogoves,")
    ht.put("line_4", "4 And the mome raths outgrabe.")
    ht.put("line_5", '5 "Beware the Jabberwock, my son!')
    ht.put("line_6", "6 The jaws that bite, the claws that catch!")
    ht.put("line_7", "7 Beware the Jubjub bird, and shun")
    ht.put("line_8", '8 The frumious Bandersnatch!"')
    ht.put("line_9", "9 He took his vorpal sword in hand;")
    ht.put("line_10", "10 Long time the manxome foe he sought--")
    ht.put("line_11", "11 So rested he by the Tumtum tree")
    ht.put("line_12", "12 And stood awhile in thought.")

    # print(ht.get("line_5"), 'line5')
    # Test storing beyond capacity
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # Test resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))
    print(ht.get(f"line_12"))
