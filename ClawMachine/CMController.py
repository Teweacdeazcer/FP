
from ClaswMachine import ClawMachine
from CMView import CMView

class CMController:
    def __init__(self):
        self.machine = ClawMachine("인형뽑기 기계")  # ClawMachine 객체 생성
        self.view = CMView()

    def start_game(self):
        while True:
            self.view.displayDolls(self.machine.dolls)
            self.view.displayMessage(f"현재 잔액: {self.machine.getAmount()}원")

            choice = self.view.getUserinput("1: 금액 추가   2: 인형 선택 & 뽑기   3: 종료\n입력 >> ")
            if choice == "1":
                amount = int(self.view.getUserinput("추가할 금액을 입력하세요: "))
                self.machine.addAmount(amount)
            elif choice == "2":
                doll_index = int(self.view.getUserinput("인형의 번호를 선택하세요(기회 1번에 2500원): ")) - 1
                if 0 <= doll_index < len(self.machine.dolls):
                    selected_doll = self.machine.dolls[doll_index]
                    self.machine.attemptGrab(selected_doll)
                else:
                    self.view.displayMessage("올바른 선택이 아닙니다.")
            elif choice == "3":
                self.view.displayMessage("게임을 종료합니다!")
                break
            else:
                self.view.displayMessage("올바른 선택이 아닙니다.")