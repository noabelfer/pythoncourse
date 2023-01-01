import threading


class BankAccount:

    def __init__(self,_holder_name:str, _account_num:int):
        self._holder_name = _holder_name
        self._account_num = _account_num
        self._balance = 0
        self._transactions = []
        self.lock = threading.Lock()


    def __str__(self):
        return (f'name: {self._holder_name}, account_num: {self._account_num}, balance: {self._balance}')

    def lock_deposit_decorator(func):
        def wrapper(self,*args, **kwargs):
            b = None
            self.lock.acquire()
            try: 
                b = func(self,*args, **kwargs)
            finally:
                self.lock.release()
                return b
        return wrapper
        
    def lock_withdraw_decorator(func):
        def wrapper(self,sum):
            b = None
            self.lock.acquire()
            while(sum > self._balance):
                self.lock.release()
                self.lock.acquire()
                
            try: 
                b = func(self,sum)
            finally:
                self.lock.release()
                return b
        return wrapper
        
    @lock_deposit_decorator
    def deposit(self, amnt):
      #  with self.lock:
        self._balance += amnt
        self._transactions.append("deposit")
    
    @lock_withdraw_decorator
    def withdraw(self, amnt)->bool:
        try:
            result = True
            # while self._balance < amnt:
                # self._cv.wait()

            self._balance -= amnt
            self._transactions.append("withdraw")
        finally:
            return result
            
    def __blocked(self,amount)->bool:
        return amount > self._balance
        
    def get_balance(self):
        return self._balance
    


if __name__ == '__main__':
   my_account = BankAccount(123456, "Israel Israeli")
   # my_account.deposit(100)
   # my_account.withdraw(1500)
   # print(my_account._balance)
   # exit()
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

   print('my_account.balance '+str(my_account._balance))
   print('len(my_account.transactions)) '+str(len(my_account._transactions)))
   assert my_account._balance == 0, \
       f"Expected balance: 0, received: {my_account._balance}"
   assert len(my_account._transactions) == 799960, \
       f"Expected transactions: 799960, received: len(my_account._transactions)"

print(my_account)
