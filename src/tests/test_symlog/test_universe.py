import unittest

from ...adl import Action
from ...symlog import Universe, AdjunctClass


class TestUniverse(unittest.TestCase):
    def setUp(self) -> None:

        self.c1 = AdjunctClass("c1", {"a": lambda: 0})
        self.c2 = AdjunctClass("c2", {"b": lambda: 0})
        self.c3 = AdjunctClass("c3", {"c": lambda: 0})

        self.u = Universe.from_things(
            [self.c1.create(), self.c1.create(), self.c2.create()]
        )

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
