class Bank:
    bankId = -1
    allBanks = []
    def __init__(self, fullName, bankAbbreviation):
        self.fullName = fullName
        self.bankAbbreviation = bankAbbreviation
        Bank.bankId += 1
        self.bankId = Bank.bankId


    @staticmethod
    def findBank(bankAbbreviation):
        # return (True, Bank.allBanks)
        for i in Bank.allBanks:
            if i.bankAbbreviation == bankAbbreviation:
                return True,i
        return False, None

    @staticmethod
    def createNewBank(fullName, bankAbbreviation):
        isBankExist, bankObject = Bank.findBank(bankAbbreviation)
        if not isBankExist:
            return False, "Bank bankAbbreviation already exist"
        if bankObject.fullName == fullName:
            return False, "Bank full name already exist"
            
        newBank = Bank(fullName, bankAbbreviation)
        Bank.allBanks.append(newBank)
        return True, "Bank Created!"