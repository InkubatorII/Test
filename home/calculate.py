class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        amount = float(input("Введите сумму, которую нужно добавить: "))
        self._balance += amount

    def _kill(self):
        self._balance = 0

    def __jackpot(self):
        self._balance *= 10

    def _merge_balance(self, other):
        self._balance += other._balance

