class bank_account():
    def __init__(self, owner, number, balance):
        self.owner = owner
        self.number = number
        self.balance = balance
    def show_balance(self):
      print("Номер счета -", self.number, "Владелец -", self.owner, "Баланс -", self.balance)

show_balance = bank_account(
    owner = "Пухов;",
    number = "Неизвестен;",
    balance = "Слишком большой")

show_balance.show_balance()