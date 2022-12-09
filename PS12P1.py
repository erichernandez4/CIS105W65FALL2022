#defying the object
class employee:
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last  + "@company.com"
    #self.rate =0.00

    def bonus(self,rate):
        b = float(rate) * float(self.pay)
        return b 

    




emp_1 = employee("Eric","Hernandez", 65000)


print(emp_1.email)
print( emp_1.first)
print(emp_1.last)
print(emp_1.pay)
print(emp_1.bonus(0.10))
print(emp_1.bonus(0.20))