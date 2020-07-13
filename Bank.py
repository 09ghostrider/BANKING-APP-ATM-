from time import sleep
import random

P = int
B = int
AccountNumber = int
Username = ['NIKSH', 'NANYA', 'NIHA', 'SHIVANAND']
Account_Number = int
balance = int
pin = int
bal = 0
Account_Number = [1043, 1037, 4528, 8302]
Pin = [1234, 2345, 3456, 4567]
balance = [1000, 500, 100, 2000]
Start = ['Yes', 'yes', 'YES']
amo = int
While = False

start = input("DO YOU WANT TO USE THE ATM: ")
if start in Start:
  print("WELCOME TO ATM")
  sleep(1)
  While = True

  while While == True:
    print("\nLOGIN")
    print("SIGNUP")
    print("EXIT")
    log = str(input("OPTION: "))
    
    if log == 'LOGIN':
      acc = int(input("\nENTER YOUR ACCOUNT NUMBER: "))
      if acc in Account_Number:
        Position = Account_Number.index(acc)
        AccountNumber = Account_Number[Position]

        if acc == AccountNumber:
          pin = int(input("\nENTER YOUR PIN:"))
          PIN = Pin[Position]
          username = Username[Position]

          if pin == PIN:
            print("\nWELCOME TO YOUR ACCOUNT", username)
            B = balance[Position]
              
            while True:
              print("\n1 : BALANCE\t\t2 : WITHDRAWAL\t\t3 : ADD MONEY\t\t4 : TRANSFER MONEY\t\t5 : EXIT")
              option = input("CHOOSE AN OPTION:")

              if option == '1':
                print("\nYOUR BALANCE IS:", B)
                continue

              elif option == '2':
                amount = int(input("\nENTER THE AMOUNT YOU WANT:"))

                if B >= amount:
                  B = B - amount
                  print("\nYOUR BALANCE IS RUPPES ",B)
                  continue

                else:
                  print("\nYOUR BALANCE IS LESS THAN AMOUNT")
                  continue

              elif option == '3':
                add = int(input("\nPLEASE ENTER THE AMOUNT YOU WANT TO ADD: "))
                B = B + add
                print("\nYOUR BALANCE IS:", B)
                continue

              elif option == '4':
                tran = int(input("ENTER THE ACCOUNT NUMBER YOU WANT TO TRANSFER TO: "))

                if tran in Account_Number:
                  TransB = Account_Number.index(tran)
                  BalB = balance[TransB]
                  print("\nYOUR BALANCE IS:", B)
                  amo = int(input("ENTER THE AMOUNT YOU WANT TO TRANSFER: "))

                  if B >= amo:
                    B = B - amo
                    BalB = BalB + amo
                    print("\nYOUR BALANCE IS RUPPES ",B)
                    print("")
                    continue
                  
                  else:
                    print("YOUR BALANCE IS LESS THE THE TRANSFER AMOUNT")
                    continue

                else:
                  print("INVALID ACCOUNT")
                  continue

              elif option == '5':
                print("\nTHANK YOU FOR USING OUR BANK")
                print("VISIT AGAIN")
                break

              else:
                print("INVALID OPTION")
                continue

          else:
            print("INVALID PIN")
            continue

        else:
          print("ACCOUNT DOES NOT EXIST")
          continue
    
    elif log == 'SIGNUP':
      Yes = input("\nDO YOU WANT TO ADD YOUR ACCOUNT: ")
      
      while Yes in Start:
        A = random.randint(1000, 9999)

        if A not in Account_Number:
          if A not in Account_Number:
            Account_Number.append(A)
            C = input("\nENTER YOUR USER NAME: ")

            if C not in Username:
              Username.append(C)
              balance.append(bal)
              D = random.randint(1000, 9999)
          
              if D not in Pin:
                Pin.append(D)
                print("\nACCOUNT NUMBER:", A)
                print("PIN:", D)
                print("USER NAME:", C)
                print("\nYOUR ACOUNT HAS BEEN ADDED")
                break
              
              else:
                print("\nPIN IS TAKEN")
                continue

            else:
              print("\nUSERNAME IS IN UES")
              continue

          else:
            print("\nINVALID ACCOUNT NUMBER")
            continue

        else:
          print("\nACCOUNT NUMBER HAS BEEN USED")
          continue

      else:
        print("\nTRANSACTION DECLINED")
        continue

    elif log == 'EXIT':
        print("\nTHANK YOU")
        print("VISIT AGAIN")
        While = False
    
    else:
      print("INVALID OPTION")
      continue

else:
  print("\nTRANSACTION DECLINED")