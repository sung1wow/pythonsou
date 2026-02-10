class ElecProduct:
    volume = 0

    def volumeControl(self,volume):
        # print('볼륨을 조절한다')
        pass

    def tv1(self):
        print('ElecTv 고유 메소드')


class ElecTv(ElecProduct):
    def tv1(self):
        print('ElecTv 고유 메소드')
    def volumeControl(self, volume):
        print('ElecTv 볼륨을 조절한다 : {volume}')

class ElecRadio(ElecProduct):
    def radio1(self,volume):
        print('ElecRadio 고유 메소드')
    def radio1(self,volume):
        sori = volume
        print(f'ElecRadio 소리를 조절 : {sori}')


product = ElecProduct()     # 다형성!!! 이거 중요함!!!!
tv = ElecTv()
product = tv
product.volumeControl(5)
print()
radio = ElecRadio()
product = radio
product.volumeControl(3)

print('--------')
q1 = [ElecTv() ,ElecRadio()]
for a in q1:
    a.volumeControl(2)
    print()
