import os

def funnyString(s):
     # Write your code here
    n = len(s)
    
    original_diffs = [abs(ord(s[i]) - ord(s[i-1])) for i in range(1, n)]
    reverse_diffs = [abs(ord(s[n-i]) - ord(s[n-i-1])) for i in range(1, n)]

    if original_diffs == reverse_diffs:
        return "Funny"
    else:
        return "Not Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()