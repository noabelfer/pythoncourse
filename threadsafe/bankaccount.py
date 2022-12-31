import threading

class BankAccount:
    
    def __init__(self,acount_id:int, name:str):
        self.balance = 0
        self.transactions = []
        self.__id = acount_id
        self.__name = name
        self.lock = threading.Lock()
        
    def deposit(self,sum:int):
        self.lock.acquire()
        try:
            self.balance += sum
            self.transactions.append(sum)
        finally:
            self.lock.release()
            
    def withdraw(self,sum:int)->bool:
        self.lock.acquire()
        try:
            if(sum > self.balance):
                self.lock.release()
                return False
            self.balance -= sum
            self.transactions.append(-sum)
        finally:
            self.lock.release()
            return True
        
    def get_balance(self)->int:
        return self.__balance
        
if __name__ == '__main__':
   my_account = BankAccount(123456, "Israel Israeli")
 
   def multiple_transactions_deposit(account):
       for i in range(100, 2000000, 10):
           account.deposit(i)

   def multiple_transactions_withdraw(account):
       for i in range(100, 2000000, 10):
           account.withdraw(i)

   t1 = threading.Thread(target=multiple_transactions_deposit, args=(my_account,))
   t2 = threading.Thread(target=multiple_transactions_deposit, args=(my_account,))
   t3 = threading.Thread(target=multiple_transactions_withdraw, args=(my_account,))
   t4 = threading.Thread(target=multiple_transactions_withdraw, args=(my_account,))

   t1.start()
   t2.start()
   t3.start()
   t4.start()

   t1.join()
   t2.join()
   t3.join()
   t4.join()
   
   print('my_account.balance '+str(my_account.balance))
   print('len(my_account.transactions)) '+str(len(my_account.transactions)))
   assert my_account.balance == 0, \
       f"Expected balance: 0, received: {my_account.balance}"
   assert len(my_account.transactions) == 799960, \
       f"Expected transactions: 799960, received: len(my_account.transactions)"



    