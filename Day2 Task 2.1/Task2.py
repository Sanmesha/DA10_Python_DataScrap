class calculator:
    def __init__(self):
        self.number=[]
    
    def insertnumber(self):
        print("enter the numbers")
        print("enter 0 to exit ")
        count=1
        while count >= 1:
          value=int(input("enter num "+str(count)+"->"))
          if(value==0 and count>5):
            break
          self.number.append(value)
          count+=1
    
    def addition(self):
        sum=0
        for i in self.number:
            sum = sum + i
        print("sum of numbers are "+str(sum))
    def multiplication(self):
        multi=1
        for i in self.number:
            multi = multi * i
        print("multiplication of number are "+str(multi))
    def substraction(self):
        sub=0
        for i in self.number:
            sub= i - sub
        print("substraction of numbers are "+str(sub))
    def division(self):
        div=1
        for i in self.number:
            div = i / div
        print("division of numbers are "+str(div))
    def modulus(self):
        mod=0
        for i in self.number:
            mod = mod % i
        print("modulus of numbers are "+str(mod))
    def percent75(self):
        sum=0
        for i in self.number:
            sum = sum + i
        print('75% is :')
        print(float(0.75*sum))
    def percent25(self):
        sum=0
        for i in self.number:
            sum = sum + i
        print('25% is :')
        print(float(0.25*sum))
    def percent50(self):
        sum=0
        for i in self.number:
            sum = sum + i
        print('50% is :')
        print(float(0.50*sum))
        
    def minimum(self):
        min_value = min(self.number)
        print("minimum of numbers are " + str(min_value))

    def maximum(self):
        max_value = max(self.number)
        print("maximum of numbers are " + str(max_value))
    
    def mean(self):
        mean_value = sum(self.number) / len(self.number)
        print("Mean of the numbers is " + str(mean_value))

    def median(self):
        sorted_numbers = sorted(self.number)
        n = len(sorted_numbers)
        if n % 2 == 0:
            median = (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
            print("Median of numbers is" + str(median))
        else:
            median = sorted_numbers[n//2]
            print("Median of numbers is" + str(median))
    

    
obj=calculator()
obj.insertnumber()
obj.addition()
obj.multiplication()
obj.substraction()
obj.division()
obj.modulus()
obj.percent75()
obj.percent25()
obj.percent50()
obj.maximum()
obj.minimum()
obj.mean()
obj.median()
