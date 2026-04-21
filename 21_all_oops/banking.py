# All OOP Principals 

# Inheritance
# Encapsulation
# Abstraction
# Polymorphism

class BankAccount:
    def __init__(self,account_no,holder_name,balance):
        self.account_no = account_no    # non sensitive
        self.holder_name = holder_name  # non sensitive
        self.__balance = balance          # sensitive -> Encapsulate / Hide

    def get_balance(self):
        return self.__balance
    
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            

# Implementation -> Abstraction 
from abc import ABC, abstractmethod

class Account(ABC):
    
    @abstractmethod
    def deposit(self,amount):
        pass 

    @abstractmethod
    def withdraw(self,amount):
        pass 
    
# Implementation -> Inheritance & Polymorphism 
class SavingsAccount(Account):
    
    def __init__(self,balance):
        self.__balance = balance 
        
    def deposit (self,amount):
        self.__balance += amount 
        
    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount 

class CurrentAccount(Account):
    
    def __init__(self,balance):
        self.__balance = balance 
        
    def deposit (self,amount):
        self.__balance += amount 
        
    def withdraw(self,amount): # different functionality 
        # i.e minimum amount should be 10000 after doing a withdraw
        if amount <= self.__balance:
            self.__balance -= amount 
        