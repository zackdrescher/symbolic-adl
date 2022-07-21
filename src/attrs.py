from enum import Enum, unique, auto
import random

from . import symlog


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


@unique
class MajorArcana(RandomEnum):
    THE_FOOL = auto()
    THE_MAGICIAN = auto()
    THE_HGIH_PRIESTESS = auto()
    THE_EMPRESS = auto()
    THE_EMPEROR = auto()
    THE_HIEROPHANT = auto()
    THE_LOVERS = auto()
    THE_CHARIOT = auto()
    JUSTICE = auto()
    THE_HERMIT = auto()
    THE_WHEEL = auto()
    STRENGTH = auto()
    THE_HANGED_MAN = auto()
    DEATH = auto()
    TEMPERANCE = auto()
    THE_DEVIL = auto()
    THE_TOWER = auto()
    THE_STAR = auto()
    THE_MOON = auto()
    THE_SUN = auto()
    JUDGEMENT = auto()
    THE_WORLD = auto()


if __name__ == "__main__":

    ma = symlog.AdjunctClass(
        "minorArcana", {"faceValue": FaceValues.get_random, "suit": Suits.get_random}
    )

    k = symlog.AdjunctClass(
        "kingdom", has={"units": lambda: [ma.create() for _ in range(4)]}
    )

    print("done~")
