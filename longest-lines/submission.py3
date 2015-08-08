import sys
f = open(sys.argv[1], 'r')

k = int(f.readline())

long_lines = [''] * k

line_number = 0
for this_line in f:
    # if we haven't read k lines let, than this line should go in the
    # stack
    if line_number < k:
        long_lines.append(this_line.strip())
        line_number += 1
        continue
    # once we fill our stack, we need to sort it because we depend on
    # this fact later
    if line_number == k:
        long_lines.sort(key=len)
        long_lines.reverse()
    # continue processing
    if len(this_line.strip()) > len(long_lines[k-1]):
        # insert this line into long lines at a point in the list
        # such that it is still sorted
        idx = k - 1
        while idx > 0 and len(long_lines[idx-1]) < len(this_line.strip()):
            idx -= 1
        long_lines = long_lines[:idx] + [this_line.strip()] + long_lines[idx:-1]
    line_number += 1

# print out the longest lines
for line in long_lines:
    print(line)
