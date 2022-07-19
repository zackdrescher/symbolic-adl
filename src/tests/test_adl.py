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


class TestHasClass(unittest.TestCase):
    def setUp(self) -> None:
        self._class = adl.Class("something", {"a": lambda: 1, "b": lambda: 2})

    def test_is_member(self):
        self.assertTrue(self._class.is_member(adl.Thing.from_attr({"a": 1, "b": 2})))
        self.assertTrue(self._class.is_member(adl.Thing.from_attr({"a": 1, "b": 3})))
        self.assertTrue(
            self._class.is_member(adl.Thing.from_attr({"a": 1, "b": 2, "c": 3}))
        )
        self.assertFalse(self._class.is_member(adl.Thing.from_attr({"b": 2, "c": 3})))
        self.assertFalse(self._class.is_member(adl.Thing()))

    def test_generate(self):
        self.assertEqual(self._class.generate(), {"a": 1, "b": 2})

    def test_create(self):
        self.assertEqual(self._class.create(), adl.Thing.from_attr({"a": 1, "b": 2}))


class TestAttrClass(unittest.TestCase):
    def setUp(self) -> None:
        self._class = adl.Class("something", attr={"a": 1, "b": 2})

    def test_is_member(self):
        self.assertTrue(self._class.is_member(adl.Thing.from_attr({"a": 1, "b": 2})))
        self.assertFalse(self._class.is_member(adl.Thing.from_attr({"a": 1, "b": 3})))
        self.assertTrue(
            self._class.is_member(adl.Thing.from_attr({"a": 1, "b": 2, "c": 3}))
        )
        self.assertFalse(self._class.is_member(adl.Thing.from_attr({"b": 2, "c": 3})))
        self.assertFalse(self._class.is_member(adl.Thing()))

    def test_generate(self):
        self.assertEqual(self._class.generate(), {})

    def test_create(self):
        self.assertEqual(self._class.create(), adl.Thing.from_attr({"a": 1, "b": 2}))


if __name__ == "__main__":
    unittest.main()
