class Machine:
    def __init__(self, name):
        self.name = name
        self.amount = 0

    def addAmount(self, amount):
        if amount > 0:
            self.amount += amount
            print(f"{amount}원이 추가되었습니다. 현재 잔액: {self.amount}원")
        else:
            print("유효한 입력이 아닙니다.")

    def getAmount(self):
        return self.amount