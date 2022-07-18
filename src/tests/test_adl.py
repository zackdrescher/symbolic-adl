import unittest

from .. import adl


class TestThing(unittest.TestCase):
    def setUp(self) -> None:
        self.thing = adl.Thing()

    def test_thing(self):
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
