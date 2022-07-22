from typing import List

from .thing import Thing


class AdjunctClass:
    """An Adjunct Class (i.e. class) a set of attributes that describes a type
    of thing. Classes can represent a group of things, or a an individual thing.
    Classes can describe things that have a specific attribute or specific
    values of a specific attribute."""

    @classmethod
    def create_from_class(
        cls, name: str, c: "AdjunctClass", has: dict = {}, attr: dict = {}
    ) -> "AdjunctClass":

        has.update(c.has)
        attr.update(c.attr)

        return cls(name, has, attr)

    @classmethod
    def create_from_thing(
        cls, name: str, thing: Thing, attrs: List[str] = []
    ) -> "AdjunctClass":

        if not attrs:
            class_attr = thing.attr
        else:
            class_attr = {k: v for k, v in thing.attr.items() if k in attrs}

        return AdjunctClass(name, attr=class_attr)

    def __init__(self, name: str, has: dict = {}, attr: dict = {}):
        self.name = name

        for i in has.values():
            if not callable(i):
                raise Exception("has must be a dict of callables")

        self.has = has
        self.attr = attr

    def is_member(self, thing: Thing) -> bool:

        for attr in self.has:
            if attr not in thing.attr:
                return False
        for attr in self.attr:
            if attr not in thing.attr:
                return False
            a = self.attr[attr]
            if isinstance(a, list):
                # check that everything in this attr is in the thing
                for t in a:
                    if not thing.contains(attr, t):
                        return False
            elif self.attr[attr] != thing.attr[attr]:
                return False

        return True

    def generate(self) -> dict:
        return {k: v() for k, v in self.has.items()}

    def create(self) -> Thing:
        return Thing.from_attr({**self.generate(), **self.attr})

    def create_n(self, n: int) -> List[Thing]:
        return [self.create() for _ in range(n)]

    def is_species_of(self, other: "AdjunctClass") -> bool:
        return is_species(other, self)

    def is_genus_of(self, other: "AdjunctClass") -> bool:
        return is_species(self, other)


def is_species(genus: AdjunctClass, species: AdjunctClass) -> bool:
    # check if speceies has all attributes of genus
    for attr in genus.has:
        if not (attr in species.has or attr in species.attr):
            return False
    for attr in genus.attr:
        if not (attr in species.attr and species.attr[attr] == genus.attr[attr]):
            return False
    return True
