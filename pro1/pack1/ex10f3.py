# 매개변수 유형
# 위치 매개변수 : 인수와 순서대로 대응
# 기본값 매개변수 : 매개변수에 입력값이 없으면 기본값 사용
# 키워드 매개변수 : 실인수와 가인수 간 동일 이름으로 대응
# 가변 매개변수 : 인수의 갯수가 동적인 경우

def showGugu(start, end=5):
    for dan in range(start, end + 1, 1):
        print(str(dan) + '단 출력')
        for i in range(1, 10):
            print(str(dan) + "*" + \
                  str(i) + "=" + str(dan * i), end = ' ')    # \는 줄이 길어서 다음 줄로 이어쓰기 한다는 뜻
            
        print()

showGugu(2, 3)    # 일반적인 형태, 값 2개가 필요하니 값 2개를 줌
print()
showGugu(2)    # def에 end=5가 있으므로 값이 비어도 상관없음
print()
showGugu(start=7, end=9)    # 인수가 바뀌어도 상관없음
print()
showGugu(end=9, start=7)    # 순서가 바뀌어도 상관없음
print()
showGugu(7, end=9)
# showGugu(start=7, 9)    # 문법 오류, 이름 붙인 인자 뒤에는 위치 인자를 쓸 수 없다.
# showGugu(end=9, 7)    # SyntaxError: positional argument follows keyword argument

print('가변 매개변수'+'----'*10)
def func1(*ar):    # *: 여러 개의 인자를 tuple로 묶어서 받겠다는 의미
    print(ar)
    for i in ar:
        print('밥 : ' + i)

func1('김밥', '비빔밥', '볶음밥')    # ('김밥', '비빔밥', '볶음밥')
func1('김밥', '비빔밥', '볶음밥', '공기밥')
func1('김밥')    # ('김밥',) 로 출력됨, 즉 쉼표가 김밥뒤에 붙음
print()
def func2(a, *ar):
# def func2(*ar,a):    # 실행오류 : TypeError: func2() missing 1 required keyword-only argument: 'a'
    print(a)
    print(ar)

func2('김밥', '비빔밥')
func2('김밥', '비빔밥', '볶음밥', '공기밥')

print()
def func3(w, h, **other):
    print(f'몸무게 : {w}, 키 : {h}')
    print(f'기타 : {other}')

func3(80,180, irum = '신기루', nai = 23)
# func3(80,180, {'irum' : '신기루', "nai" : 23})    # “키워드 인자”로 주느냐, “딕셔너리 한 덩어리”로 주느냐

print()
def func4(a, b, *c, **d):
    print(a, b)
    print(c)
    print(d)

func4(1,2)
func4(1,2,3,4,5)
func4(1,2,3,4,5, kbs=9, mbc=11)

print()
# type hint :  함수의 인자와 반환값에 type을 적어 가독성 향상
def typeFunc(num:int, data:list[str]) -> dict[str, int]:    # “이런 타입이 들어오고 이런 타입이 나간다”는 안내판
    print(num)
    print(data)
    result = {}
    for idx, item in enumerate(data, start=1):
        print(f'idx:{idx}, item:{item}')
        result[item] = idx 
    return result

rdata = typeFunc(1, ['일', '이', '삼'])
print(rdata)
print()
rdata = typeFunc("한개", [10,20,30])
print(rdata)


