from collections import Counter

def solution(topping):
    elder = Counter(topping)
    
    younger = set()
    case = 0
    
    for i in topping:
        younger.add(i)
        elder[i] -= 1

        if elder[i] == 0:
            del elder[i]
        if len(younger) == len(elder):
            case += 1

    return case


# print(solution([1, 2, 1, 3, 1, 4, 1, 2]))