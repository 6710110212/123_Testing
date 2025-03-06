import os

def caesar_cipher(s, k):
    result = []
    
    k = k % 26
    
    for char in s:
        if 'a' <= char <= 'z':  
            new_char = chr(((ord(char) - ord('a') + k) % 26) + ord('a'))
            result.append(new_char)
        elif 'A' <= char <= 'Z': 
            new_char = chr(((ord(char) - ord('A') + k) % 26) + ord('A'))
            result.append(new_char)
        else:
            result.append(char) 
    
    return ''.join(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesar_cipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
