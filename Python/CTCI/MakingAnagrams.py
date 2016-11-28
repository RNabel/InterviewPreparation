import sys


def get_frequencies(a):
    output = [0] * 27
    offset = ord('A')

    for letter in a:
        index = ord(letter) - offset
        output[index] += 1

    return output


def get_count(a, b):
    a = a.upper()
    b = b.upper()
    frq_a = get_frequencies(a)
    frq_b = get_frequencies(b)

    count = 0

    for i_a, i_b in zip(frq_a, frq_b):
        count += abs(i_a - i_b)

    return count


if __name__ == '__main__':
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()

    print get_count(a, b)
