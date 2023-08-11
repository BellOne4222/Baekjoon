from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sm_1 = sum(queue1)
    sm_2 = sum(queue2)
    all_sm = sm_1 + sm_2
    target = int(all_sm / 2)
    change = 0
    all_queue = queue1 + queue2
    cnt = len(all_queue) * 2
    p = 0  # pop 횟수
    a = 0  # append 횟수
    result = 0

    while cnt > 0:
        if p == 1 and a == 1:
            result += 1
            p = 0
            a = 0

        if sm_1 == target and sm_2 == target:
            return result
        
        if sm_1 > sm_2:
            change = queue1.popleft()
            p += 1
            queue2.append(change)
            a += 1
            sm_1 -= change
            sm_2 += change
            cnt -= 1
        elif sm_1 < sm_2:
            change = queue2.popleft()
            p += 1
            queue1.append(change)
            a += 1
            sm_1 += change
            sm_2 -= change
            cnt -= 1
        
        if p == 1 and a == 1:
            result += 1
            p = 0
            a = 0

    return -1  # 조건을 만족하는 경우가 없을 때 -1 반환

