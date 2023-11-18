class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate(self, quantity):
        total_price = self.price * quantity
        return total_price

coffee = Beverage("커피", 3000)
green_tea = Beverage("녹차", 2500)
ice_tea = Beverage("아이스티", 3000)

order = input("주문하실 음료를 선택해주세요. (커피, 녹차, 아이스티): ")


if order == "커피":
    selected_Beverage = coffee
elif order == "녹차":
    selected_Beverage = green_tea
elif order == "아이스티":
    selected_Beverage = ice_tea
else:
    print("팔고 있지 않는 음료입니다.")
    exit()

quantity = int(input("수량을 입력하세요: "))

total_price = selected_Beverage.calculate(quantity)
print(order + " " + str(quantity) + "잔의 총 가격은 " + str(total_price) + "원입니다.")
