class Vehicle:
    def __init__(self, name, speed, milage):
        self.name = name
        self.speed = speed
        self.milage = milage
class Bus(Vehicle):
    pass
School_bus = Bus("School Bus", 160, 12)
print("Name:", School_bus.name, "Speed:", School_bus.speed, "Milage:", School_bus.milage)