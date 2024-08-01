my_dict = {'Alex': 1971, 'Mari': 1999}
print('Dict:', my_dict)
print('Existing value:', my_dict['Alex'])
print('Not existing value:', my_dict.get('Leam'))
my_dict.update({'Kirill': 2001, 'Tasha': 2003})
a = my_dict.pop('Mari')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)

# Множество
my_set = {1, 2, 'apple', 56.676, 1, 2, 'apple', 56.676, 1, 'apple'}
print('Set:', my_set)
my_set.remove('apple')
my_set.add((1, 2, 3, 4))
print('Modified set:', my_set)