import sys


def add(val, h_map):
    h_map[0] += 1
    c, h_map = h_map
    if len(val):
        first = val[0]
        val = val[1:]

        if first in h_map:
            inner_map = h_map[first]
        else:
            inner_map = [0, {}]
            h_map[first] = inner_map

        add(val, inner_map)


def find(val, h_map):
    c, h_map = h_map
    if len(val):
        first = val[0]
        val = val[1:]
        if first in h_map:
            return find(val, h_map[first])
        else:
            print 0
            return 0

    else:
        print c
        return c


handlers = {
    "add": add,
    "find": find
}

if __name__ == '__main__':
    # Set up trie.

    n = int(sys.stdin.readline())
    trie = [0, {}]
    for i in range(n):
        # Get user input.
        line = sys.stdin.readline().strip()
        tokens = line.split(" ")
        # Input validation.
        if len(tokens) == 2:
            handlers[tokens[0]](tokens[1], trie)

        elif len(tokens) == 1 and tokens[0] == "find":
            print 0
