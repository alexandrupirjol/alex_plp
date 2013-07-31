import sys
import ast

{'b':1, 1:'a'}

def is_immutable(obj):
    print obj
    def check_immutable(base_obj):
        if isinstance(base_obj, (str, int, long, float, complex, bool, type(None))):
            return True
        else:
            return False

    if isinstance(obj, tuple):
        for i in obj:
            if not is_immutable(i):
                return False
        return True
    else:
        return check_immutable(obj)

def swap(d):
    
    try:
        d = ast.literal_eval(d)
    except ValueError:
        print "ERROR :: Invalid input type!"
        sys.exit(1)

    if len(d) != len(set(d.values())):
        print "Swap is not possble : duplicate values"
        sys.exit(1)

    for v in d.values():
        if not is_immutable(v):
            print "Swap is not possible : mutable value"
            sys.exit(1)

    print dict (zip(d.values(),d.keys()))





if __name__ == '__main__':
    swap(sys.argv[1])

