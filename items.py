import typing
from dataclasses import dataclass

from BaseClasses import Item, ItemClassification
from .constants import item_names, GameName, BaseId


@dataclass
class CK64ItemData:
    name: str
    classification: ItemClassification

    def is_progression(self):
        return self.classification & ItemClassification.progression == ItemClassification.progression

    def is_trap(self):
        return self.classification & ItemClassification.trap == ItemClassification.trap

    def is_filler(self):
        return self.classification & ItemClassification.filler == ItemClassification.filler


class CornKidzItem(Item):
    game: str = GameName


base_id = 3116411600

item_table: list[CK64ItemData] = [
    # region Movement
    CK64ItemData(
        item_names.Jump,
        ItemClassification.progression,
    ),
    CK64ItemData(
        item_names.Punch,
        ItemClassification.progression,
    ),
    CK64ItemData(
        item_names.Climb,
        ItemClassification.progression,
    ),
    CK64ItemData(
        item_names.Slam,
        ItemClassification.progression,
    ),
    CK64ItemData(
        item_names.Headbutt,
        ItemClassification.progression,
    ),
    CK64ItemData(
        item_names.WallJump,
        ItemClassification.progression,
    ),
    CK64ItemData(
        item_names.Swim,
        ItemClassification.progression,
    ),
    CK64ItemData(
        item_names.Crouch,
        ItemClassification.progression,
    ),
    CK64ItemData(
        item_names.Drill,
        ItemClassification.progression,
    ),
    CK64ItemData(
        item_names.FallWarp,
        ItemClassification.useful,
    ),
    # endregion
    # region Cranks
    CK64ItemData(
        item_names.CrankMonsterPark,
        ItemClassification.progression,
    ),
    CK64ItemData(
        item_names.CrankHollowElevator,
        ItemClassification.progression,
    ),
    CK64ItemData(
        item_names.CrankHollowZooWall,
        ItemClassification.progression,
    ),
    CK64ItemData(
        item_names.CrankAnxietyTower,
        ItemClassification.progression,
    ),
    # endregion
    # region Collectables
    CK64ItemData(
        item_names.BottleCap,
        ItemClassification.progression,
    ),
    CK64ItemData(
        item_names.TrashCan,
        ItemClassification.progression,
    ),
    CK64ItemData(
        item_names.DiscoBall,
        ItemClassification.progression,
    ),
    CK64ItemData(
        item_names.Rat,
        ItemClassification.progression,
    ),
    CK64ItemData(
        item_names.Fish,
        ItemClassification.progression,
    ),
    CK64ItemData(
        item_names.MetalWorm,
        ItemClassification.progression,
    ),
    CK64ItemData(
        item_names.MegaDreamSoda,
        ItemClassification.progression,
    ),
    CK64ItemData(
        item_names.CheeseGrater,
        ItemClassification.progression,
    ),
    CK64ItemData(
        item_names.VoidScrew,
        ItemClassification.progression,
    ),
    # endregion
    # region Progression
    # CK64ItemData(
    #     item_names.XP,
    #     ItemClassification.progression,
    # ),
    CK64ItemData(
        item_names.XPCube,
        ItemClassification.progression,
    ),
    CK64ItemData(
        item_names.RedScrew,
        ItemClassification.progression,
    ),
    CK64ItemData(
        item_names.Moth,
        ItemClassification.progression,
    ),
    CK64ItemData(
        item_names.XPCrystal,
        ItemClassification.progression,
    ),
    # endregion
    # region Filler
    CK64ItemData(
        item_names.DreamSoda,
        ItemClassification.filler,
    ),
    # endregion
    # region Traps
    CK64ItemData(
        item_names.SlapTrap,
        ItemClassification.trap,
    ),
    CK64ItemData(
        item_names.SlipTrap,
        ItemClassification.trap,
    ),
    CK64ItemData(
        item_names.SkidTrap,
        ItemClassification.trap,
    ),
    # endregion
]

lookup_id_to_name: typing.Dict[int, str] = {BaseId + i: data.name for i, data in enumerate(item_table)}
lookup_name_to_id: typing.Dict[str, int] = {v: k for k, v in lookup_id_to_name.items()}


def get_trap_item_names() -> list[str]:
    return [item_data.name for item_data in item_table
            if item_data.classification & ItemClassification.trap == ItemClassification.trap]


def get_filler_item_names() -> list[str]:
    return [item_data.name for item_data in item_table
            if item_data.classification & (~ItemClassification.skip_balancing) == ItemClassification.filler]
