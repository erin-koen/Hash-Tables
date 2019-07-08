# takes a value, runs a hashing operation on it, 

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0 
        self.elements = [None] * capacity 


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    # take a string, run it through hash function, return an integer between 0 (inclusive) and max (exclusive). Max will be passed as BasicHashTable.capacity
    djb2 = 5381
    for c in string:
        djb2 = (hash*33)+ ord(c)

    return djb2 % max # will provide the index in which to place a new value, delete or edit an existing one



# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    # hash the key
    hashed_key = hash(key, hash_table.capacity)
    # check capacity vs count and resize array if needed
    if hash_table.capacity == hash_table.count:
        # create new buckets
        new_capacity = hash_table.capacity*2
        new_elements = [None] * new_capacity

        # copy over elements
        for i in range(hash_table.count):
            new_elements[i] = hash_table.elements[i]

        # set hash_table properties to new properties
        hash_table.elements = new_elements
        hash_table.capacity = new_capacity

    # insert the value at hash_table[hashed_key], handle errors
    
    # increment count
    pass


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    # hash the key
    # remove the value at hash_table[hashed_key]
    # handle errors
    # decremement count
    pass


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    # hash key - if hash_table[hashed_key], return value stored there. Else return None.
    pass


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
