from re import S
import unittest

from .. import adl


class TestNonEmptyThing(unittest.TestCase):
    def setUp(self) -> None:
        self.thing = adl.Thing()

        self.thing.attr = {"a": 1, "b": 2}

    def test_has(self):
        self.assertTrue(self.thing.has("a"))
        self.assertTrue(self.thing.has("b"))
        self.assertFalse(self.thing.has("c"))

    def test_eq(self):
        self.assertTrue(self.thing == {"a": 1, "b": 2})
        self.assertFalse(self.thing == {"a": 1, "b": 3})
        self.assertFalse(self.thing == {"a": 1, "b": 2, "c": 3})


class TestEmptyClass(unittest.TestCase):
    def setUp(self) -> None:

        self._class = adl.Class("something")

    def test_generate(self):
        self.assertEqual(self._class.generate(), adl.Thing())


if __name__ == "__main__":
    unittest.main()
