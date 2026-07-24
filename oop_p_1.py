class Car:
    vehicle='car'

    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def start(self):
        print(self.brand,self.model,"is starting")


car1=Car("Toyota","Corolla")


print(car1.brand,'is a',car1.model)


car1.start()


car2=Car("Honda","Civic")


print(car2.brand,'is a',car2.model)


car2.start()