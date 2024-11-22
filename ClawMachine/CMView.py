
class CMView:

    def displayDolls(self, dolls):
        print("뽑기 가능한 인형 목록:")
        for idx, doll in enumerate(dolls, start=1):
            print(f"{idx}. {doll.name}")

    def displayMessage(self, message):
        print(message)

    def getUserinput(self, prompt):
        return input(prompt)