from bank import Bank

class Accounts:
    accountId = -1
    def __init__(self, bank, balance):
        self.bank = bank
        self.balance = balance
        self.accountId = Accounts.accountId

    def isAccountExist(self, bankAbbreviation):
        return self.bank.bankAbbreviation == bankAbbreviation

    def displayBalance(self):
        print(self.bank.bankAbbreviation, "Balance is: ", self.balance)

    def isSufficientBalance(self, amount):
        return self.balance >= amount

    @staticmethod
    def createNewAccount(bankAbbreviation, ):
        isBankExist, bankObject = Bank.findBank(bankAbbreviation)
        if not isBankExist:
            return False, "Bank does not exist"
        Accounts.accountId+=1
        newAccount = Accounts(bankObject, 100)
        return True, "Account Created"