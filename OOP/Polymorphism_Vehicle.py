class Car:
  def start(self):
    print(f"Car start with key")

class Bike:
  def start(self):
    print(f"Bike start with button")

class Bus:
  def start(self):
    print("Bus start with engine")


def start_vehicle(vehicle_type):
  vehicle_type.start()


start_vehicle(Car())
start_vehicle(Bike())
start_vehicle(Bus())
