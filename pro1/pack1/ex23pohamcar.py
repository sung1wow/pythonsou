# 여러 개의 부품 객체를 조립해 완성차 생성
# 클래스의 포함 관계 사용 (자원의 재활용이 목적임)
# 다른 클래스(객체)를 마치 자신의 멤버처럼 선언하고 사용
# import ex23pohamhandle
from ex23pohamhandle import PohamHandle

class PohamCar:
    turnShowMessage = "정지"

    def __init__(self, ownerName):
        # ownerName = ownerName    # 이 따구로 하지 말것
        self.ownerName = ownerName
        self.handle = PohamHandle()    # 클래스의 포함관계

    def turnHandle(self, q):
        if q > 0:
            self.turnShowMessage = self.handle.rightTurn(q)    # rightTurn은 핸들에 있음, .을 찍어서 계속 들어감
        elif q < 0:
            self.turnShowMessage = self.handle.leftTurn(q)
        elif q == 0:
            self.turnShowMessage = "직진"

if __name__ == '__main__':    # “야 나 여기 주인공(메인)이야? 그럼 실행한다. 아니야? 그럼 조용히 클래스만 제공하고 빠질게.”
    tom = PohamCar('미스터 톰')
    tom.turnHandle(10)
    print(tom.ownerName + '의 회전량은 ' + \
          tom.turnShowMessage + ' ' + str(tom.handle.quantity))
    
    john = PohamCar('미스터 존')
    john.turnHandle(-20)
    print(john.ownerName + '의 회전량은 ' + \
          john.turnShowMessage + ' ' + str(john.handle.quantity))
    
    john.turnHandle(0)
    print(john.ownerName + '의 회전량은 ' + \
          john.turnShowMessage + ' 0')