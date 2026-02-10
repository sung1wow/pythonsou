# 반복문 for
# for i in [1,2,3,4,5]:
# for i in (1,2,3,4,5):
for i in {1,2,3,4,5}:   # set은 순서가 없으므로 순서대로 안 찍힐 수도 있음 
    print(i, end = ' ')

print('분산/표준편차 ---')
# numbers = [1,3,5,7,9]   # 합은 25, 평균은 5.0
# numbers = [3,4,5,6,7]   # 합은 25, 평균은 5.0
numbers = [-3,4,5,7,12]   # 합은 25, 평균은 5.0
tot = 0
for a in numbers:
    tot += a
print(f"합은 {tot}, 평균은 {tot / len(numbers)}")
avg = tot / len(numbers)
# 편차의 합
hap = 0
for i in numbers:
    hap += (i - avg) **2
print(f'편차 제곱의 합 {hap}')
vari = hap / len(numbers)
print(f'분산은 {vari}')
print(f'표준편차 {vari ** 0.5}')

print()
colors = ['r', 'g', 'b']
for v in colors:
    print(v, end = ' ')

print('iter() : 반복 가능한 객체를 하나씩 꺼낼 수 있는 상태로 만들어 주는 함수')
iterator = iter(colors)
for v in iterator:
    print(v, end = ', ')

print()
for idx, d in enumerate(colors):    # 인덱스와 값을 반환
    print(idx, ' ', d)

print('\n사전형---')
datas = {'python':'만능언어', 'java':'웹용언어', 'mariadb':'RDBMS'}
for i in datas.items():
    # print(i)
    print(i[0], ' ~~ ', i[0])

for k, v in datas.items():
    print(k, ' -- ', v)

for k in datas.keys():
    print (k, end = ' ')

print()
for val in datas.values():
    print (val, end = ' ')

print('\n다중 for ----------------')
for n in [2,3]:
    print('--{}단--'.format(n))
    for i in [1,2,3,4,5,6,7,8,9]:
        print('{} * {} = {}'.format(n, i, n * i))

print('continue, break -------')
nums = [1,2,3,4,5]
for i in nums:
    if i == 2:continue
    # if i == 4:break
    print(i, end = ' ')
else:
    print('정상종료')

print('\정규 표현식 + for')
str = """
미국에서 혹한 속에 태어난 송아지가 세 살배기 아기와 함께 소파에서 낮잠을 자는 모습이 공개돼 훈훈함을 자아냈다.
CNN 방송과 워싱턴포스트(WP) 등 미국 매체는 지난 1월31일(현지시간) 켄터키주 마운트 스털링의 한 농가에서 있었던 일화를 전했다.
이곳에서 농장을 운영하는 태너 소렐은 같은 달 24일 눈발이 쏟아지는 날 출산이 임박한 어미 소의 상태를 살피러 나갔다가 송아지가 이미 태어난 것을 발견했다.
"""
import re 
str2 = re.sub(r'[^가-힣\s]','', str)    # 한글과 공백 이외의 문자는 공백처리
print(str2)
str3 = str2.split(' ')  # 공백을 구분자로 문자열 분리
print(str3)
cou = {}
for i in str3:
    if i in cou:
        cou[i] += 1    # 같은 단어가 있으면 누적
    else:
        cou[i] = 1    # 최초 단어인 경우는 '단어':1
print(cou)

print('정규 표현식 좀 더 연습 ')
for test_ss in ['111-1234', '일이삼-일이삼사', '222-1234', '333&1234']:
    if re.match(r'^\d{3}-\d{4}$', test_ss):   # \d : 숫자, ^ : 숫자로 시작해야 돼, $ : 이렇게 끝나야 돼
        print(test_ss, '전화번호 맞아요')
    else:
        print(test_ss, '전화번호 아니야')

print('comprehension : 반복문 + 조건문 + 값 생성을 한 줄로 표현')
a = [1,2,3,4,5,6,7,8,9,10]
li = []
for i in a:
    if i % 2 == 0:
        li.append(i)
print(li)
print(list(i for i in a if i % 2 == 0))    # 위 4개줄과 동일한 코딩임

datas = [1, 2, 'a', True, 3.0]
datas = {1, 2, 'a', True, 3.0, 2, 1, 2, 1, 2, 2}
li2 = [i * i for i in datas if type(i) == int]
print(li2)
############################################################### 이해 못함 
id_name = {1:'tom', 2:'oscar'}
name_id = {val:key for key, val in id_name.items()}
print(name_id)
print()
print([1,2,3])
print(*[1,2,3])    # * : unpack
aa = [(1,2), (3,4), (5,6)]
for a, b in aa:
    print(a + b)

print([a + b for a, b in aa])    # [3, 7, 11]
print(*[a + b for a, b in aa], sep='\n')

print('\n수열 생성 : range')
print(list(range(1, 6)))    # [1, 2, 3, 4, 5]
# print(list(range(1, 6, 1)))    # (1, 3, 5)
print(tuple(range(1, 6, 2)))    # (1, 3, 5)
print(list(range(-10, -100, -20)))    # [-10, -30, -50, -70, -90]
print(set(range(1, 6)))    # {1, 2, 3, 4, 5}
print()
for i in range(6):
    print(i, end = ' ')    # 0 1 2 3 4 5

for _ in range(6):    # _ : 가독성을 위해서
    print('반복')

tot = 0 
for i in range(1, 11):
    tot += i
print('tot : ', tot)
print('tot : ', sum(range(1, 11)))    # sum() : 내장함수

for i in range(1, 10):
    print(f'2 * {i} = {2 * i}')

# 문1 : 2 ~ 9 구구단 출력 (단은 행 단위 출력)

for gugudan in range(1,10):
    for h in range(1,10):
        print(f' {h} * {gugudan} = {h * gugudan}')
    

for i in range(2, 10):
    for j in range(1, 10):
        print(f'{i} * {j} = {i * j}', end = ' ')
        print()


# 문2 : 주사위를 두 번 던져서 나온 숫자들의 합이 4의 배수가 되는 경우만 출력

for i in range(6):
    n1 = i + 1
    for j in range(6):
        n2 = j + 1
        n = n1 + n2
        if n%4 == 0:
            print(n1, n2)

print()
for i in range(1, 7, 1):    # 짧은 버전
    for j in range(1, 7, 1):
        su = i + j
        if su%4 == 0: print(i, j)

print('\nend')