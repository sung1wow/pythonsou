"""
재귀문제 :  리스트 자료 v = [7, 9, 15, 43, 32, 21] 에서 최대값 구하기 - 재귀 호출 사용 

    print(find_max(v, len(v)))
"""

# 풀이1
def find_max_1(v,idx,current_max):
    if idx == len(v):    # len(v)가 되면 다 본거임
        return current_max    # 거기서 최댓값 내놔
    
    if v[idx] > current_max:    # 지금 보고 있는 게 크면
        current_max = v[idx]    # 최댓값 지금거로 교체

    return find_max_1(v,idx+1,current_max)    # 다음거 보셈

v = [7, 9, 15, 43, 32, 21]
print(find_max_1(v,0,v[0]))    # v자료에서 0부터 시작하고, current_max는 처음값으로 시작하셈


# 풀이2
def find_max_2(v,index):

    if index == len(v) - 1:    # 지금 보고 있는게 마지막이면
        return v[index]    # 그냥 그거 내놔

    next_max = find_max_2(v, index + 1)    # 하나씩 뒤에꺼 보자

    if v[index] > next_max:    # 너가 지금 보고 있는거 > 뒤에거 이면
        return v[index]    # 지금 보고 있는 거 내놔
    else:
        return next_max    # 아니라면 뒤에거 내놔

v = [7, 9, 15, 43, 32, 21]
print(find_max_2(v,0))    # v자료에서 0부터 시작하셈




# 선생님꺼 풀이
# 재귀문제 :  리스트 자료 v = [7, 9, 15, 43, 32, 21] 에서 최대값 구하기 - 재귀 호출 사용 
# print(find_max(v, len(v)))
# for문으로 
def find_max_for(v):
    max_value = v[0]  

    for i in range(1, len(v)):  
        if v[i] > max_value: 
            max_value = v[i] 

    return max_value 

v = [7, 9, 15, 43, 32, 21]
print(find_max_for(v))

print('------------')
def find_max(v, n):
    if n == 1: 
        return v[0]   # 리스트의 첫 번째 값을 반환하고 재귀 종료
    # 재귀 호출
    prev_max = find_max(v, n - 1)
        # 앞의 (n-1)개 원소 중 최대값을 구함. 이 호출이 끝나야 아래 코드로 내려옴

    # 마지막 값과 비교
    if v[n - 1] > prev_max:
        # 현재 단계에서 마지막 원소 v[n-1]과 이전 단계에서 구한 최대값(prev_max)을 비교
        return v[n - 1]  # 마지막 값이 더 크면 그 값을 최대값으로 반환
    else:
        return prev_max 

v = [7, 9, 15, 43, 32, 21] 
print(find_max(v, len(v)))

print('-- 좀 더 파이썬 스럽게 ---')
def find_max(v, n):
    if n == 1:
        return v[0]    

    return max(
        v[n - 1],           #  현재 단계의 마지막 원소
        find_max(v, n - 1)  #  앞의 (n-1)개 중 최대값을 재귀로 구함
    )   # 두 값 중 큰 값을 반환

print(find_max(v, len(v)))
