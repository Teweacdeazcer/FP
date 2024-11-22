class DollDTO:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Doll(name={self.name})"