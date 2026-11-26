object_list = [1, 397, 27468, -95, 1309, 397, -539874, -240767, -95, 397]

hash_count = {}

for obj in object_list:
    try:
        hash_count[hash(obj)] = hash_count.get([hash(obj)], 0) + 1
    except TypeError:
        continue

print(sum(value for value in hash_count.values() if value >1))