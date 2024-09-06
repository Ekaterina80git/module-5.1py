
class Hause:
    def __init__(self,name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self,nev_floor):
         for i in range(1,nev_floor+1):
             if 1 <= nev_floor <= self.number_of_floors:
                 print(i)
             else:
                 print("Такого этажа не существует")
                 break




h1 = Hause("ЖК Горьковский",18)
h2 = Hause("Домик в деревне",2)
h1.go_to(5)
h2.go_to(10)



