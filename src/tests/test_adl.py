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

    def test_create(self):
        self.assertEqual(self._class.create(), adl.Thing())

    def test_is_member(self):
        self.assertTrue(self._class.is_member(adl.Thing.from_attr({"a": 1, "b": 2})))
        self.assertTrue(self._class.is_member(adl.Thing.from_attr({"a": 1, "b": 3})))
        self.assertTrue(
            self._class.is_member(adl.Thing.from_attr({"a": 1, "b": 2, "c": 3}))
        )
        self.assertTrue(self._class.is_member(adl.Thing.from_attr({"b": 2, "c": 3})))
        self.assertTrue(self._class.is_member(adl.Thing()))

    def test_is_genus(self):
        self.assertTrue(
            self._class.is_genus_of(adl.Class("something", {"a": lambda: 1}))
        )
        self.assertTrue(
            self._class.is_genus_of(adl.Class("something", {"a": lambda: 2}))
        )
        self.assertTrue(
            self._class.is_genus_of(adl.Class("something", {"b": lambda: 2}))
        )
        self.assertTrue(self._class.is_genus_of(adl.Class("something")))
        self.assertTrue(self._class.is_genus_of(adl.Class("something", attr={"a": 1})))

        self.assertTrue(
            self._class.is_genus_of(
                adl.Class("something", {"a": lambda: 1, "b": lambda: 2})
            )
        )
        self.assertTrue(
            self._class.is_genus_of(
                adl.Class("something", {"a": lambda: 1, "b": lambda: 2, "c": lambda: 3})
            )
        )
        self.assertTrue(
            self._class.is_genus_of(
                adl.Class("something", {"a": lambda: 1, "b": lambda: 2}, attr={"c": 3})
            )
        )


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

    def test_is_genus(self):
        self.assertFalse(
            self._class.is_genus_of(adl.Class("something", {"a": lambda: 1}))
        )
        self.assertFalse(
            self._class.is_genus_of(adl.Class("something", {"a": lambda: 2}))
        )
        self.assertFalse(
            self._class.is_genus_of(adl.Class("something", {"b": lambda: 2}))
        )
        self.assertFalse(self._class.is_genus_of(adl.Class("something")))
        self.assertFalse(self._class.is_genus_of(adl.Class("something", attr={"a": 1})))

        self.assertTrue(
            self._class.is_genus_of(
                adl.Class("something", {"a": lambda: 1, "b": lambda: 2})
            )
        )
        self.assertTrue(
            self._class.is_genus_of(
                adl.Class("something", {"a": lambda: 1, "b": lambda: 2, "c": lambda: 3})
            )
        )
        self.assertTrue(
            self._class.is_genus_of(
                adl.Class("something", {"a": lambda: 1, "b": lambda: 2}, attr={"c": 3})
            )
        )
        self.assertTrue(
            self._class.is_genus_of(adl.Class("something", attr={"a": 1, "b": 2}))
        )
        self.assertTrue(
            self._class.is_genus_of(adl.Class("something", attr={"a": 3, "b": 4}))
        )
        self.assertTrue(
            self._class.is_genus_of(
                adl.Class("something", attr={"a": 3, "b": 4, "c": 5})
            )
        )
        self.assertTrue(
            self._class.is_genus_of(
                adl.Class("something", {"x": lambda: 5}, attr={"a": 3, "b": 4, "c": 5})
            )
        )


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

    def test_is_genus(self):
        self.assertFalse(
            self._class.is_genus_of(adl.Class("something", {"a": lambda: 1}))
        )
        self.assertFalse(
            self._class.is_genus_of(adl.Class("something", {"a": lambda: 2}))
        )
        self.assertFalse(
            self._class.is_genus_of(adl.Class("something", {"b": lambda: 2}))
        )
        self.assertFalse(self._class.is_genus_of(adl.Class("something")))
        self.assertFalse(self._class.is_genus_of(adl.Class("something", attr={"a": 1})))
        self.assertFalse(
            self._class.is_genus_of(
                adl.Class("something", {"a": lambda: 1, "b": lambda: 2})
            )
        )
        self.assertFalse(
            self._class.is_genus_of(
                adl.Class("something", {"a": lambda: 1, "b": lambda: 2, "c": lambda: 3})
            )
        )
        self.assertFalse(
            self._class.is_genus_of(
                adl.Class("something", {"a": lambda: 1, "b": lambda: 2}, attr={"c": 3})
            )
        )

        self.assertTrue(
            self._class.is_genus_of(
                adl.Class(
                    "something", {"a": lambda: 1, "b": lambda: 2}, attr={"a": 1, "b": 2}
                )
            )
        )
        self.assertTrue(
            self._class.is_genus_of(adl.Class("something", attr={"a": 1, "b": 2}))
        )
        self.assertTrue(
            self._class.is_genus_of(
                adl.Class("something", attr={"a": 1, "b": 2, "c": 3})
            )
        )
        self.assertTrue(
            self._class.is_genus_of(
                adl.Class(
                    "something",
                    {"a": lambda: 1, "b": lambda: 2, "c": lambda: 3},
                    attr={"a": 1, "b": 2},
                )
            )
        )

        self.assertFalse(
            self._class.is_genus_of(adl.Class("something", attr={"a": 3, "b": 4}))
        )
        self.assertFalse(
            self._class.is_genus_of(
                adl.Class("something", attr={"a": 3, "b": 4, "c": 5})
            )
        )
        self.assertFalse(
            self._class.is_genus_of(
                adl.Class("something", {"x": lambda: 5}, attr={"a": 3, "b": 4, "c": 5})
            )
        )


if __name__ == "__main__":
    unittest.main()
