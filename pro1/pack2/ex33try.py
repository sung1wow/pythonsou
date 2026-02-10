# 예외처리 : 파일, 네트워크, DB작업, 실행에러 등의 에러 대처

def divide(a, b):
    return a / b

print('이런 저런 작업 진행...')
# c = divide(5, 2)
# c = divide(5, 0)
# print(c)

try:    ## 이건 왠만하면 쓰는 게 좋음, 에러에 대한 예외를 쓰는거라서 나쁠게 없음 
    # 실행문(예외 발생 가능 구문)
    c = divide(5, 2)
    # c = divide(5, 0)
    print(c)

    aa = [1, 2]
    print(aa[0])
    # print(aa[3])

    open("c:/work/abc.text")

except ZeroDivisionError:                 # 예외 종류 관련 클래스
    print('두번째 값은 0을 주면 안돼요')    # 예외 발생 처리 구문
except IndexError as err:          # err이라는 별명을 붙이면 
    print('참조 범위 오류 :', err)  # 시스템이 주는 오류메시지도 출력 가능
except Exception as e:               # Exception 이 가장 커서 얘를 먼저 적으면
    print('에러 : ', e)              # 다 묶여버림 + 다른 거 안 적으면 다 뭉뚱거려짐
finally:
    print('에러 유무에 상관없이 반드시 수행됨')  # 무조건 실행됨, 파일 닫기 같은 거

print('end')