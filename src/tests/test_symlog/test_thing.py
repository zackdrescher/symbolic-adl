import unittest

from ... import symlog


class TestNonEmptyThing(unittest.TestCase):
    def setUp(self) -> None:
        self.thing = symlog.Thing()

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
        class_ = symlog.AdjunctClass.create_from_thing("Thing", self.thing, ["a", "b"])
        self.assertTrue(class_.is_member(self.thing))

        class_ = symlog.AdjunctClass.create_from_thing("Thing", self.thing, ["b"])
        self.assertTrue(class_.is_member(self.thing))

        class_ = symlog.AdjunctClass.create_from_thing("Thing", self.thing)
        self.assertTrue(class_.is_member(self.thing))


class TestThingContains(unittest.TestCase):
    def setUp(self) -> None:
        self.thing = symlog.Thing.from_attr({"a": 1, "b": 2})
        self.container = symlog.Thing.from_attr({"contains": []})

    def test_contains(self):
        self.container.attr["contains"].append(self.thing)

        self.assertTrue(self.container.contains("contains", self.thing))

    def test_doesnt_contains(self):

        self.assertFalse(self.container.contains("contains", self.thing))


if __name__ == "__main__":
    unittest.main()
