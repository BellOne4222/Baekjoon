# 참고 : https://velog.io/@sugenius77/Python%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%AA%A8%EC%9D%8C%EC%82%AC%EC%A0%84

def solution(word):
    answer = 0
    word_list = []
    words = 'AEIOU'
    
    def dfs(cnt, w):
        if cnt == 5:
            return 
        for i in range(len(words)):
            word_list.append(w + words[i])
            dfs(cnt+1, w + words[i])
            
    dfs(0,"")
    
    return word_list.index(word)+1