from collections import deque

def solution(skill, skill_trees):
    essential_skills = [i for i in skill]
    essential_skill = deque(essential_skills)
    skill_sequence = [j for j in range(len(skill))]
    skill_dict = dict(zip(essential_skill,skill_sequence))
    available = 0
    cnt = 0
    
    for j in skill_trees:
        cnt = 0
        essential_skills = [i for i in skill]
        essential_skill = deque(essential_skills)
        for k in j:
            if k not in skill_dict:
                cnt += 1
            elif k == essential_skill[0]:
                cnt += 1
                essential_skill.popleft()
            else:
                break
        if cnt == len(j):
            available += 1
    return available

# print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))