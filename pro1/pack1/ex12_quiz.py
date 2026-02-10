# 연습문제1) 리스트를 통해 직원 자료를 입력받아 가공 후 출력하기

"""
연습문제1) 리스트를 통해 직원 자료를 입력받아 가공 후 출력하기

함수를 두 개 작성

# 입력 함수 :  [사번, 이름, 기본급, 입사년도]
def inputfunc():
    datas = [
        [1, "강나루", 1500000, 2010],
        [2, "이바다", 2200000, 2018],
        [3, "박하늘", 3200000, 2005],
    ]
    return datas


처리 함수 : processfunc(datas) : datas에 기억된 내용을 출력한다.

처리 조건 : 

 1) 급여액은 기본급 + 근속수당 

 2) 수령액은 급여액 - 공제액

* 근무년수에 대한 수당표	* 급여 상한액에 대한 공제세율표
근무년수     근속수당
 0~3년        150000
 4~8년        450000
 9년 이상    1000000	급여액                공제세율
300만원 이상          0.5
200만원 이상          0.3
200만원 미만          0.15


출력 결과 : 

사번  이름    기본급    근무년수  근속수당  공제액    수령액
-------------------------------------------------------------------------------
1    강나루    1500000   16       1000000   750000   1750000
2    이바다    2200000   8          450000    795000   1855000
3    박하늘    3200000   21       1000000   2100000  2100000
처리 건수 : 4 건
"""


def inputfunc():
    datas = [
        [1, "강나루", 1500000, 2010],
        [2, "이바다", 2200000, 2018],
        [3, "박하늘", 3200000, 2005],
    ]
    return datas
    
def get_bonus(workyear):
    if workyear <= 3:
        return 150000
    elif workyear >= 9:
        return 1000000
    else:
        return 450000

def get_tax_rate(real_pay):
    if real_pay >= 3000000:
        return 0.5
    elif real_pay < 2000000:
        return 0.15
    else:
        return 0.3


def processfunc(datas):
    print('출력 결과 :')
    print('사번  이름    기본급    근무년수  근속수당  공제액    수령액')
    print('------'*10)


    for number, name, pay, hireyear in datas:

        workyear = 2026 - hireyear

        bonus = get_bonus(workyear)

        real_pay = pay + bonus

        tax_rate = get_tax_rate(real_pay)

        reduce_pay = (real_pay)*tax_rate
        your_pay = pay + bonus - reduce_pay

            
        print(
            f'{number:<5}{name:<6}{pay:<12}{workyear:<8}'
            f'{bonus:<10}{reduce_pay:<10}{your_pay:<7}'
            )


datas = inputfunc()
processfunc(datas)



print()
print()
# 연습문제2) 리스트를 통해 상품 자료를 입력받아 가공 후 출력하기

"""
연습문제2) 리스트를 통해 상품 자료를 입력받아 가공 후 출력하기

처리 조건 :  
  1) 한 개의 상품명과 가격은 문자열로 입력됨. 문자열 나누기 필요.
  2) 취급 상품 예는 아래와 같다.
 * 취급상품표
  상품명   단가
  새우깡    450
  감자깡    300
  양파깡,   350

# 입력 함수
def inputfunc():
    datas = [
        "새우깡,15",
        "감자깡,20",
        "양파깡,10",
        "새우깡,30",
        "감자깡,25",
        "양파깡,40",
        "새우깡,40",
        "감자깡,10",
        "양파깡,35",
        "새우깡,50",
        "감자깡,60",
        "양파깡,20",
    ]
    return datas

출력 형태:
상품명   수량   단가   금액
-----------------------------------
새우깡    15    450   6750
감자깡    20    300   6000
양파깡    10    350   3500
새우깡    30    450   13500
감자깡    25    300   7500
양파깡    40    350   14000
새우깡    40    450   18000
감자깡    10    300   3000
양파깡    35    350   12250
새우깡    50    450   22500
감자깡    60    300   18000
양파깡    20    350   7000

소계
새우깡 : 135건   소계액 : 60750원
감자깡 : 115건   소계액 : 34500원
양파깡 : 105건   소계액 : 36750원
총계
총 건수 : 355
총 액  : 132000원
"""


def inputfunc():
    datas = [
        "새우깡,15",
        "감자깡,20",
        "양파깡,10",
        "새우깡,30",
        "감자깡,25",
        "양파깡,40",
        "새우깡,40",
        "감자깡,10",
        "양파깡,35",
        "새우깡,50",
        "감자깡,60",
        "양파깡,20",
    ]
    return datas

def get_price(name):
    if name == "새우깡":
        return 450
    elif name == "감자깡":
        return 300
    elif name == "양파깡":
        return 450
    

def processfunc(datas):

    shrimp_sum = 0
    shrimp_count = 0
    potato_sum = 0
    potato_count = 0
    onion_sum = 0
    onion_count = 0

    total_sum = 0
    total_count = 0


    print('출력 형태:')
    print('상품명   수량   단가   금액')
    print('---'*10)

    for data in datas:
        name, count = data.split(',')
        count = int(count)

        unit_price = get_price(name)

        price = count * unit_price

        print(
            f'{name:<7}{count:<6}{unit_price:<7}{price}'
            )
        

        if name == "새우깡":
            shrimp_count += count
            shrimp_sum += price
        elif name == "감자깡":
            potato_count += count
            potato_sum += price
        elif name == "양파깡":
            onion_count += count
            onion_sum += price

        total_count += count
        total_sum += price

    print()
    print('소계')
    print(f'새우깡 : {shrimp_count}건    소계액 : {shrimp_sum}원')
    print(f'감자깡 : {potato_count}건    소계액 : {potato_sum}원')
    print(f'양파깡 : {onion_count}건    소계액 : {onion_sum}원')

    print()
    print('총계')
    print(f'총 건수 : {total_count}')
    print(f'총 액 : {total_sum}원' )

datas = inputfunc()
processfunc(datas)

