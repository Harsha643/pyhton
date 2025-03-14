# # class Car():
# #     def __init__(self,car_num):
# #         self.car_num=car_num
# #     def __sub__(self,car2):
# #         return self.car_num - car2.car_num
    

# # car1=Car(3)
# # car2=Car(5)

# # print(car1-car2)



# class BankAccount:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder  # Public attribute
#         self._bank_name = "ABC Bank"  # Protected attribute
#         self.__balance = balance  # Private attribute

#     def deposit(self, amount):
#         self.__balance += amount
#         print(f"Deposited ${amount}. New Balance: ${self.__balance}")

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrawn ${amount}. New Balance: ${self.__balance}")
#         else:
#             print("Insufficient funds!")

#     def get_balance(self):
#         return self.__balance  # Accessing private attribute through a method

# # Creating an object of BankAccount
# account = BankAccount("John Doe", 1000)

# # Public attribute can be accessed directly
# print(account.account_holder)  # Output: John Doe

# # Protected attribute (Not recommended to access directly, but possible)
# print(account._bank_name)  # Output: ABC Bank

# # Private attribute (Direct access will cause an error)
# # print(account.__balance)  # ❌ AttributeError: 'BankAccount' object has no attribute '__balance'

# # Accessing private data using a method
# print(account.get_balance())  # Output: 1000

# # Modifying balance using deposit and withdraw methods
# account.deposit(500) 
# account.withdraw(200)  

# account.deposit(1000)







