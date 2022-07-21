import unittest

from .. import symblog


class TestNonEmptyThing(unittest.TestCase):
    def setUp(self) -> None:
        self.thing = symblog.Thing()

        self.thing.attr = {"a": 1, "b": 2}

    def test_has(self):
        self.assertTrue(self.thing.has("a"))
        self.assertTrue(self.thing.has("b"))
        self.assertFalse(self.thing.has("c"))

    def test_eq(self):
        self.assertTrue(self.thing == {"a": 1, "b": 2})
        self.assertFalse(self.thing == {"a": 1, "b": 3})
        self.assertFalse(self.thing == {"a": 1, "b": 2, "c": 3})

    def test_create_class(self):
        class_ = symblog.AdjunctClass.create_from_thing("Thing", self.thing, ["a", "b"])
        self.assertTrue(class_.is_member(self.thing))

        class_ = symblog.AdjunctClass.create_from_thing("Thing", self.thing, ["b"])
        self.assertTrue(class_.is_member(self.thing))

        class_ = symblog.AdjunctClass.create_from_thing("Thing", self.thing)
        self.assertTrue(class_.is_member(self.thing))


class TestEmptyClass(unittest.TestCase):
    def setUp(self) -> None:

        self._class = symblog.AdjunctClass("something")

    def test_create(self):
        self.assertEqual(self._class.create(), symblog.Thing())

    def test_is_member(self):
        self.assertTrue(
            self._class.is_member(symblog.Thing.from_attr({"a": 1, "b": 2}))
        )
        self.assertTrue(
            self._class.is_member(symblog.Thing.from_attr({"a": 1, "b": 3}))
        )
        self.assertTrue(
            self._class.is_member(symblog.Thing.from_attr({"a": 1, "b": 2, "c": 3}))
        )
        self.assertTrue(
            self._class.is_member(symblog.Thing.from_attr({"b": 2, "c": 3}))
        )
        self.assertTrue(self._class.is_member(symblog.Thing()))

    def test_is_genus(self):
        self.assertTrue(
            self._class.is_genus_of(symblog.AdjunctClass("something", {"a": lambda: 1}))
        )
        self.assertTrue(
            self._class.is_genus_of(symblog.AdjunctClass("something", {"a": lambda: 2}))
        )
        self.assertTrue(
            self._class.is_genus_of(symblog.AdjunctClass("something", {"b": lambda: 2}))
        )
        self.assertTrue(self._class.is_genus_of(symblog.AdjunctClass("something")))
        self.assertTrue(
            self._class.is_genus_of(symblog.AdjunctClass("something", attr={"a": 1}))
        )

        self.assertTrue(
            self._class.is_genus_of(
                symblog.AdjunctClass("something", {"a": lambda: 1, "b": lambda: 2})
            )
        )
        self.assertTrue(
            self._class.is_genus_of(
                symblog.AdjunctClass(
                    "something", {"a": lambda: 1, "b": lambda: 2, "c": lambda: 3}
                )
            )
        )
        self.assertTrue(
            self._class.is_genus_of(
                symblog.AdjunctClass(
                    "something", {"a": lambda: 1, "b": lambda: 2}, attr={"c": 3}
                )
            )
        )


class TestThingContains(unittest.TestCase):
    def setUp(self) -> None:
        self.thing = symblog.Thing.from_attr({"a": 1, "b": 2})
        self.container = symblog.Thing.from_attr({"contains": []})

    def test_contains(self):
        self.container.attr["contains"].append(self.thing)

        self.assertTrue(self.container.contains("contains", self.thing))

    def test_doesnt_contains(self):

        self.assertFalse(self.container.contains("contains", self.thing))


class TestHasClass(unittest.TestCase):
    def setUp(self) -> None:
        self._class = symblog.AdjunctClass(
            "something", {"a": lambda: 1, "b": lambda: 2}
        )

    def test_is_member(self):
        self.assertTrue(
            self._class.is_member(symblog.Thing.from_attr({"a": 1, "b": 2}))
        )
        self.assertTrue(
            self._class.is_member(symblog.Thing.from_attr({"a": 1, "b": 3}))
        )
        self.assertTrue(
            self._class.is_member(symblog.Thing.from_attr({"a": 1, "b": 2, "c": 3}))
        )
        self.assertFalse(
            self._class.is_member(symblog.Thing.from_attr({"b": 2, "c": 3}))
        )
        self.assertFalse(self._class.is_member(symblog.Thing()))

    def test_generate(self):
        self.assertEqual(self._class.generate(), {"a": 1, "b": 2})

    def test_create(self):
        self.assertEqual(
            self._class.create(), symblog.Thing.from_attr({"a": 1, "b": 2})
        )

    def test_is_genus(self):
        self.assertFalse(
            self._class.is_genus_of(symblog.AdjunctClass("something", {"a": lambda: 1}))
        )
        self.assertFalse(
            self._class.is_genus_of(symblog.AdjunctClass("something", {"a": lambda: 2}))
        )
        self.assertFalse(
            self._class.is_genus_of(symblog.AdjunctClass("something", {"b": lambda: 2}))
        )
        self.assertFalse(self._class.is_genus_of(symblog.AdjunctClass("something")))
        self.assertFalse(
            self._class.is_genus_of(symblog.AdjunctClass("something", attr={"a": 1}))
        )

        self.assertTrue(
            self._class.is_genus_of(
                symblog.AdjunctClass("something", {"a": lambda: 1, "b": lambda: 2})
            )
        )
        self.assertTrue(
            self._class.is_genus_of(
                symblog.AdjunctClass(
                    "something", {"a": lambda: 1, "b": lambda: 2, "c": lambda: 3}
                )
            )
        )
        self.assertTrue(
            self._class.is_genus_of(
                symblog.AdjunctClass(
                    "something", {"a": lambda: 1, "b": lambda: 2}, attr={"c": 3}
                )
            )
        )
        self.assertTrue(
            self._class.is_genus_of(
                symblog.AdjunctClass("something", attr={"a": 1, "b": 2})
            )
        )
        self.assertTrue(
            self._class.is_genus_of(
                symblog.AdjunctClass("something", attr={"a": 3, "b": 4})
            )
        )
        self.assertTrue(
            self._class.is_genus_of(
                symblog.AdjunctClass("something", attr={"a": 3, "b": 4, "c": 5})
            )
        )
        self.assertTrue(
            self._class.is_genus_of(
                symblog.AdjunctClass(
                    "something", {"x": lambda: 5}, attr={"a": 3, "b": 4, "c": 5}
                )
            )
        )


class TestAttrClass(unittest.TestCase):
    def setUp(self) -> None:
        self._class = symblog.AdjunctClass("something", attr={"a": 1, "b": 2})

    def test_is_member(self):
        self.assertTrue(
            self._class.is_member(symblog.Thing.from_attr({"a": 1, "b": 2}))
        )
        self.assertFalse(
            self._class.is_member(symblog.Thing.from_attr({"a": 1, "b": 3}))
        )
        self.assertTrue(
            self._class.is_member(symblog.Thing.from_attr({"a": 1, "b": 2, "c": 3}))
        )
        self.assertFalse(
            self._class.is_member(symblog.Thing.from_attr({"b": 2, "c": 3}))
        )
        self.assertFalse(self._class.is_member(symblog.Thing()))

    def test_generate(self):
        self.assertEqual(self._class.generate(), {})

    def test_create(self):
        self.assertEqual(
            self._class.create(), symblog.Thing.from_attr({"a": 1, "b": 2})
        )

    def test_is_genus(self):
        self.assertFalse(
            self._class.is_genus_of(symblog.AdjunctClass("something", {"a": lambda: 1}))
        )
        self.assertFalse(
            self._class.is_genus_of(symblog.AdjunctClass("something", {"a": lambda: 2}))
        )
        self.assertFalse(
            self._class.is_genus_of(symblog.AdjunctClass("something", {"b": lambda: 2}))
        )
        self.assertFalse(self._class.is_genus_of(symblog.AdjunctClass("something")))
        self.assertFalse(
            self._class.is_genus_of(symblog.AdjunctClass("something", attr={"a": 1}))
        )
        self.assertFalse(
            self._class.is_genus_of(
                symblog.AdjunctClass("something", {"a": lambda: 1, "b": lambda: 2})
            )
        )
        self.assertFalse(
            self._class.is_genus_of(
                symblog.AdjunctClass(
                    "something", {"a": lambda: 1, "b": lambda: 2, "c": lambda: 3}
                )
            )
        )
        self.assertFalse(
            self._class.is_genus_of(
                symblog.AdjunctClass(
                    "something", {"a": lambda: 1, "b": lambda: 2}, attr={"c": 3}
                )
            )
        )

        self.assertTrue(
            self._class.is_genus_of(
                symblog.AdjunctClass(
                    "something", {"a": lambda: 1, "b": lambda: 2}, attr={"a": 1, "b": 2}
                )
            )
        )
        self.assertTrue(
            self._class.is_genus_of(
                symblog.AdjunctClass("something", attr={"a": 1, "b": 2})
            )
        )
        self.assertTrue(
            self._class.is_genus_of(
                symblog.AdjunctClass("something", attr={"a": 1, "b": 2, "c": 3})
            )
        )
        self.assertTrue(
            self._class.is_genus_of(
                symblog.AdjunctClass(
                    "something",
                    {"a": lambda: 1, "b": lambda: 2, "c": lambda: 3},
                    attr={"a": 1, "b": 2},
                )
            )
        )

        self.assertFalse(
            self._class.is_genus_of(
                symblog.AdjunctClass("something", attr={"a": 3, "b": 4})
            )
        )
        self.assertFalse(
            self._class.is_genus_of(
                symblog.AdjunctClass("something", attr={"a": 3, "b": 4, "c": 5})
            )
        )
        self.assertFalse(
            self._class.is_genus_of(
                symblog.AdjunctClass(
                    "something", {"x": lambda: 5}, attr={"a": 3, "b": 4, "c": 5}
                )
            )
        )


class TestContianerClass(unittest.TestCase):
    def setUp(self) -> None:
        self.thing = symblog.Thing.from_attr({"a": 1, "b": 2})

        self.container_class = symblog.AdjunctClass(
            "container", has={"contains": lambda: []}
        )
        self.container_thing = self.container_class.create()

        self.thing_container_class = symblog.AdjunctClass(
            "thingContainer", attr={"contains": [self.thing]}
        )

    def test_is_not_member(self):

        self.assertFalse(self.thing_container_class.is_member(self.container_thing))

        other_thing = symblog.Thing.from_attr({"c": 3})
        self.container_thing.get("contains").append(other_thing)
        self.assertFalse(self.thing_container_class.is_member(self.container_thing))

    def test_is_member(self):
        self.container_thing.get("contains").append(self.thing)
        self.assertTrue(self.thing_container_class.is_member(self.container_thing))

        other_thing = symblog.Thing.from_attr({"c": 3})
        self.container_thing.get("contains").append(other_thing)
        self.assertTrue(self.thing_container_class.is_member(self.container_thing))

    def test_genus(self):

        self.assertTrue(self.container_class.is_genus_of(self.thing_container_class))


class TestClassCraeteFrom(unittest.TestCase):
    def setUp(self) -> None:

        self._class = symblog.AdjunctClass(
            "something", has={"c": lambda: 1}, attr={"a": 1, "b": 2}
        )

    def test_has(self):

        t = symblog.AdjunctClass.create_from_class(
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

        t = symblog.AdjunctClass.create_from_class("sub", self._class, attr={"d": 1})

        self.assertTrue("c" in t.has)
        self.assertTrue("d" in t.attr)
        self.assertTrue("a" in t.attr)
        self.assertTrue("b" in t.attr)

        self.assertFalse("c" in t.attr)
        self.assertFalse("d" in t.has)
        self.assertFalse("a" in t.has)
        self.assertFalse("b" in t.has)

    def test_species(self):
        t = symblog.AdjunctClass.create_from_class(
            "sub", self._class, has={"d": lambda: 1}
        )

        self.assertTrue(t.is_species_of(self._class))


if __name__ == "__main__":
    unittest.main()
