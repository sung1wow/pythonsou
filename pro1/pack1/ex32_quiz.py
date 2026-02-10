from abc import*

class Employee(metaclass=ABCMeta):    # 추상 클래스
    def __init__(self, irum, nai):
        self.irum = irum
        self.nai = nai

    @abstractmethod    
    def pay(self):    # 추상 클래스
        pass

    @abstractmethod
    def data_print(self):    # 추상 클래스
        pass

    def irumnai_print(self):    # 이름, 나이 출력용
        print('이름:'+ self.irum + ', 나이:' + str(self.nai), end='')


class Temporary(Employee):
    def __init__(self, irum, nai, ilsu, ildang):
        # Employee.__init__(self, irum, nai) 이걸로 아래 2줄 대체 가능
        self.irum = irum
        self.nai = nai
        self.ilsu = ilsu
        self.ildang = ildang

    def pay(self):
        return  self.ilsu * self.ildang

    def data_print(self):
        super().irumnai_print()
        print(', 월급:' + str(self.pay()))
        

class Regular(Employee):
    def __init__(self, irum, nai, salary):
        self.irum = irum
        self.nai = nai
        self.salary = salary

    def pay(self):
        return self.salary

    def data_print(self):
            super().irumnai_print()
            print(', 급여:' + str(self.pay()))
    

class Salesman(Employee):
    def __init__(self, irum, nai, salary, sales, commission):
        Employee.__init__(self, irum, nai)
        self.salary = salary
        self.sales = sales
        self.commission = commission

    def pay(self):
        return self.salary + self.sales * self.commission

    def data_print(self):
        super().irumnai_print()
        print(f', 수령액:{int(self.pay())}')


t = Temporary('홍길동', 25, 20, 15000)
r = Regular('한국인', 27, 3500000)
s = Salesman('손오공', 29, 1200000, 5000000, 0.25)

t.data_print()
r.data_print()
s.data_print()

