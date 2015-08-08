import itertools
import sys

test_cases = open(sys.argv[1], 'r')

def permute(the_string):
    # turn string into sorted array of chars
    arr = [c for c in the_string]
    arr.sort()
    # then get all possible permutations, itertools implementation
    # gives us the desired ordering, no more work to do
    return [''.join(p) for p in itertools.permutations(arr, len(arr))]

for test in test_cases:
    if test == "":
        continue
    permutations = permute(test.strip())
    print(','.join(permutations))
