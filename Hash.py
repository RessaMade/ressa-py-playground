'''
# 1. program to count similar hash values
object_list = [1, 397, 27468, -95, 1309, 397, -539874, -240767, -95, 397]

hash_count = {}

for obj in object_list:
    try:
        hash_count[hash(obj)] = hash_count.get([hash(obj)], 0) + 1
    except TypeError:
        continue

print(sum(value for value in hash_count.values() if value >1))

'''

# 2. program to creates a dictionary of objects as keys and hash values as values
objects = [1, "hello", (1, 2), [1, 2], {"a": 1}]
objects_dict = {}


for obj in objects:
    try:
        objects_dict[obj] = hash(obj)
    except TypeError:
        pass

print(objects_dict)


print(objects_dict)