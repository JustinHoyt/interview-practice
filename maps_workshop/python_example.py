# initialize map
my_map = {'name':'Jack', 'age': 26}

# add item
my_map['address'] = 'Downtown'

# update value
my_map['age'] = 27

# how to check if key is in map
if 'age' in my_map:
    print(my_map['age'])

# iterate over map
for key, value in my_map.items():
    print(key, ": ", value, sep="")
