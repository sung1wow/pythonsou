# 사용자 정의 함수
"""
def 함수명(가인수,,,):
    # ...
    return 반환값    # 1개만 반환, return이 없으면 return None

함수명(실인수,,,)    # 함수 호출
"""

def doFunc1():
    print('doFunc1 수행')

def doFunc2(name):
    print('name : ', name)
    # return None

def doFunc3(arg1, arg2):
    re = arg1 + arg2
    return re

def doFunc4(a1, a2):
    imsi = a1 + a2
    if imsi % 2 == 1:
        return
    else:
        return imsi

doFunc1()    # 함수 호출 - 함수를 수행하세요
print('함수 주소는', doFunc1)    # 주소가 찍힘, 함수 이름도 변수이기 때문에 (참조형임)
print('함수 주소는', id(doFunc1))
imsi = doFunc1    # 괄호 여부에 따라 주소를 가지고 올지 수행할지 달라짐
imsi()
print(doFunc1())    # 함수를 수행하고, 뭐를 들고 온거임 (들고 올게 없어서 None)
print('------'*6)
doFunc2(7)
# doFunc2("길동", "순신")
print('------'*6)
doFunc3("대한", "민국")
print(doFunc3("대한", "민국"))
print(doFunc3(5,6))
result = doFunc3("5","6")
print(result)

print(doFunc4(3, 4))
print(doFunc4(3, 5))

print('------'*6)
def triArea(a, b):
    c = a * b / 2
    triAreaPrint(c)    # 다른 함수 호출 

def triAreaPrint(cc):
    print('삼각형의 면적은 ', cc)

triArea(20, 30)

print('------'*6)
def passResult(kor, eng):
    ss = kor + eng
    if ss >= 50:
        return True
    else:
        return False

if passResult(20, 50):
    print('합격')
else:
    print('불합격')

print()
def swapFunc(a, b):
    return b, a    # return (b, a)

a = 10; b = 20
print(a, ' ', b)
print(swapFunc(a, b))

print()
def funcTest():
    print('funcTest 멤버 처리')
    def funcInner():
        print('내부 함수')
    funcInner()

funcTest()

# if 조건식 안에 함수 사용
def isOdd(para):
    return para%2 == 1    # 홀수이면 True 반환

mydict = {x:x * x for x in range(11) if isOdd(x)}
print(mydict)

print('변수의 생존 범위 (scope rule)----')
# 변수가 저장되는 이름공간은 변수가 어디서 선언 되었는가에 따라 생존 시간이 다름
# 전역, 지역 변수
# Local -> Enclosing function -> Global -> Built-in

player = '전국대표'    # 전역변수 ( 현재 모듈 어디서든 호출 가능), 근데 전역에 없으면 못 찾아냄
name = '한국인'

def funcSoccer():
    name = '홍길동'    # 지역변수 ( 현재 함수 내에서만 호출 가능), 근데 지역에 없으면 전역을 뒤져서 찾아냄
    # player = '지역대표'
    city = '서울'
    print(f'이름은 {name} 수준은 {player}')    # 이름은 홍길동 수준은 지역대표
    print(f'지역은 {city}')

funcSoccer()
print(f'이름: {name}, 수준: {player}')    # 이름: 한국인, 수준: 전국대표
# print(f'지역은 {city}')    # 즉, 얘는 지역 변수이므로 여기서 처리 불가함

print()
a = 10; b = 20; c = 30
def Foo():
    a = 7    # 지역 변수
    b = 100
    def Bar():
        global c    # Bar 함수의 멤버가 아니라 모듈(파일)의 멤버가 됨. 전역변수
        nonlocal b    # 바로 위 함수의 지역 변수로 변환
        b = 8    # 지역 변수
        print(f'Bar 수행 후 a:{a}, b:{b}, c:{c}')
        c = 9
        b = 200
    Bar()
    print(f'Foo 수행 후 a:{a}, b:{b}, c:{c}')

Foo()
print(f'함수 수행 후 a:{a}, b:{b}, c:{c}')

print()
g = 1
def func():
    global g    # 아래 항의 이유로 g한테 값을 주기 위해 글로벌 g값을 가져옴
    a = g    # g는 아무런 값도 가지고 있지 않는데 a한테 값을 줄려고 하니까 에러가 나는 거임
    g = 2
    return a

print(func())