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
        self.storage = [None] * capacity



# '''
# Fill this in.
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

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    # hash the key
    hashed_key = hash(key, hash_table.capacity)
    new_elem = Pair(key,value)

    # check if key already exists and handle errors
    if hash_table.storage[hashed_key]:
        print('Error, there is already a value at index {hashed_key}')
        return None
    
    # insert the value at hash_table[hashed_key], 
    hash_table.storage[hashed_key] = new_elem
    





# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    # hash the key
    hashed_key = hash(key, hash_table.capacity)
    
    # handle error
    if not hash_table.storage[hashed_key]:
        print(f'There is no value to delete at index {hashed_key}')
        return None

    # remove the value at hash_table[hashed_key]
    hash_table.storage[hashed_key] = None

    


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    hashed_key = hash(key, hash_table.capacity)
    element = hash_table.storage[hashed_key]

    return element.value if element is not None else None

def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
