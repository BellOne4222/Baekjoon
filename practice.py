def solution(dirs):
    start = (0,0)
    up = (0,1)
    down = (0,-1)
    left = (-1,0)
    right = (1,0)
    before = start
    check = []
    sm = 0
    road = 0
    cnt = 0
    
    for i in range(len(dirs)):
        if dirs[i] == 'U':
            sm = tuple(sum(j) for j in zip(before, up))
            road = (before,sm)
            if road not in check:
                check.append(road)
                cnt += 1
            else:
                continue
            
            
        elif dirs[i] == 'D':
            sm = tuple(sum(j) for j in zip(before, down))
            road = (before,sm)
            if road not in check:
                check.append(road)
                cnt += 1
            else:
                continue
        elif dirs[i] == 'L':
            sm = tuple(sum(j) for j in zip(before, left))
            road = (before,sm)
            if road not in check:
                check.append(road)
                cnt += 1
            else:
                continue
        else:
            sm = tuple(sum(j) for j in zip(before, right))
            road = (before,sm)
            if road not in check:
                check.append(road)
                cnt += 1
            else:
                continue
        
        before = sm
        
    return cnt
        