class vehicle:
    def __init__(self, name, speed, fare):
        self.name = name
        self.speed = speed
        self.fare = fare
class Bus(vehicle):
    pass
School_bus = Bus("School Bus", 160, 0)
City_bus = Bus("City Bus", 160, 2.25)
print("Name:", School_bus.name, "Speed:", School_bus.speed, "fare:", School_bus.fare)
print("Name:", City_bus.name, "Speed:", City_bus.speed, "fare:", City_bus.fare)