import os
import sys

class ListSorter:
    """
    Given a file containing a list of dictionaries implement a sorting algorithm 
    (of your choosing) that will sort the list based on the dictionary keys. The dictionary
    keys will contain alphabetic characters while the values will be integers. The rule for 
    comparing dictionaries between them is:
        *   if the value of the dictionary with the lowest alphabetic key is lower than the 
        value of the other dictionary with the lowest alphabetic key, then the first 
        dictionary is smaller than the second.
        *   if the two values specified in the previous rule are equal reapply the algorithm 
        ignoring the current key. 

    The input is a file containing the list of dictionaries. Each dictionary key value 
    is specified on the same line in the form <key> <whitespace> <value>. Each list item is 
    split by an empty row. The output is a file containing a list of integers specifying the 
    dictionary list in sorted order. Each integer identifies a dictionary in the order they 
    were received in the input file.
    """

    def __init__(self, file):
        self.list = self.parse_input(file)

    def parse_input(self, input_file):

        with open(input_file, "r") as f:
            lines = "".join(f.readlines()).split("\n\n")
            
            def list_to_dict(new_dict, item):
                if isinstance(new_dict, str):
                    return {new_dict.split(" ")[0]: int(new_dict.split(" ")[1]),
                            item.split(" ")[0]: int(item.split(" ")[1])}
                else:
                    new_dict[item.split(" ")[0]] = int(item.split(" ")[1])
                    return new_dict

            def get_dict(item):
                l = item.split("\n")
                return reduce(list_to_dict, l)
            
            lst = map(get_dict, lines)


            print lst
            f.close()

        return lst

    def sort(self):
        
        self.order = [0 for i in range(len(self.list))]

        def get_dicts_keys(dict_a, dict_b):
            if not dict_a[1:] or not dict_b[1:]:
                return (dict_a[0], dict_b[0])
            elif dict_a[0] != dict_b[0]:
                return (dict_a[0], dict_b[0])
            else:
                return get_dicts_keys(dict_a[1:], dict_b[1:])


        for i in range(len(self.list)):     
            for j in range(i+1, len(self.list)):
                k1, k2 = get_dicts_keys(sorted(self.list[i].keys()), sorted(self.list[j].keys()))
                if self.list[i][k1] > self.list[j][k2]:
                    self.order[i] += 1
                else:
                    self.order[j] += 1

        print self.order
        return self

    def output_file(self):
        with open('output.txt', "w") as f:
            for i in self.order:
                f.write("%i%s" %(i, "\n"))

def main(argv=None):
    file_path = argv[0] or "%s/%s" %(os.path.dirname(os.path.realpath(__file__)), 'dicts.txt')
    if not os.path.exists(file_path):
        print("ERROR :: Input must be a valid file!!")
        sys.exit(1)

    obj = ListSorter(file_path)
    print obj.list
    obj.sort().output_file()

if __name__ == '__main__':
    main(sys.argv[1:])
