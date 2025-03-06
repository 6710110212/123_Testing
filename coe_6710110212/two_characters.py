import os
from itertools import combinations

def is_alternating(t):
    for i in range(1, len(t)):
        if t[i] == t[i - 1]:
            return False
    return True

def alternate(s):
    max_length = 0
    unique_chars = set(s)
    
    for char1, char2 in combinations(unique_chars, 2):
        filtered_string = [char for char in s if char == char1 or char == char2]
        
        if is_alternating(filtered_string):
            max_length = max(max_length, len(filtered_string))
    
    return max_length

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())
    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')
    fptr.close()
