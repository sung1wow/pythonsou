print('------'*15)

# 문1) 1 ~ 100 사이의 정수 중 3의 배수이나 2의 배수가 아닌 수를 출력하고, 합을 출력
hap = 0
for i in range(1,101):
    if i%3 == 0:
        if i%2 == 0:
            continue
        print(i)
        hap += i
print(f'문1의 답 : {hap}입니다')

print()
# 문2) 2 ~ 5 까지의 구구단 출력
for a in range(1,6):
    for b in range(1,6):
        print(f'{a} * {b} = {a*b}')

print()
# 문3) 1 ~ 100 사이의 정수 중 “짝수는 더하고, 홀수는 빼서” 최종 결과 출력
final = 0
for e in range(1, 101):
    if e%2 == 0:
        final += e
    else:
        final -= e
print(f"문3의 답 : {final}")

print()
# 문4) -1, 3, -5, 7, -9, 11 ~ 99 까지의 모두에 대한 합을 출력
hap = 0
for a in range(-1, -99, -4):
    hap += a
for b in range(3, 99, 4):
    hap += b
print(f"문4의 답 : {hap}")

print()
# 문5) 1 ~ 100 사이의 숫자 중 각 자리 수의 합이 10 이상인 수만 출력
# 예) 29 → 2 + 9 = 11 (출력)
print('문5의 답')
for i in range(1, 101):
    tens = i//10
    ones = i%10
    if tens + ones >= 10:
        print(i)

print()
# 문6) 1부터 시작해서 누적합이 처음으로 1000을 넘는 순간의 숫자와 그때의 합을 출력
# 힌트: 언제 멈출지 미리 모름 → while 적합
print('문6의 답')
hap = 0
i = 1
while hap<=1000:
    hap += i
    if hap > 1000:
        break
    i += 1
print(i, hap)

print()
# 문7) 구구단을 출력하되 결과가 30을 넘으면 해당 단 중단하고 다음 단으로 이동
print('문7의 답')
for a in range(1,10):
    for b in range(1,10):
        if a*b < 30:
            print(f'{a} * {b} = {a*b}')



# 문8) 1 ~ 1000 사이의 소수(1보다 크며 1과 자신의 수 이외에는 나눌 수 없는 수)와 그 갯수를 출력
# 힌트: 이 문제는 반복이 두 단계다. 2부터 1000까지 하나씩 검사한다. 각 숫자마다 소수인지 확인한다.
# 그래서 while 안에 while 구조가 필요하다.
i = 2
count = 0
while i <= 1000:
    j = 2
    is_prime = True

    while j<i:
        if i%j == 0:
            is_prime = False
            break
        j += 1
    if is_prime:
        count += 1
    i += 1
print('\n 개수 : ', count)


# continue 연습 문제
# 문제1) 1부터 50까지의 숫자 중 3의 배수는 건너뛰고 나머지 수만 출력하라
# 문제2) 1부터 100까지 출력하되 4의 배수, 6의 배수는 건너뛴다. 그 외의 수 중 5의 배수만 출력하고 그들의 합도 출력하라


