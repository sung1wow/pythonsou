# Closure : Scope에 제약을 받지 않는 변수들을 포함하고 있는 코드블럭이다.
# 내부 함수의 주소를 변환해 함수 밖에서 함수 내의 멤버를 참조하기

def funcTimes(a, b):
    c = a * b
    return c

print(funcTimes(2, 3))
# print(c)    c는 함수 안에서만 존재하는 변수(지역 변수), 함수가 끝나는 순간 사라져서 값이 없음

kbs = funcTimes(2, 3)
print(kbs)    # 값, 즉 6을 출력
kbs = funcTimes
print(kbs)    # 함수를 가리키는 변수를 출력
print(kbs(2, 3))    # 값, 즉 6을 출력
print(funcTimes(2, 3))    # 함수가 아직 살아있음 값, 즉 6을 출력
print(id(kbs)), id(funcTimes)    # kbs와 funcTimes는 값은 함수를 가리키므로 같은 주소를 가짐
mbc = sbs = kbs
del funcTimes     # funcTimes 변수 삭제 (이름이 사라진거임, 함수가 사라진 건 아님)
# print(funcTimes(2, 3))    #NameError: name 'funcTimes' is not defined, 이름을 못 찾는 거
print(mbc(2, 3))    # mbc는 여전히 참조 함수를 가지고 있기 때문에 값이 출력됨

#######################################################################
print('\n--클로저를 사용하지 않은 경우-------')
def out():
    count = 0
    def inn():
        nonlocal count    # 바깥 함수의 count를 사용하겠다
        count += 1
        return count    # 1이 반환됨
    print(inn())    # 1이 출력됨

# print(count)    # err
out()    # 이게 끝나면 count는 사라짐
out()    # 즉, 또 다시 함수를 불러도 0부터 시작하는 거임

print('\n--클로저를 사용한 경우-------')
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count    # 1이 반환됨
    return inner    # <== 요게 클로저 : 내부 함수의 주소를 밖으로 반환

var1 = outer()    # 내부함수의 주소를 변수에 저장, var1은 함수 그 자체, var1()은 함수를 실행한 결괏값 
print('var1 주소:', var1)
print(var1())
print(var1())
myvar = var1()    # 지번주소, 도로명주소 다르지만 위치는 동일한 거랑 비슷함
print(myvar)
print()
var2 = outer()    # 새로운 객체(inner 함수) 생성
print(var2())
print(var2())

print(var1, var2)    # 기능은 같지만 주소는 다름, 즉 별도로 돌아가며 count 값이 다름

print('수량 * 단가 * 세금 한 결과를 출력하는 함수 작성')
def outer2(tax):     # tax는 지역 변수
    def inner2(su, dan):
        amount = su * dan * tax
        return amount
    return inner2

# 1분기에는 su * dan에 대한 tax는 0.1 부과
q1 = outer2(0.1)    # inner2의 주소를 기억한다
result1 = q1(5, 50000)
print('result1 :', result1)
result2 = q1(2, 10000)
print('result2 :', result2)
print()
# 2분기에는 su * dan에 대한 tax는 0.05 부과
q2 = outer2(0.05)
result3 = q2(5, 50000)
print('result3 :', result3)
result4 = q2(2, 10000)
print('result4 :', result4)

print('\n 일급함수 : 함수 안의 함수, 인자로 함수 전달, 반환값이 함수')
def func1(a, b):
    return a + b

func2 = func1
print(func1(3, 4))
print(func2(3, 4))
print()
def func3(fu):    # 인자로 함수 전달
    def func4():    # 함수 안의 함수를 선언
        print('나는 내부함수야~~')
    func4()
    return fu    # 반환값이 함수

mbc = func3(func1)
print(mbc(3, 4))

print('\n축약함수(Lambda function) : 이름이 없는 한 줄짜리 함수')
# 형식 : lambda 매개변수들,,,:반환식     <= return 없이 결과 반환, 잠깐 쓸 짧은 함수를 빠르게 만들기 위해서
def hapFunc(x, y):
    return x + y
print(hapFunc(1,2))
# 람다로 표현
print((lambda x, y:x + y)(1,2))

gg = lambda x, y: x + y
print(gg(1, 2))

kbs = lambda a, su=10: a + su
print(kbs(5))
print(kbs(5, 6))    # su는 10을 가질 수 있었지만 6으로 바꿈

sbs = lambda a, *tu, **di:print(a, tu, di)
sbs(1, 2, 3, var1=4, var2=5)    # a → 첫 번째 값 하나, *tu → 나머지 위치 인자들 전부 튜플(tuple) 로 묶기, **di → 키워드 인자들 전부 딕셔너리(dict) 로 묶기, 그리고 print(a, tu, di) 실행

li = [lambda a,b : a + b, lambda a,b : a * b]
print(li[0](3,4))    # li 안에는 숫자나 문자열이 아니라 “함수”가 들어 있음, 리스트의 첫 번째 함수 실행
print(li[1](3,4))    # 리스트의 두 번째 함수 실행

print('\n다른 함수에서 람다 사용하기')
# filter(함수, 반복가능한 개체)
print(list(filter(lambda a: a<5, range(10))))
print(list(filter(lambda a: a%2, range(10))))    # 0은 False, 1은 True 취급해서, 홀수만 남음

# 문) filter를 이용해 1 ~ 100 사이의 정수 중 5의 배수이거나 7의 배수만 출력
print(list(filter(lambda a : a%5 == 0 or a%7 == 0, range(1, 101))))