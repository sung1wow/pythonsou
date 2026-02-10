# ElecrProduct의 sub class 두 개를 만들고 
# volumeControl()을 overriding하여 다형성을 구현하시오


class ElecProduct:
    volume = 0

    def volumeControl(self, volume):
        
        # print("공통 볼륨 조절 :", volume)
        pass


class ElecTv(ElecProduct):
    def volumeControl(self, volume):
        self.volume = volume
        print("TV 볼륨 조절 :", volume)


class ElecRadio(ElecProduct):
    def volumeControl(self, volume):
        print("라디오 볼륨 조절 :", volume)

products = [ElecTv(), ElecRadio()]

for p in products:
    p.volumeControl(10)


"""
class Animal:

    def move(self):
        pass


class Dog:

    name = "개"

    def move(self):
        pass


class Cat:
    name = "고양이"

    def move(self):
        pass


class Wolf:



class Fox:

    def move(self):
        pass
    def foxMethod(self):
        pass
"""

