class Car:
    def __init__(self,color,speed,model,brand):
        self.color=color
        self.speed=speed
        self.model=model
        self.brand=brand

    def start(self):
        print("Hello! the car has started. Put your foot on the pedal")
    
    def stop(self):
        print("Hold up! the engine isn't on! The car has stopped")

    def speedup(self):
        print("Watch out! you are passing the speed limit" )

    def change_gear(self,gear_type):
        print("The gear has changed")

lambo=Car("lime",120,"aventador","lamborghini")

print(lambo.start())