# A more Pythonic approach ... I think ...

a = {'x': [1,2,3], 'y': 1, 'z': set([1,2,3]), 'w': 'qweqwe', 't': {'a': [1, 2], 'b':{'c':1}}, 'm': [1], 'l':'some key'}
b = {'x': [4,5,6], 'y': 4, 'z': set([4,2,3]), 'w': 'asdf', 't': {'a': [3, 2], 'b':{'c':1}}, 'm': "wer", 'f':{'a': '3'}}

print a, "\n", b, "\n"

def merge(dict_a, dict_b):
    print "merge", dict_a, "\n", dict_b, "\n"


    def handle_types(value_a, value_b):
        if value_a is None:
            return value_b
        elif value_b is None:
            return value_a

        if type(value_a) == type(value_b):
            if isinstance(value_a, dict) and isinstance(value_b, dict):
                return merge(value_a, value_b)
            elif isinstance(value_a, set) and isinstance(value_b, set):
                return value_a.union(value_b)
            else:
                return value_a + value_b 
        else:
            return (value_a, value_b)

    new_dict = dict((k, handle_types(dict_a.get(k), dict_b.get(k))) for k in set(dict_a).union(set(dict_b)))
    print new_dict
    return new_dict


merge(a, b)
