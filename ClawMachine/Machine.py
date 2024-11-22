class Machine:
    def __init__(self, name):
        self.name = name
        self.amount = 0

    def addAmount(self, amount):
        self.amount += amount
        print(f"{amount}원이 추가되었습니다. 현재 잔액: {self.amount}원")

    def getAmount(self):
        return self.amount