import sys

closed_b = {
    "}": "{",
    "]": "[",
    ")": "("
}


def check_balanced(braces):
    st = []
    for b in braces:
        if b in closed_b:
            if len(st) and st[-1] == closed_b[b]:
                st.pop()
            else:
                return False
        else:
            st.append(b)
    return len(st) == 0


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    for i in range(n):
        braces = sys.stdin.readline().strip()
        print "YES" if check_balanced(braces) else "NO"
