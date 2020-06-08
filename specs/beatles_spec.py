import unittest

import sys
sys.path.append(".")
sys.path.append("..")
from beatles import *

class FunctionsPracticeTest(unittest.TestCase):

    def setUp(self):
        self.beatles = [
            {"name": "John Lennon", "birth_year": 1940, "death_year": 1980, "instrument": ["piano","guitar"]},
            {"name": "Paul McCartney", "birth_year": 1942, "death_year": None, "instrument": "bass"},
            {"name": "George Harrison", "birth_year": 1943, "death_year": 2001, "instrument": "guitar"},
            {"name": "Ringo Starr", "birth_year": 1940, "death_year": None, "instrument": "drums"}
        ]

    def test_get_member_names(self):
        member_names = get_all_member_names(self.beatles)
        self.assertEqual(len(member_names),4)
        self.assertEqual(member_names[0],"John Lennon")

    def test_get_member_instrument(self):
        self.assertEqual(len(self.beatles[0]["instrument"]),2)
        # print(self.beatles[0]["instrument"])

    def test_get_all_alive_member(self):
        members = get_all_alive_member(self.beatles)
        self.assertEqual(len(members),2)
        # print(members)

    def test_get_all_alive_member_names(self):
        members = get_all_alive_member(self.beatles)
        names = get_all_member_names(members)
        self.assertEqual(len(names),2)
        print(names)
    

    # def test_name_capitalised(self):
    #     greeting = greet("john", "morning")
    #     self.assertEqual(greeting, "Good morning,John")

if __name__ == "__main__":
    unittest.main()
else:
    print("Didn't find main method")