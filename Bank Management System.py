while True:
 balance = 0
 a = int(input("1.Balance\n2.Deposit\n3.Withdraw\n4.Exit"))


 if(a == 1):
    print(f"Balance = {balance}")

 elif(a == 2):
     b = int(input("Enter the amount:"))
     balance = balance + b
     print(f"Now the Balance is :{balance} ")

 elif(a == 3):
     c = int(input("Enter the amount to withdraw :"))
     if (c <= balance):
        balance = balance - c
     else:
         print(f"You have no enough balance to withdraw {c}")
         exit()

     print(f"Remaining Balance:{balance}")

 elif(a == 4):
     print("Thank you for using the bank system")
     break
 


    