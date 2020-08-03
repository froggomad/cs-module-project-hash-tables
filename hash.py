def hash(str, list_size):
    #str to bytes
    bytes_representation = str.encode()

    sum = 0
    for byte in bytes_representation:
        sum += byte
    #return remainder of sum/list_size (or lhs if rhs is greater)
    return sum % list_size

#init list
my_list = [None] * 5

#setter
my_list[hash("aqua", len(my_list))] = "#00FFFF"
#getter
print(my_list[hash("aqua", len(my_list))])


# my goal here is to make the function more dynamic by just passing the list in and letting
# the function determine the length
# this probably does a number on storage complexity though
HASH_DATA_SIZE = 4
hash_data = [None] * HASH_DATA_SIZE

def stretch_hash(str):
    bytes_representation = str.encode()

    sum = 0
    for byte in bytes_representation:
        sum += byte
        #restrict max number
        #total &= 0xffffffff # 32 bit
        total &= 0xffffffffffffffff #64 bit
    #return remainder of sum/list_size (or lhs if rhs is greater)
    return sum

def get_index(s):
    hash_value = stretch_hash(s)

    return hash_value % HASH_DATA_SIZE

def put(k, v):
    index = get_index(k)
    hash_data[index] = v

def get(k):
    index = get_index(k)
    return hash_data[index]

put("Kenny", "Hello, world!")
put("nada", "nothing")
put("another", "some")
print(get("Kenny"))
print(get("nada"))
print(get("another"))


# TODO: