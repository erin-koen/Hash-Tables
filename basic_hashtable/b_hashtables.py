
from doubly_linked_list import (
    ListNode,
    DoublyLinkedList
)

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# initialize HT with storage set to a list of DLLs
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [DoublyLinkedList()] * capacity



# Hash function unchanged
def hash(string, max_index):
    # take a string, run it through hash function, return an integer between 0 (inclusive) and max (exclusive). Max will be passed as BasicHashTable.capacity
    djb2 = 5381
    
    for char in string:
        djb2 = (djb2*33)+ ord(char)

    return djb2 % max_index # will provide the index in which to place a new value, delete or edit an existing one




def hash_table_insert(hash_table, key, value):
    # create a Pair
    element = Pair(key, value)

    # hash the key of the element to find which index to put it in
    idx = hash(element.key, hash_table.capacity)

    # check the DLL at the index to see if there's anything in it, add the element to the head if not, and to the tail if so.
    if hash_table.storage[idx].length == 0:
        hash_table.storage[idx].add_to_head(element)
    else: 
        hash_table.storage[idx].add_to_tail(element)







def hash_table_remove(hash_table, key):
    
    # hash the key
    idx = hash(key, hash_table.capacity)

    # check if there's anything in the list at that index
    if hash_table.storage[idx].length == 0:
        print(f'There is no value to delete at index {idx}')
        return None



    
    


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
