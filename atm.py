class atm(object):
    def __init__(self,cn,pn):
        self.cardnumber:cn
        self.pinnumber:pn

    

    def Balance(self):
            print("your balance is 50000 ")

    def Withdrawl(self,removal):
        newamount = 50000 - removal
        print("You have withdrawn amount " + str(removal) + ". Your remaining balance is " + str(newamount))
              


def display():
    cn = input("insert your card number : ")
    pn = input("enter your pin number : ")
    atmd = atm(cn,pn)
    print("choose your activity ")
    print("1.Balance enquiry 2.withdrawl")
    activity = int(input("enter activity number"))
    if(activity == 1):
        atmd.Balance()
    elif(activity == 2):
        removal = int(input("enter your withdrawl amount "))
        atmd.Withdrawl(removal)
    else:
        print("enter an number between 1 and 2")
        
display()   