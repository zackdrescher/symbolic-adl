from typing import List


class Thing:
    def __init__(self):
        self.attr = {}

    @classmethod
    def from_attr(cls, attr):
        thing = cls()
        thing.attr = attr
        return thing

    def has(self, attr: str) -> bool:
        return attr in self.attr

    def __eq__(self, __o: object) -> bool:

        if isinstance(__o, Thing):
            return self.attr == __o.attr
        elif isinstance(__o, dict):
            return self.attr == __o


class Class:
    def __init__(self, name: str, has: dict = {}, attrs: dict = {}):
        self.name = name

        for i in has.values():
            if not callable(i):
                raise Exception("has must be a dict of callables")

        self.has = has
        self.attrs = attrs

    def is_member(self, thing: Thing) -> bool:

        for attr in self.has:
            if attr not in thing.attr:
                return False
        for attr in self.attrs:
            if self.attrs[attr] != thing.attr[attr]:
                return False

        return True

    def generate(self) -> dict:
        return {k: v() for k, v in self.has.items()}

    def create(self) -> Thing:
        return Thing.from_attr({**self.generate(), **self.attrs})


class Universe:
    def __init__(self):
        self.things = []

    def add_thing(self, thing: Thing):
        self.things.append(thing)

    def get_class(self, _class: Class) -> List[Thing]:

        return [thing for thing in self.things if _class.is_member(thing)]
