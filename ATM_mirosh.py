class ATM():
  def __init__(self, money, accnumber,password):
    self.accnumber = accnumber
    self.password = password
    self.money = money

  #Банкомат должен иметь: номер карты, пароль. Функции: баланс, снять деньги, внести деньги, завершить обслуживание. Цикл не должен прерываться.
  # Добавить килл каунт 

  def login(self):
    try:
      num = int(input("Enter an account number: "))
      passw = int(input("Enter password: "))
      int(num) and int(passw)
    except ValueError:
      print("Please write numbers")
      ATM.login(account1)
    if num  != self.accnumber or  passw != self.password:
      print("Invalid account number or password, please try again.")
      ATM.login(account1)
    else:
      ATM.menu(account1)

  def menu(self):
    print("Hello worl... oh sorry! Please choose option number.")
    print("1. Check banc account.")
    print("2. Withdraw money.")
    print("3. Deposit money.") 
    print("4. Exit.")
    
    try:
      option = int(input(">"))
      int(option)
    except ValueError:
      print("Please write numbers")
      ATM.menu(account1)
    if option == 1:
      ATM.check(account1)
    elif option == 2:
      ATM.withdraw(account1)
    elif option == 3:
      ATM.deposit(account1)
    elif option == 4:
      ATM.out(account1)
    else:
      print("Wrong input, please select again.")
      ATM.menu(account1)
         

  def check(self):
    print(self.money)
    ATM.menu(account1)

  def withdraw(self):
    try:
      withdraw1 = int(input("Write withdraw amount >"))
      int(withdraw1)
    except ValueError:
      print("Please write numbers")
      ATM.withdraw(account1)
    if withdraw1 > int(self.money):
      self.money = int( self.money + withdraw1-withdraw1)
      print("Withdraw amount is too high. You are poor")
      print(self.money)
    else:
      self.money = int(self.money - withdraw1)
      print(self.money)
    ATM.menu(self)
        
    
  def deposit(self):
    try:
      deposit1 = int(input("Deposit amount> "))
      int(deposit1)
    except ValueError:
      print("Please write numbers")
      ATM.deposit(account1)
    if deposit1 < 0:
      print("You cant deposit negative sum")
      ATM.deposit(self)
    else:
      self.money = int(self.money + deposit1)
      print(self.money)
    ATM.menu(self)
  
  def out(self):
    ATM.login(self)
  

account1 = ATM(50000, 12, 34)
ATM.login(account1)
