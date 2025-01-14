import unittest

from ... import symlog


class TestEmptyClass(unittest.TestCase):
    def setUp(self) -> None:

        self._class = symlog.AdjunctClass("something")

    def test_create(self):
        self.assertEqual(self._class.create(), symlog.Thing())

    def test_is_member(self):
        self.assertTrue(self._class.is_member(symlog.Thing.from_attr({"a": 1, "b": 2})))
        self.assertTrue(self._class.is_member(symlog.Thing.from_attr({"a": 1, "b": 3})))
        self.assertTrue(
            self._class.is_member(symlog.Thing.from_attr({"a": 1, "b": 2, "c": 3}))
        )
        self.assertTrue(self._class.is_member(symlog.Thing.from_attr({"b": 2, "c": 3})))
        self.assertTrue(self._class.is_member(symlog.Thing()))

    def test_is_genus(self):
        self.assertTrue(
            self._class.is_genus_of(symlog.AdjunctClass("something", {"a": lambda: 1}))
        )
        self.assertTrue(
            self._class.is_genus_of(symlog.AdjunctClass("something", {"a": lambda: 2}))
        )
        self.assertTrue(
            self._class.is_genus_of(symlog.AdjunctClass("something", {"b": lambda: 2}))
        )
        self.assertTrue(self._class.is_genus_of(symlog.AdjunctClass("something")))
        self.assertTrue(
            self._class.is_genus_of(symlog.AdjunctClass("something", attr={"a": 1}))
        )

        self.assertTrue(
            self._class.is_genus_of(
                symlog.AdjunctClass("something", {"a": lambda: 1, "b": lambda: 2})
            )
        )
        self.assertTrue(
            self._class.is_genus_of(
                symlog.AdjunctClass(
                    "something", {"a": lambda: 1, "b": lambda: 2, "c": lambda: 3}
                )
            )
        )
        self.assertTrue(
            self._class.is_genus_of(
                symlog.AdjunctClass(
                    "something", {"a": lambda: 1, "b": lambda: 2}, attr={"c": 3}
                )
            )
        )


class TestHasClass(unittest.TestCase):
    def setUp(self) -> None:
        self._class = symlog.AdjunctClass("something", {"a": lambda: 1, "b": lambda: 2})

    def test_is_member(self):
        self.assertTrue(self._class.is_member(symlog.Thing.from_attr({"a": 1, "b": 2})))
        self.assertTrue(self._class.is_member(symlog.Thing.from_attr({"a": 1, "b": 3})))
        self.assertTrue(
            self._class.is_member(symlog.Thing.from_attr({"a": 1, "b": 2, "c": 3}))
        )
        self.assertFalse(
            self._class.is_member(symlog.Thing.from_attr({"b": 2, "c": 3}))
        )
        self.assertFalse(self._class.is_member(symlog.Thing()))

    def test_generate(self):
        self.assertEqual(self._class.generate(), {"a": 1, "b": 2})

    def test_create(self):
        self.assertEqual(self._class.create(), symlog.Thing.from_attr({"a": 1, "b": 2}))

    def test_is_genus(self):
        self.assertFalse(
            self._class.is_genus_of(symlog.AdjunctClass("something", {"a": lambda: 1}))
        )
        self.assertFalse(
            self._class.is_genus_of(symlog.AdjunctClass("something", {"a": lambda: 2}))
        )
        self.assertFalse(
            self._class.is_genus_of(symlog.AdjunctClass("something", {"b": lambda: 2}))
        )
        self.assertFalse(self._class.is_genus_of(symlog.AdjunctClass("something")))
        self.assertFalse(
            self._class.is_genus_of(symlog.AdjunctClass("something", attr={"a": 1}))
        )

        self.assertTrue(
            self._class.is_genus_of(
                symlog.AdjunctClass("something", {"a": lambda: 1, "b": lambda: 2})
            )
        )
        self.assertTrue(
            self._class.is_genus_of(
                symlog.AdjunctClass(
                    "something", {"a": lambda: 1, "b": lambda: 2, "c": lambda: 3}
                )
            )
        )
        self.assertTrue(
            self._class.is_genus_of(
                symlog.AdjunctClass(
                    "something", {"a": lambda: 1, "b": lambda: 2}, attr={"c": 3}
                )
            )
        )
        self.assertTrue(
            self._class.is_genus_of(
                symlog.AdjunctClass("something", attr={"a": 1, "b": 2})
            )
        )
        self.assertTrue(
            self._class.is_genus_of(
                symlog.AdjunctClass("something", attr={"a": 3, "b": 4})
            )
        )
        self.assertTrue(
            self._class.is_genus_of(
                symlog.AdjunctClass("something", attr={"a": 3, "b": 4, "c": 5})
            )
        )
        self.assertTrue(
            self._class.is_genus_of(
                symlog.AdjunctClass(
                    "something", {"x": lambda: 5}, attr={"a": 3, "b": 4, "c": 5}
                )
            )
        )


class TestAttrClass(unittest.TestCase):
    def setUp(self) -> None:
        self._class = symlog.AdjunctClass("something", attr={"a": 1, "b": 2})

    def test_is_member(self):
        self.assertTrue(self._class.is_member(symlog.Thing.from_attr({"a": 1, "b": 2})))
        self.assertFalse(
            self._class.is_member(symlog.Thing.from_attr({"a": 1, "b": 3}))
        )
        self.assertTrue(
            self._class.is_member(symlog.Thing.from_attr({"a": 1, "b": 2, "c": 3}))
        )
        self.assertFalse(
            self._class.is_member(symlog.Thing.from_attr({"b": 2, "c": 3}))
        )
        self.assertFalse(self._class.is_member(symlog.Thing()))

    def test_generate(self):
        self.assertEqual(self._class.generate(), {})

    def test_create(self):
        self.assertEqual(self._class.create(), symlog.Thing.from_attr({"a": 1, "b": 2}))

    def test_is_genus(self):
        self.assertFalse(
            self._class.is_genus_of(symlog.AdjunctClass("something", {"a": lambda: 1}))
        )
        self.assertFalse(
            self._class.is_genus_of(symlog.AdjunctClass("something", {"a": lambda: 2}))
        )
        self.assertFalse(
            self._class.is_genus_of(symlog.AdjunctClass("something", {"b": lambda: 2}))
        )
        self.assertFalse(self._class.is_genus_of(symlog.AdjunctClass("something")))
        self.assertFalse(
            self._class.is_genus_of(symlog.AdjunctClass("something", attr={"a": 1}))
        )
        self.assertFalse(
            self._class.is_genus_of(
                symlog.AdjunctClass("something", {"a": lambda: 1, "b": lambda: 2})
            )
        )
        self.assertFalse(
            self._class.is_genus_of(
                symlog.AdjunctClass(
                    "something", {"a": lambda: 1, "b": lambda: 2, "c": lambda: 3}
                )
            )
        )
        self.assertFalse(
            self._class.is_genus_of(
                symlog.AdjunctClass(
                    "something", {"a": lambda: 1, "b": lambda: 2}, attr={"c": 3}
                )
            )
        )

        self.assertTrue(
            self._class.is_genus_of(
                symlog.AdjunctClass(
                    "something", {"a": lambda: 1, "b": lambda: 2}, attr={"a": 1, "b": 2}
                )
            )
        )
        self.assertTrue(
            self._class.is_genus_of(
                symlog.AdjunctClass("something", attr={"a": 1, "b": 2})
            )
        )
        self.assertTrue(
            self._class.is_genus_of(
                symlog.AdjunctClass("something", attr={"a": 1, "b": 2, "c": 3})
            )
        )
        self.assertTrue(
            self._class.is_genus_of(
                symlog.AdjunctClass(
                    "something",
                    {"a": lambda: 1, "b": lambda: 2, "c": lambda: 3},
                    attr={"a": 1, "b": 2},
                )
            )
        )

        self.assertFalse(
            self._class.is_genus_of(
                symlog.AdjunctClass("something", attr={"a": 3, "b": 4})
            )
        )
        self.assertFalse(
            self._class.is_genus_of(
                symlog.AdjunctClass("something", attr={"a": 3, "b": 4, "c": 5})
            )
        )
        self.assertFalse(
            self._class.is_genus_of(
                symlog.AdjunctClass(
                    "something", {"x": lambda: 5}, attr={"a": 3, "b": 4, "c": 5}
                )
            )
        )


class TestContianerClass(unittest.TestCase):
    def setUp(self) -> None:
        self.thing = symlog.Thing.from_attr({"a": 1, "b": 2})

        self.container_class = symlog.AdjunctClass(
            "container", has={"contains": lambda: []}
        )
        self.container_thing = self.container_class.create()

        self.thing_container_class = symlog.AdjunctClass(
            "thingContainer", attr={"contains": [self.thing]}
        )

    def test_is_not_member(self):

        self.assertFalse(self.thing_container_class.is_member(self.container_thing))

        other_thing = symlog.Thing.from_attr({"c": 3})
        self.container_thing.get("contains").append(other_thing)
        self.assertFalse(self.thing_container_class.is_member(self.container_thing))

    def test_is_member(self):
        self.container_thing.get("contains").append(self.thing)
        self.assertTrue(self.thing_container_class.is_member(self.container_thing))

        other_thing = symlog.Thing.from_attr({"c": 3})
        self.container_thing.get("contains").append(other_thing)
        self.assertTrue(self.thing_container_class.is_member(self.container_thing))

    def test_genus(self):

        self.assertTrue(self.container_class.is_genus_of(self.thing_container_class))


class TestClassCraeteFrom(unittest.TestCase):
    def setUp(self) -> None:

        self._class = symlog.AdjunctClass(
            "something", has={"c": lambda: 1}, attr={"a": 1, "b": 2}
        )

    def test_has(self):

        t = symlog.AdjunctClass.create_from_class(
            "sub", self._class, has={"d": lambda: 1}
        )

        self.assertTrue("c" in t.has)
        self.assertTrue("d" in t.has)
        self.assertTrue("a" in t.attr)
        self.assertTrue("b" in t.attr)

        self.assertFalse("c" in t.attr)
        self.assertFalse("d" in t.attr)
        self.assertFalse("a" in t.has)
        self.assertFalse("b" in t.has)

    def test_attr(self):

        t = symlog.AdjunctClass.create_from_class("sub", self._class, attr={"d": 1})

        self.assertTrue("c" in t.has)
        self.assertTrue("d" in t.attr)
        self.assertTrue("a" in t.attr)
        self.assertTrue("b" in t.attr)

        self.assertFalse("c" in t.attr)
        self.assertFalse("d" in t.has)
        self.assertFalse("a" in t.has)
        self.assertFalse("b" in t.has)

    def test_species(self):
        t = symlog.AdjunctClass.create_from_class(
            "sub", self._class, has={"d": lambda: 1}
        )

        self.assertTrue(t.is_species_of(self._class))


if __name__ == "__main__":
    unittest.main()
