class Bank():
    def __init__(self,BankId,Name,Location):
        assert type(BankId)==int and type(Location)==str
        self.BankId = BankId
        self.Name = Name
        self.Location = Location
BankA=Bank(1,'Centenary','MAKERERE')
BankB=Bank(2,'Stanbic','MAKERERE')

class TellerA(Bank):
    def __init__(self,Tid,TName):
        assert type(Tid) == int
        self.Id = Tid
        self.Name = TName
        self.balance = 0


    def CollectMoney(self,amount):
        self.balance += amount
        return self.balance

    def OpenAccount(self):
        print("Welcome to Centenary Bank")
        print("Do u wish to open an account?")
        print("Your branch is %s" %BankA.Location)
        
    def CloseAccount(self):
        print("Would you like to close your account? ")
        print("You are legible to getting a loan")
        print("Your branch is %s" %BankA.Location)
        
    def LoanRequest(self):
        if self.balance>5000:
         print("You are legible to getting a loan")
        else:
            print("Request failed")
            
    def ProvideInfomation(self):
        print("Tid:%d,TName:%s,Address:%s,PhoneNo:%d,AccNo:%d   ")
        print("Your branch is %s" %BankA.Location)

    def IssueCard(self):
        print("%s, your ATM card is ready"%self.Name)
        print("your branch is %s" %BankA.Location)




class TellerB(Bank):
    def __init__(self,Tid,TName):
        assert type(Tid) == int
        self.Id = Tid
        self.Name = TName
        self.balance = 0

    def CollectMoney(self,amount):
        self.balance+=amount
        return self.balance

    def OpenAccount(self):
        print("Welcome to Stanbic Bank")
        print("Do you wish to open an account?")
        print("Your branch is %s" %BankB.Location)

    def CloseAccount(self):
        print("Would you like to close your account?")


    def LoanRequest(self):
        if self.balance>5000:
            print("You are legible to getting a loan")
            print("Your branch is %s" %BankB.Location)
        else:
            print("Request failed")
            

    def ProvideInformation(self):
        print("Tid:%d,TName:%s,Address:%s,PhoneNo:%d,AccNo:%d")
        print("Your branch is %s" %BankB.Location)

    def IssueCard(self):
        print("%s, your ATM card is ready" %self.Name)
        print("You were served by %s" %Diana_Esther.Name)






class Customer2(TellerB,Bank):
    def __init__(self,Cid,CName,Address,PhoneNo,AccNo,Balance):


       self.Id = Cid
       self.Name = CName
       self.Address = Address
       self.PhoneNo = PhoneNo
       self.AccNo = AccNo
       self.balance = Balance


    def GeneralInquiry(self):
        print("Cid:%d,CName:%s,Address:%s,PhoneNo:%d,AccNo:%d,Balance:%d"%(self.Id,self.Name,self.Address,self.PhoneNo,self.AccNo,self.balance))

    def DepositMoney(self,amount):
        assert type(amount) == int

        self.balance += amount
        print('%d is your balance'%(self.balance))


    def WithdrawMoney(self,amount):
        self.balance -= amount
        print("%d is your balance"%(self.balance))


    def OpenAccount(self):
        print("Yes, please!")


    def CloseAccount(self):
        print("No, please!")


    def ApplyLoan(self):
        print("CName:%d,AccNo:%d I would like to get a loan")

    def RequestCard(self):
        print("Is my card ready?")

class Customer1(TellerA,Bank):
    def __init__(self,Cid,CName,Address,PhoneNo,AccNo,Balance):


       self.Id = Cid
       self.Name = CName
       self.Address = Address
       self.PhoneNo = PhoneNo
       self.AccNo = AccNo
       self.balance = Balance


    def GeneralInquiry(self):
        print("Cid:%d,CName:%s,Address:%s,PhoneNo:%d,AccNo:%d,Balance:%d"%(self.Id,self.Name,self.Address,self.PhoneNo,self.AccNo,self.balance))

    def DepositMoney(self,amount):
        assert type(amount)==int

        self.balance += amount
        print('%d is your balance'%(self.balance))


    def WithdrawMoney(self,amount):
        self.balance -= amount
        print("%d is your balance"%(self.balance))


    def OpenAccount(self):
        print("Yes, please!")


    def CloseAccount(self):
        print("No, please!")


    def ApplyLoan(self):
        print("CName:%d,AccNo:%d I would like to get a loan")

    def RequestCard(self):
        print("Is my card ready?")
        print("You were served by %s" %Nalin_Brinah.Name)


Diana_Esther = TellerB(7,"Kyomuhendo")
aggy = Customer2(10,"Sarah","Kampala",+256724879321,2005004001,5000)
aggy.OpenAccount()
print(aggy.GeneralInquiry())
aggy.DepositMoney(5000)
aggy.LoanRequest()
aggy.IssueCard()

print('')

Nalin_Brinah = TellerA(3,"Nakalembe")
ked = Customer1(12,"Berna","Kampala",+256489422254,2009004300,20000)
ked.OpenAccount()
print(ked.GeneralInquiry())
ked.DepositMoney(20000)
ked.LoanRequest()
ked.IssueCard()


