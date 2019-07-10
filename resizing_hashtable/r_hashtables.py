

class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None



class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.count = 0


def hash(string, max_index):
    # take a string, run it through hash function, return an integer between 0 (inclusive) and max (exclusive). Max will be passed as BasicHashTable.capacity
    djb2 = 5381
    for char in string:
        djb2 = (djb2*33) + ord(char)

    # will provide the index in which to place a new value, delete or edit an existing one
    return djb2 % max_index



def hash_table_insert(hash_table, key, value):
    # create a linkedPair
    element = LinkedPair(key, value)

    # hash the key to find the index
    idx = hash(key, hash_table.capacity)
    # check storage at index to see if there's a collision, and just insert the elemnt if the index is empty
    if hash_table.storage[idx] is None or hash_table.storage[idx].key is key:
        hash_table.storage[idx] = element
        return
    # traverse the LL, if you find the key already exists, overwrite the value. If it doesn't exist, add it to the end.
    # prev_node = hash_table.storage[idx]
    curr_node = hash_table.storage[idx].next

    while curr_node is not None:
        if curr_node.key is key:
            element.next = curr_node.next
            curr_node = element
            return
        if curr_node.next is None:
            curr_node.next = element
            print('DFJKLSFJDSKL', element.value)
        curr_node = curr_node.next 
    
   


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
    # set a variable to track where we've been
    prev_node = hash_table.storage[idx]
    # figure out how to traverse through the LL till you find the key
    while curr_node is not None:
        if curr_node.key is key:
            prev_node.next = curr_node.next
            print(f'The item with key {key} was found and deleted.')
            return
        prev_node = curr_node
        curr_node = curr_node.next

    # if you get to the end of the list, print an error and return
    print(f'No pair with that key was found.')
    return



# Should return None if the key is not found.
def hash_table_retrieve(hash_table, key):
    # hash the key to find the index
    idx = hash(key, hash_table.capacity)
    curr_node = hash_table.storage[idx]
    while curr_node is not None:
        print('curr_node value', curr_node.value)
        if curr_node.key is key:
            return curr_node.value
        curr_node = curr_node.next
    # if you've gotten here it's because the current node is the one you're looking for. Return it.
    print(f'The item with key {key} was not found.')
    return None


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    # double size of capacity
    new_cap = hash_table.capacity * 2

    # create a new hash table with that capacity
    new_ht = HashTable(new_cap)

    # loop through the existing storage, then traverse through each list at each index
    for item in hash_table.storage:
        print('item', item)
        curr_node = item
        while curr_node is not None:
            # call the insert method to stick it in the new ht
            hash_table_insert(new_ht, curr_node.key, curr_node.value)
            # move on to the next node
            curr_node = curr_node.next
    # when you've done this at every index, return the new ht
    return new_ht


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
