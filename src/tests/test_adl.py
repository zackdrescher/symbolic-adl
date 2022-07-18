import unittest

from .. import adl


class TestThing(unittest.TestCase):
    def setUp(self) -> None:
        self.thing = adl.Thing()

    def test_has(self):
        self.thing.attr = {"a": 1, "b": 2}
        self.assertTrue(self.thing.has("a"))
        self.assertTrue(self.thing.has("b"))
        self.assertFalse(self.thing.has("c"))


if __name__ == "__main__":
    unittest.main()
