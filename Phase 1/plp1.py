list1 = [[1], [2, 3], ["4", [5, [6, [{"some_key":3, "key":4}, [8]]]]]]
list2 = [[1], [2, 3], [4, [5, [6, [7, [8, [9]]]]]]]

print list1, "\n", list2, "\n"

def is_flat(l):
    return all(not isinstance(el, list) for el in l)

def flatten(list1, list2, max_depth):
    print "flatten\n", list1, "\n", list2
    def f(x, y):
        if isinstance(x, list) and isinstance(y, list):
            return x + y
        elif isinstance(x, list) and not isinstance(y, list):
            return x + [y]
        elif not isinstance(x, list) and isinstance(y, list):
            return [x] + y
        else:
            return [x] + [y]

    if max_depth == 0 or (is_flat(list1) and is_flat(list2)):
        return list1, list2
    else:
        flatten(reduce(f , list1), reduce(f, list2), max_depth -1)

flatten(list1, list2, 7)
