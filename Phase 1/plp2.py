a = {'x': [1,2,3], 'y': 1, 'z': set([1,2,3]), 'w': 'qweqwe', 't': {'a': [1, 2], 'b':{'c':1}}, 'm': [1], 'l':'some key'}
b = {'x': [4,5,6], 'y': 4, 'z': set([4,2,3]), 'w': 'asdf', 't': {'a': [3, 2], 'b':{'c':1}}, 'm': "wer", 'f':{'a': '3'}}

print a, "\n", b, "\n"

def merge(dict_a, dict_b):
    print "merge", dict_a, dict_b, "\n"

    new_dict = {}

    def handle_types(value_a, value_b):
        try:
            if isinstance(value_a, dict) and isinstance(value_b, dict):
                return merge(value_a, value_b)
            elif isinstance(value_a, set) and isinstance(value_b, set):
                return value_a.union(value_b)
            else:
                return value_a + value_b
        except TypeError:
            return (value_a, value_b)

    for k in dict_a.keys():
        if dict_b.has_key(k):
            new_dict[k] = handle_types(dict_a[k], dict_b[k])
        else:
            new_dict[k] = dict_a[k]

    for k in dict_b.keys():
        if not dict_a.has_key(k):
            new_dict[k] = dict_b[k]

    print new_dict
    return new_dict


merge(a, b)
