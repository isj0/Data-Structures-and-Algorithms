class Vehicle:

    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def get_fare(self):
        return self.seating_capacity * 100
    

class Bus(Vehicle):

    def __init__(self, seating_capacity):
        super().__init__(seating_capacity)

    def get_fare(self):
        vehicle_fare = super().get_fare()
        maintenance_fare = 0.1 * vehicle_fare
        total_fare = vehicle_fare + maintenance_fare
        return total_fare
    
v = Vehicle(50)
print("Vehicle Fare:", v.get_fare())

b = Bus(50)
print("Bus fare:", b.get_fare())

