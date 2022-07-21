from typing import List


class Thing:
    """A thing is an object that has attributes.
    Things typically represent extant objects in the world."""

    def __init__(self):
        self.attr = {}

    @classmethod
    def from_attr(cls, attr):
        thing = cls()
        thing.attr = attr
        return thing

    def has(self, attr: str) -> bool:
        return attr in self.attr

    def get(self, attr: str) -> object:
        if not self.has(attr):
            raise ValueError(f"{self} does not have {attr}")
        return self.attr[attr]

    def __eq__(self, __o: object) -> bool:

        if isinstance(__o, Thing):
            return self.attr == __o.attr
        elif isinstance(__o, dict):
            return self.attr == __o
        else:
            return False

    def create_class(self, name: str, attrs: List[str]) -> "Class":
        class_attr = {k: v for k, v in self.attr.items() if k in attrs}
        return Class(name, attr=class_attr)

    def contains(self, attr: str, thing: "Thing") -> bool:

        if not self.has(attr):
            raise ValueError(f"{self} does not have {attr}")

        attr = self.attr[attr]
        if not isinstance(attr, list):
            raise ValueError(f"{attr} is not a collection")

        return thing in attr


class Class:
    """A class a set of attributes that describte a type of thing.
    Classes can represent a group of things, or a an individual thing.
    Classes can describe things that have a specific attribute or specific
    values of a specific attribute."""

    @classmethod
    def create_from(
        cls, name: str, c: "Class", has: dict = {}, attr: dict = {}
    ) -> "Class":
        has.update(c.has)
        attr.update(c.attr)
        return cls(name, has, attr)

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

    def is_species_of(self, other: "Class") -> bool:
        return is_species(other, self)

    def is_genus_of(self, other: "Class") -> bool:
        return is_species(self, other)


def is_species(genus: Class, species: Class) -> bool:
    # check if speceies has all attributes of genus
    for attr in genus.has:
        if not (attr in species.has or attr in species.attr):
            return False
    for attr in genus.attr:
        if not (attr in species.attr and species.attr[attr] == genus.attr[attr]):
            return False
    return True


class Universe:
    """A universe is a collection of things.
    In principle, the universe is the collection of ALL things. However
    practically, it can be considered as a collection of things of a specific class.
    A Clases can be sampled from universes."""

    def __init__(self):
        self.things = []

    def add_thing(self, thing: Thing):
        self.things.append(thing)

    def add_things(self, things: List[Thing]):
        self.things.extend(things)

    def add_thing(self, thing: dict):
        self.things.append(Thing.from_attr(thing))

    def get_class(self, _class: Class) -> List[Thing]:

        return [thing for thing in self.things if _class.is_member(thing)]

    def exists(self, _class: Class) -> bool:
        return len(self.get_class(_class)) > 0

    def individual(self, _class: Class) -> Thing:
        return len(self.get_class(_class)) == 1
