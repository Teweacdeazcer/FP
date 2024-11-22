class DollDTO:
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def __str__(self):
        return f"Doll(name={self.name}, count={self.count})"

    def decreaseCount(self):
        if self.count > 0:
            self.count -= 1
        else:
            print(f"{self.name}의 재고가 없습니다!")

    def getCount(self):
       return self.count