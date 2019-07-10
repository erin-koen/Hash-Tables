

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
        self.storage = [None] * capacity
        self.count = 0


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max_index):
    # take a string, run it through hash function, return an integer between 0 (inclusive) and max (exclusive). Max will be passed as BasicHashTable.capacity
    djb2 = 5381
    for char in string:
        djb2 = (djb2*33) + ord(char)

    # will provide the index in which to place a new value, delete or edit an existing one
    return djb2 % max_index


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    # create a linkedPair
    element = LinkedPair(key, value)

    # hash the key to find the index
    idx = hash(key, hash_table.capacity)


    # check storage at index to see if there's a collision, and just insert the elemnt if the index is empty
    if hash_table.storage[idx] is None:
        hash_table.storage[idx] = element
        return
    
    # otherwise traverse till you find an empty spot
    curr_node = hash_table.storage[idx]
    while curr_node.next is not None:
        curr_node = curr_node.next
    
    # and stick in the element when you get there
    curr_node.next = element


def hash_table_remove(hash_table, key):
    # hash the key to find the index
    idx = hash(key, hash_table.capacity)
    # if there's nothing there, print it out and let 'em know
    if hash_table.storage[idx] is None:
        print(f'There is no key: value pair at that index.')
        return None
    # if there's only one ListNode, and its key is equal to that which was passed, set it to None
    if hash_table.storage[idx].next is None and hash_table.storage[idx].key == key:
        hash_table.storage[idx] = None
        print(f'The item was found and deleted.')
        return None

    # set a variable to track the node you're traversing TO, start with the second node, since we've satisfied the conditionals above
    curr_node = hash_table.storage[idx].next

    # figure out how to traverse through the LL till you find the key
    while curr_node.next.key is not key:

        # set curr node to the next node
        curr_node = curr_node.next

        # if you get to the end of the list, print an error and return
        if curr_node.next is None:
            print(f'No pair with that key was found.')
            return

    # if you get this far it's because the next node's key is what you're looking for. Change the reference in curr_node.next to point to the pair two spots ahead of it
    curr_node.next = curr_node.next.next


# Should return None if the key is not found.
def hash_table_retrieve(hash_table, key):
    # hash the key to find the index
    idx = hash(key, hash_table.capacity)
    curr_node = hash_table.storage[idx]
    while curr_node.key is not key:
        if curr_node.next is None:
            print(f'That key does not exist.')
            return None
        curr_node = curr_node.next
    # if you've gotten here it's because the current node is the one you're looking for. Return it.
    return curr_node


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

    # old_capacity = len(ht.storage)
    # ht = hash_table_resize(ht)
    # new_capacity = len(ht.storage)

    # print("Resized hash table from " + str(old_capacity)
    #       + " to " + str(new_capacity) + ".")


Testing()
