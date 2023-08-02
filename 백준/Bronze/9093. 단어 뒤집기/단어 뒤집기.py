import sys

N = int(sys.stdin.readline())

for i in range(N):
    sentence = sys.stdin.readline().split()
    for j in sentence:
        print(j[::-1], end=' ')
    
    