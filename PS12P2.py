class student:
    
    def __init__ (self,first, last,code,credits):
        self.first = first 
        self.last = last
        self.code = code
        self.credits = credits


    def tuition(self, code):
        if code == "I":
            tuition  = 250.00
        else:
            tuition = 500.00

        owe = tuition* 12   
        return owe




student_1 = student("Eric", "Hernandez", "I", 12)

print(student_1.first)
print(student_1.last)
print(student_1.code)
print(student_1.credits)
print(student_1.tuition("I"))
print(student_1.tuition("O"))