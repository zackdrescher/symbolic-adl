from enum import Enum, unique, auto
import random

from . import adl


def get_random_member(enum: Enum) -> Enum:
    return random.choice(list(enum))


class RandomEnum(Enum):
    @classmethod
    def get_random(cls) -> "RandomEnum":
        return get_random_member(cls)


@unique
class FaceValues(RandomEnum):
    ACE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    TEN = auto()
    PAGE = auto()
    KNIGHT = auto()
    QUEEN = auto()
    KING = auto()


@unique
class Suits(RandomEnum):
    SWORDS = auto()
    CUPS = auto()
    PENTACLES = auto()
    WANDS = auto()


if __name__ == "__main__":

    c = adl.Class(
        "minorArcana", {"faceValue": FaceValues.get_random, "suit": Suits.get_random}
    )
