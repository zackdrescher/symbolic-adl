import unittest

from ...adl import Action
from ...symlog import Universe, AdjunctClass


class TestUniverse(unittest.TestCase):
    def setUp(self) -> None:

        self.c1 = AdjunctClass("c1", {"a": lambda: 0})
        self.c2 = AdjunctClass("c2", {"b": lambda: 0})
        self.c3 = AdjunctClass("c3", {"c": lambda: 0})

        self.thing1 = self.c1.create()
        self.thing2 = self.c1.create()
        self.thing3 = self.c2.create()

        self.u = Universe.from_things([self.thing1, self.thing2, self.thing3])

        self.a1 = Action("a1", {"c1": self.c1}, {"c1": lambda x: x.incr("a")})
        self.a2 = Action("a2", {"c2": self.c2}, {"c2": lambda x: x.incr("b")})
        self.a3 = Action("a3", {"c3": self.c3}, {"c3": lambda x: x.incr("c")})

    def test_len(self):
        self.assertEqual(len(self.u), 3)

    def test_get_class(self):
        self.assertEqual(len(self.u.get_class(AdjunctClass("all"))), 3)
        self.assertEqual(len(self.u.get_class(self.c1)), 2)
        self.assertEqual(len(self.u.get_class(self.c2)), 1)

    def test_exists(self):
        self.assertTrue(self.u.exists(AdjunctClass("all")))
        self.assertTrue(self.u.exists(self.c1))
        self.assertTrue(self.u.exists(self.c2))

        self.assertFalse(self.u.exists(self.c3))

    def test_individual(self):
        self.assertTrue(self.u.individual(self.c2))

        self.assertFalse(self.u.individual(AdjunctClass("all")))
        self.assertFalse(self.u.individual(self.c1))
        self.assertFalse(self.u.individual(self.c3))

    def test_do(self):
        self.u.do(self.a1)
        self.assertEqual(self.thing1.get("a"), 1)
        self.assertEqual(self.thing2.get("a"), 0)
        self.assertFalse(self.thing3.has("a"))

        self.u.do(self.a2)
        self.assertFalse(self.thing1.has("b"))
        self.assertFalse(self.thing2.has("b"))
        self.assertEqual(self.thing3.get("b"), 1)

        self.assertRaises(Exception, self.u.do, self.a3)

        self.assertFalse(self.thing1.has("c"))
        self.assertFalse(self.thing2.has("c"))
        self.assertFalse(self.thing3.has("c"))
