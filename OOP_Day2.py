'''
# Inheritance

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        print(" inside constructor - Brand name is :",self.brand)
        self.model_name = model
        print("inside constructor - Model name is :", self.model_name)

    def start_engine(self):
        print("Vehile starts...")

    def stop_engine(self):
        print("Vehile stops...")

class Car(Vehicle):
    def __init__(self,brand,model,fuel_type):
        super().__init__(brand,model)
        self.fuel_type = fuel_type

    def honk(self):
        print(f"{self.brand}{self.model_name} is honking: beep beep")


c = Car("Maruti suzuki","Breeza","Petrol")
print(c.fuel_type)
c.start_engine()
c.stop_engine()
c.honk()


v = Vehicle("Telsa","ModelS")



v1 = Vehicle("Toyoto","Camry")
print("Outside constrcutor: ",v1.brand)
print("Outside constrcutor: ",v1.model_name)

v2 = Vehicle("Honda","Honda civic")
print("Outside constrcutor: ",v2.brand)
print("Outside constrcutor: ",v2.model_name)

'''


# Encapsulation :
# public ( every one ), # protected(_) ( only child class can access ), private(__) ( only inside that class)
class BankAccount:
    def __init__(self,owner,balance,pin):
        self.owner = owner
        print("Inside constructor ", self.owner)
        self._balance = balance
        print("Inside constructor ", self._balance)
        self.__pin = pin
        print("Inside constructor ",self.__pin)

    def display(self):
        print("Inside class ", self.owner)

        print("Inside class ", self._balance)

        print("Inside class ", self.__pin)


class SavingsAccount(BankAccount):
    def __init__(self,owner,balance,pin,interest_rate):
        super().__init__(owner,balance,pin)
        self.interest_rate = interest_rate

    def access_parent_data(self):
        print("owner :",self.owner)
        print("balance :", self._balance)
        print("Pin :", self._BankAccount__pin)


sa = SavingsAccount("ETL QA Labs",10000,12345,7.8)
sa.access_parent_data()



bank = BankAccount("ETL QA Labs",10000,12345)
bank.display()
print(bank.owner)
print(bank._balance)  # Should not be allowed
# print(bank.__pin)
print(bank._BankAccount__pin)


