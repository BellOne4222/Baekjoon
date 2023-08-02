import sys

N = int(sys.stdin.readline())

for i in range(N):
    stack = []
    sentence = sys.stdin.readline()
    flag = True
    for j in range(len(sentence)):
        if sentence[j] == '(':
            stack.append(sentence[j])
        elif sentence[j] == ')':
            if stack:
                stack.pop()
            else:
                flag = False
                break
    if not stack and flag:
        print('YES')
    elif stack or not flag:
        print('NO')
        
    