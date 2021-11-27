class Person:
    def __init__(self,initialAge):
        if initialAge<0:
            print('Age is not valid, setting age to 0.')
            self.age=0
        else:
            self.age=initialAge

    def amIOld(self):
        if self.age<13:
            print('You are young.')
        elif self.age>=13 and self.age<18:
            print('You are a teenager.')
        else:
            print('You are old.')
    def yearPasses(self):
        self.age=self.age+1

#Added while loops for invalid input and constraints. The editor doesn't allow altering the stub code.

while(True):
    try:
        t = int(input())
        if t<1 or t>4:
            print('Number of test cases should be between 1 and 4.')            
            continue
    except:
        print('Invalid input.')
        continue
    break

for i in range(0, t):
    while(True):
        try:
            age = int(input())
            if age<-5 or age>30:
                print('Constraint error.')
                continue
        except:
            print('Invalid input.')
            continue
        break    
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")