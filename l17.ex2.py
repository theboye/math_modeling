class Cell:
    def __init__(self, amount: int = 1):
        self.amount = amount

    def cel(self,amount):
        return self.amount

    def __add__(self, other):
        amount_1 = self.amount.copy()
        amount_1 += other.cel()
        return Cell(amount_1,self.name)

    def __sub__(self, other):
        amount_1 = self.amount.copy()
        amount_1 -= other.cel()
        return Cell(amount_1, self.name)

    def __mul__(self, other):
        amount_1 = self.amount.copy()
        amount_1 *= other.cel()
        return Cell(amount_1, self.name)
