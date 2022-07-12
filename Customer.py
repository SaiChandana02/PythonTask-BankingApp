from accounts import Accounts

class Customer:
    customerID = -1
    allCustomer = []

    def __init__(self, fName, lName, userName):
        self.fName = fName
        self.lName = lName
        self.totalBalance = 0
        self.customerId = Customer.customerId
        self.userName = userName
        self.accounts = []

    def deposit(self, amount, bankAbbreviation):
        isAccountExist, account = self.findAccount(bankAbbreviation)
        if not isAccountExist:
            return False, "Account does not exist"
        account.balance += amount
        self.__updateTotalBalance()
        self.displayBalance()
        return True, "Amount Deposited."

    def withdraw(self, amount,bankAbbreviation):
        isAccountExist, account = self.findAccount(bankAbbreviation)
        if not isAccountExist:
            return False, "Account does not exist"
        if not account