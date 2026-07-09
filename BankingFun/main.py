import account
from current_account import CurrentAccount

def main():
    acc1 = account.Account( "88888888", "J Jones")
    acc2 = account.Account("12345678","S Saleem", 100.00)

    acc2.deposit(12)
    print(acc2)

    acc1.deposit(200)
    acc2.withdraw(value=50)

    print(acc1)
    print(acc2)

    cacc = CurrentAccount("565656565", "Jones", 100, 750)
    cacc.withdraw(851)
    print(cacc)


    accounts = {}
    accounts[acc1.account_id] = acc1
    accounts[acc2.account_id] = acc2
    accounts[cacc.account_id] = cacc

    acc2.balance = -1

    for acc_id in accounts:
        accounts[acc_id].deposit(40)
        print(accounts[acc_id])



if __name__ == '__main__':
    main()