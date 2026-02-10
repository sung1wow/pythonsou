# 클래스의 다중 상속 - 부모가 복수

class Tiger:
    data = "호랑이 세계"

    def cry(self):
        print('호랑이 : 어흥')

    def eat(self):
        print('맹수는 고기를 좋아함')

class Lion:
    def cry(self):
        print('사자 : 으르렁')

    def hobby(self):
        print('백수의 왕은 낮잠이 취미')

class Liger1(Tiger, Lion):    # 다중 상속은 순서가 중요 (cry 두개인데 뭐 받을래?)
    pass

a1 = Liger1()
print(a1.data)
a1.eat()
a1.hobby()
a1.cry()

print('---'*10)
def hobby():
    print('모듈의 멤버 : 일반 함수')

class Liger2(Lion, Tiger):
    data = '라이거 만세'

    def play(self):
        print('라이거 고유 메소드')

    def hobby(self):    # 메소드 오버라이드
        print('라이거는 공원 걷기를 좋아함')

    def showData(self):
        self.hobby()       # 자식꺼
        super().hobby()    # 부모꺼
        hobby()            # 그냥 모듈에 만들어 놓은거 

        self.eat()         # 라이거부터 찾고 없으면 라이언, 타이거로 올라감
        super().eat()      # 처음부터 라이언, 타이거에서 찾음

        print(self.data + ' ' + super().data)

a2 = Liger2()
a2.cry()
