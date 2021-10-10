'''
b = 0
class calculator:
    def __init__(self):
        self.b = 0
    
    def add(self , a):
        self.b += a
        return self.b

    def sub(self , a):
        self.b -= a
        return self.b   

cal1 = calculator()
cal2 = calculator()


print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(1))
print(cal2.add(2))'''







class Car:
    car_num = 0
    name = []
    engine = []
    tire = []
    option = []
    option_name = []
    max_speed = []
    price = []



    def __init__(self):
        pass
    def Insert(self):
        self.name.append(input("이름 :"))
        self.engine.append(int(input("엔진 가격 :")))
        self.tire.append(int(input("타이어 가격 :")))
        option_whe = input("옵션(있음/없음) :")
        if option_whe == '있음':
            self.option.append(option_whe)
            self.option_name.append(input("옵션 이름 :"))
        elif option_whe == '없음':
            self.option.append(option_whe)
            self.option_name.append('x')
        self.max_speed.append(int(input("최고 속도 :")))

        self.car_num += 1 #차량 등록 수 카운트
    
    def Order(self):
        print()

    
    def Price(self):
        print
    
    
    def Option(self):
        print


    def Speed_gap(self):
        Gap =  max(self.max_speed) - min(self.max_speed)
        





msg = """========자동차 정보 프로그림========
1. 자동차 정보 입력\n2. 저장된 목록 보기\n3.각 자동차 구매 가격 조회
4. 옵션이 있는 자동차 조회\n5. 빠른 자동차와 느린 자동차의 속도 차이 조회\n6. 프로그램 이용 종료 
=======================================\n입력 : """
car = Car()
while(1):
    choice = int(input(msg))
    if choice == 1:
        print("자동차 정보 입력")
        car.Insert()
    elif choice == 2:
        car.Order()
    elif choice == 3:
        print("원하시는 가격을 입력해주세요")
        low = int(input("하한가 :"))
        high = int(input("상한가 :"))
        car.Price(low,high)
    elif choice == 4:
        car.Option()
    elif choice == 5:
        car.Speed_gap()
    else:
        break