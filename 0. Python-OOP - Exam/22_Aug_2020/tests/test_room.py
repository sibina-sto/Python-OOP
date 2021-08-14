import unittest
from project.rooms.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("TestName", 100, 2)

    def test_room_init(self):
        self.assertEqual("TestName", self.room.family_name)
        self.assertEqual(100, self.room.budget)
        self.assertEqual(2, self.room.members_count)
        self.assertEqual([], self.room.children)
        self.assertEqual(0, self.room.expenses)

    def test_room_expenses__when_value_is_negative__expect_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.room.expenses = -1

        self.assertEqual("Expenses cannot be negative", str(context.exception))

    def test_room_expenses__when_value_is_positive__expect_to_change_expenses_to_its_value(self):
        self.room.expenses = 5
        self.assertEqual(5, self.room.expenses)


if __name__ == '__main__':
    unittest.main()
