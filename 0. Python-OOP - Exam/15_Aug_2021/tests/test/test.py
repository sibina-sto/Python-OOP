from project.pet_shop import PetShop
from unittest import TestCase, main


class PetShopTests(TestCase):
    def setUp(self) -> None:
        self.pet_shop = PetShop("Test")

    def test_init(self):
        self.assertEqual("Test", self.pet_shop.name)
        self.assertEqual([], self.pet_shop.pets)
        self.assertEqual({}, self.pet_shop.food)

    def test_add_food_invalid_quantity_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.pet_shop.add_food("food", 0)
        self.assertEqual("Quantity cannot be equal to or less than 0", str(ex.exception))

    def test_add_food_valid(self):
        self.assertEqual({}, self.pet_shop.food)
        expected_result = "Successfully added 1000.00 grams of meat."
        actual_result = self.pet_shop.add_food("meat", 1000)
        self.assertEqual(expected_result, actual_result)
        self.assertEqual({"meat": 1000}, self.pet_shop.food)

    def test_add_food_existing_food_quantity_increases(self):
        self.pet_shop.food = {"meat": 5}
        self.pet_shop.add_food("meat", 3)
        self.assertEqual({"meat": 8}, self.pet_shop.food)

    def test_add_pet_valid(self):
        self.assertEqual([], self.pet_shop.pets)
        expected_result = "Successfully added Jerry."
        actual_result = self.pet_shop.add_pet("Jerry")
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(["Jerry"], self.pet_shop.pets)

    def test_add_pet_existing_pet_raises(self):
        self.pet_shop.pets = ["Jerry"]
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet("Jerry")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_feed_pet_not_existing_pet_raises(self):
        self.pet_shop.food = {"meat": 5}
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet("meat", "Jerry")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_not_existing_food_raises(self):
        self.pet_shop.pets = ["Jerry"]
        self.assertEqual({}, self.pet_shop.food)
        expected_result = "You do not have meat"
        actual_result = self.pet_shop.feed_pet("meat", "Jerry")
        self.assertEqual(expected_result, actual_result)

    def test_feed_pet_adds_food(self):
        self.pet_shop.pets = ["Jerry"]
        self.pet_shop.food = {"meat": 50}
        expected_result = "Adding food..."
        actual_result = self.pet_shop.feed_pet("meat", "Jerry")
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(1050.0, self.pet_shop.food["meat"])

    def test_feed_pet_food_valid(self):
        self.pet_shop.pets = ["Jerry"]
        self.pet_shop.food = {"meat": 1100}
        expected_result = "Jerry was successfully fed"
        actual_result = self.pet_shop.feed_pet("meat", "Jerry")
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(1000, self.pet_shop.food["meat"])

    def test_repr_method(self):
        self.pet_shop.pets = ["Jerry", "Tom"]
        expected_result = "Shop Test:\nPets: Jerry, Tom"
        actual_result = repr(self.pet_shop)
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    main()
