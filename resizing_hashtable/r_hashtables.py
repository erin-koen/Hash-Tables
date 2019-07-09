

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [] * capacity


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max_index):
    # take a string, run it through hash function, return an integer between 0 (inclusive) and max (exclusive). Max will be passed as BasicHashTable.capacity
    djb2 = 5381
    for char in string:
        djb2 = (djb2*33)+ ord(char)

    return djb2 % max_index # will provide the index in which to place a new value, delete or edit an existing one


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    # create a linkedPair
    element = LinkedPair(key,value)

    # hash the key to find the index
    idx = hash(key, hash_table.capacity)

    # check storage at index to see if there's a collision
    if hash_table.storage[idx] is None:
        hash_table.storage[idx] =  element
        return
    
    else:
        for e in hash_table.storage:
            if e.next is None:
                e.next = element
                return



# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    pass


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    pass


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    pass


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    # ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
