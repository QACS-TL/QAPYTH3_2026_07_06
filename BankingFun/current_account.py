from account import Account

class CurrentAccount(Account):
    _overdraft_limit = 500

    def __init__(self, account_id, name, balance, overdraft_limit):
        super().__init__(account_id, name, balance)
        self._overdraft_limit = overdraft_limit

    @property
    def overdraft_limit(self):
        return self._overdraft_limit

    @overdraft_limit.setter
    def overdraft_limit(self, overdraft_limit):
        if overdraft_limit < 0:
            raise ValueError("Overdraft limit cannot be negative")
        self._overdraft_limit = overdraft_limit

    def withdraw(self, value):
        if value < 0:
            #value = 0
            raise ValueError("value cannot be negative")
        if value > self._balance + self._overdraft_limit:
            raise ValueError("Withdraw value too high")
        self._balance -= value

    def __str__(self):
        return f"{super().__str__()} Overdraft limit: £{self.overdraft_limit}"