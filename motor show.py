class three_of_car:
    not_akkawed_names=["toyota","mazda","honda"]

    count_of_cars=0
    #methods of class out constractor
    def __init__(self, name, model, history, sales):
        self.name=name

        self.model=model

        self.history=history

        self.sales=sales
        three_of_car.count_of_cars += 1

    def car_info(self):
        if self.name in three_of_car.not_akkawed_names:
            raise ValueError("name not allawed")
        else:
            return f"car name is :  {self.name}\n models is  :  {self.model} \n sales is   :  {self.sales}\n\n"

    def delate_name(self):
        three_of_car.count_of_cars-=1
        return f"the {self.name} is delated"
    def deleta_car(self):
            cars=input("enter the name to removed : ")
            if cars in three_of_car.delate_name():
                return f"the cars is {self.name}"
print(three_of_car.count_of_cars)
bmw=three_of_car("bnw","bmw -2",2020,"10000000$")
print(three_of_car.count_of_cars)
marceds=three_of_car("marceds","marceds s-class",2020,"1000000$")
print(three_of_car.count_of_cars)
lixes=three_of_car("lixes","lixes -2",2020,"100000$")
print(three_of_car.count_of_cars)
hiundai=three_of_car("huindai","amg",2020,"100000$")
print(three_of_car.count_of_cars)

print(hiundai.delate_name())

print(bmw.car_info())

print(marceds.car_info()) 

print(lixes.car_info())

print(hiundai.car_info())

print(three_of_car.count_of_cars)

print(f"the count of cars is in show {three_of_car.count_of_cars}")