class Car:
      def __init__(self,brand,speed):
            self.brand=brand
            self.speed=speed
      def display(self):
            print(f"brand:{self.brand},speed:{self.speed}km\h")
def create_Car():
          Car1=Car("toyota",180)
          return Car1
my_Car=create_Car()
my_Car.display()

                   
            
     
