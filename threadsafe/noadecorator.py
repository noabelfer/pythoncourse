import threading


class BankAccount:

    def __init__(self,_holder_name:str, _account_num:int):
        self._holder_name = _holder_name
        self._account_num = _account_num
        self._balance = 0
        self._transactions = []
        self.lock = threading.Lock()


    def __str__(self):
        lent = len(self._transactions)
        return (f'name: {self._holder_name}, account_num: {self._account_num}, balance: {self._balance},transactions: {lent}')

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
        def wrapper(self,*args, **kwargs):
            sum = args[0]
            b = None
            self.lock.acquire()
            while(sum > self._balance):
                self.lock.release()
                self.lock.acquire()
                
            try: 
                b = func(self,*args, **kwargs)
            finally:
                self.lock.release()
                return b
        return wrapper
        
    @lock_deposit_decorator
    def deposit(self, amnt):
        self._balance += amnt
        self._transactions.append("deposit")
    
    @lock_withdraw_decorator
    def withdraw(self, amnt)->bool:
        self._balance -= amnt
        self._transactions.append("withdraw")
         
    def get_balance(self):
        return self._balance
    


if __name__ == '__main__':
   my_account = BankAccount(123456, "Israel Israeli")
   # my_account.deposit(100)
   # my_account.withdraw(15)
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

   assert my_account._balance == 0, \
       f"Expected balance: 0, received: {my_account._balance}"
   assert len(my_account._transactions) == 799960, \
       f"Expected transactions: 799960, received: len(my_account._transactions)"

print(my_account)
