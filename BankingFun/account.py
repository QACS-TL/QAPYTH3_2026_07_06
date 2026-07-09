class Account:
    def __init__(self,  account_id = "00000000", name="Anon", balance=0):
        self.account_id = account_id
        self.name = name
        self._balance = balance

    @property
    def balance(self)->int:
        return self._balance

    @balance.setter
    def balance(self, value:int)->None:
        if value < 0:
            value = 0
        self._balance = value

    def deposit(self,  value):
        if value < 0:
            value = 0
        self._balance += value

    def withdraw(self, *,  value):
        if value < 0:
            #value = 0
            raise ValueError("value cannot be negative")
        if value > self._balance:
            raise ValueError("Withdraw value too high")
        self._balance -= value



    def __str__(self):
        return f"ID: {self.account_id}, Name: {self.name}, Balance: £{self.balance}"

