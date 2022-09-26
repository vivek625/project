from genericpath import exists
from getpass import getpass
import pickle
import os
import pathlib
class Bank:
    accName = ''
    account_number = 0
    deposit = 0
    type = ''

    # create account 

    def createAccount(self):
        self.account_number = int(input("Enter account number: "))
        self.accName = input("Enter customer name : ")
        self.type = input("Enter your account type : ")
        self.deposit = int(input("minimum balance of account (500>= saving and 1000 >= current account "))
        print("\n\n Created  account ")
        
    # show account details 

    def showAccount(self):
        print("Account number : " , self.account_number)
        print("Account holder name : ", self.accName)
        print("Type of account[c/s] : ",self.type)
        print("Balance : ",self.deposit)

    # modify your account details

    def modifyAccount(self):
        print("Account number : ",self.account_number)
        self.accName = input("modify your account holder name : ")
        self.type = input("modify account type name :")
        self.deposit = int(input("balance : "))


    def depositAmount(self,Amount):
        self.deposit += Amount

    def withdrawAmount(self , Amount):
        self.deposit -= Amount

    def report (self):
        print(self.account_number , " " , self.accName , " " , self.type , " ", self.deposit)
    def getAccountNo(self):
        return self.account_number
    def getAcccountHolderName(self):
        return self.accName
    def getAccountType(self):
        return self.type
    def getDeposit(self):
        return self.deposit
    


def information():
    print("          **************************             ")
    print("vivek raj singh bank management system ".center(50))
    print("***************************".center(50))

def writeAccount():
    bank = Bank()
    bank.createAcc()
    writeAccountsFile(Bank)

def displayAll():
    file = pathlib.path("accounts.data")     # accounts.data buildin module
    if file/exists():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        for item in mylist:
            print(item.account_number," ",item.accName , " ", item.type , " ",item.deposit)
        infile.close()
    else:
        print("no records in database ")

def displaySp(num):
    file = pathlib.path('accounts.data')
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist:
            if item.account_number == num:
                print("your account balance is = ", item.deposit)
                found = True 
            else:
                print("No records to search")
            if not found:
                print("No records with this number")


def despositAndWithdraw(num1, num2):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist:
            if item.account_number == num1:
                if num2 == 1:
                    amount = int(input("Enter the amount to deposit : "))
                    item.deposit += amount
                    print("your account is updated")
                elif num2 == 2:
                    amount = int(input("Enter the amount to withdraw : "))
                    if amount <= item.deposit:
                        item.deposit -= amount
                    else:
                        print("You cannot withdraw larger amount")

    else:
        print("No record to search ")
    outfile = open('newaccounts.data','wb')
    pickle.dump(mylist,outfile)
    outfile.close()
    os.rename('newaccounts.data','accounts.data')


# --- delete function --------

def deleteAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist:
            if item.account_number != num:
                newlist.append(item)
            os.remove('accounts.data')
            outfile = open('newaccounts.data','wb')
            pickle.dump(newlist,outfile)
            outfile.close()
            os.rename('newaccounts.data','accounts.data')
def modifyAccount(num):
    file = pathlib.Path('accounts.data')
    if file.exists():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in oldlist:
            if item.account_number == num:
                item.accName = input("Enter the account holder name : ")
                item.type = input("Enter the account type : ")
                item.deposit = int(input("Enter the Amount : "))

        outfile = open('newaccounts.data','wb')
        pickle.dump(oldlist,outfile)
        outfile.close()
        os.rename('newaccounts.data','accounts.data')

def writeAccountsFile(account) : 
    
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')
    else :
        oldlist = [account]
    outfile = open('newaccounts.data','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')

# --------- start of program 
ch = ''
num = 0
while ch != 8:
    print("\tMain menu")
    print("\t1. new account")
    print("\t2. deposit amount")
    print("\t3. withdraw amount")
    print("\t4. Balance enquiry")
    print("\t5. all account holder list")
    print("\t6. close an account")
    print("\t7. modify an acount")
    print("\t8. exit")
    print("\tselect your opention (1-8) ")
    ch = input()

    if ch == '1':
        writeAccount()
    elif ch == '2':
        num = int(input("\tEnter the account no. : "))
        despositAndWithdraw(num,1)
    elif ch == '3':
        num = int(input("\tEnter the account no. :"))
        despositAndWithdraw(num,2)
    elif ch == '4':
        num = int(input("\tEnter the account no. : "))
        displaySp(num)
    elif ch == '5':
        displayAll()
    elif ch == '6':
        num = int(input("\tEnter the account no. :"))
        deleteAccount(num)
    elif ch == '7':
        num = int(input("\tEnter the account no. : "))
        modifyAccount(num)
    elif ch == '8':
        print("\tThanks for using bank management system")
        break
    else:
        print("Invalid choice")

    ch = input("Enter your choice : ")
