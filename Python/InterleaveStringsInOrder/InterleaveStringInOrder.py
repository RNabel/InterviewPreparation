def print_interleaved_strings_rec(left, right, current):
    if not len(left) and not len(right):
        print current

    if len(left):
        result = current + left[0]
        print_interleaved_strings_rec(left[1:], right, result)

    if len(right):
        result = current + right[0]
        print_interleaved_strings_rec(left, right[1:], result)

if __name__ == '__main__':
    print_interleaved_strings_rec("AB", "CD", "")
    print_interleaved_strings_rec("AB", "C", "")
