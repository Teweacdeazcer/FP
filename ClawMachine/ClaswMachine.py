
import random
from Machine import Machine
from DollDTO import DollDTO

class ClawMachine(Machine):
    def __init__(self, name, sucessRate=50):
        Machine.__init__(self, name)
        self.sucessRate = sucessRate  # 성공 확률 : 50%
        self.dolls = [
            DollDTO("곰돌이"),
            DollDTO("토끼"),
            DollDTO("강아지"),
        ]

    def attemptGrab(self, doll_choice):
        if self.amount < 1:
            print("잔액이 부족합니다. 금액을 추가해주세요.")
            return None

        self.amount -= 2500
        if random.randint(1, 100) <= self.successRate:
            print(f"축하합니다! {doll_choice.name}을(를) 뽑았습니다!!")
            return doll_choice
        else:
            print("꽝... 아쉽게도 실패하였습니다.")
            return None