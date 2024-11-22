import random
from Machine import Machine
from DollDTO import DollDTO

class ClawMachine(Machine):
    def __init__(self, name, sucessRate=50):
        Machine.__init__(self, name)
        self.sucessRate = sucessRate  # 성공 확률 : 50%
        self.dolls = [
            DollDTO("곰인형"),
            DollDTO("벨루가인형"),
            DollDTO("팬더인형"),
            DollDTO("고라파덕인형"),
            DollDTO("티니핑인형"),
        ]

    def attemptGrab(self, doll_choice):
        if self.amount < 3000:
            print("잔액이 부족합니다. 금액을 추가해주세요.")
            return None

        self.amount -= 3000
        if random.randint(1, 100) <= self.sucessRate:
            print(f"축하합니다! {doll_choice.name}을(를) 뽑았습니다!!")
            return doll_choice
        else:
            print("꽝... 아쉽게도 실패하였습니다.")
            return None