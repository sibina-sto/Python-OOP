from unittest import TestCase, main

from vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(50, 200)

    def test_vehicle_init__expect_to_initialized(self):
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual(200, self.vehicle.horse_power)
        self.assertEqual(50, self.vehicle.capacity)
        self.assertEqual(self.vehicle.fuel_consumption, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_vehicle_drive_when_fuel_less_than_fuel_needed_expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.drive(50)
        self.assertEqual("Not enough fuel", str(context.exception))

    def test_vehicle_drive_when_fuel_greater_than_fuel_needed_expect_fuel_decreases(self):
        self.vehicle.drive(30)
        self.assertEqual(12.5, self.vehicle.fuel)

    def test_vehicle_refuel_when_fuel_less_than_fuel_needed_expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.drive(30)
            self.vehicle.refuel(50)
        self.assertEqual("Too much fuel", str(context.exception))

    def test_vehicle_refuel_when_fuel_greater_than_fuel_needed_expect_fuel_increases(self):
        self.vehicle.drive(30)
        self.vehicle.refuel(17.5)
        self.assertEqual(30, self.vehicle.fuel)

    def test_vehicle__str__expect_msg(self):
        self.assertEqual('The vehicle has 200 horse power with 50 fuel left and 1.25 fuel consumption', self.vehicle.__str__())


if __name__ == '__main__':
    main()
