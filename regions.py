from dataclasses import dataclass, field
from typing import List

from .rules import CK64Rule as Rule
from .constants import region_names


@dataclass
class CK64EntranceData:
    target: str
    rules: list[list[Rule]] = field(default_factory=list)
    indirect_conditions: list[str] = field(default_factory=list) # see https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/world%20api.md#an-important-note-on-entrance-access-rules

    def __init__(self, target:str, rules=None, indirect_conditions=None):
        if rules is None:
            rules = []
        if indirect_conditions is None:
            indirect_conditions = []
        self.target = target
        if len(rules) < 1:
            self.rules = [[]]
        elif isinstance(rules[0], Rule):
            self.rules = [rules]
        else:
            self.rules = rules
        self.indirect_conditions = indirect_conditions
        assert isinstance(self.rules, list) and isinstance(self.rules[0], list), f"rules couldn't be converted to a list of lists {rules}"


@dataclass
class CK64RegionData:
    name: str
    connects_to: List[CK64EntranceData] = field(default_factory=list)


region_table: List[CK64RegionData] = [
    CK64RegionData(
        region_names.Menu,
        [
            CK64EntranceData(region_names.Hub)
        ]
    ),

    CK64RegionData(
        region_names.Hub,
        [
            CK64EntranceData(region_names.MonsterPark),
            CK64EntranceData(
                region_names.WollowsHollow,
                [Rule.CanReachParkTop, Rule.Jump, Rule.WallJump],
                [region_names.MonsterParkTop],
            ),
            CK64EntranceData(
                region_names.Tower,
                [Rule.PostOwllohDefeated],
                [region_names.WollowsHollowTree]
            ),
            CK64EntranceData(
                region_names.AnxietyTower,
                [Rule.PostOwllohDefeated, Rule.Level5],
                [region_names.WollowsHollowTree]
            )
        ]
    ),
    # region Park
    CK64RegionData(
        region_names.MonsterPark,
        [
            CK64EntranceData(
                region_names.MonsterParkAcrossLake,
                [[Rule.Swim],
                [Rule.Slam, Rule.Platforming]],
            ),
            CK64EntranceData(
                region_names.MonsterParkHouse,
                [Rule.CrankMonsterPark,
                 Rule.Jump, Rule.WallJump_Or_Headbutt]
            ),
            CK64EntranceData(
                region_names.MonsterParkAttic,
                [Rule.Platforming, Rule.VerticalHeadbutt]
            ),
            CK64EntranceData(
                region_names.MonsterParkSewers,
                [Rule.Swim]
            )
        ]
    ),
    CK64RegionData(region_names.MonsterParkAcrossLake),
    CK64RegionData(
        region_names.MonsterParkHouse,
        [
            CK64EntranceData(
                region_names.MonsterParkHouseFoyer,
                [Rule.Platforming]
            )
        ]
    ),
    CK64RegionData(
        region_names.MonsterParkHouseFoyer,
        [
            CK64EntranceData(
                region_names.MonsterParkTop,
                [Rule.Platforming]
            ),
        ]
    ),
    CK64RegionData(region_names.MonsterParkAttic),
    CK64RegionData(region_names.MonsterParkSewers),
    CK64RegionData(
        region_names.MonsterParkTop,
        [
            CK64EntranceData(
                region_names.MonsterParkAttic,
                [Rule.Jump, Rule.Headbutt, Rule.Climb]
            )
        ]
    ),
    # endregion
    # region Hollow
    CK64RegionData(
        region_names.WollowsHollow,
        [
            CK64EntranceData(
                region_names.WollowsHollowChurch,
                [Rule.MaxPlatforming, Rule.Slam]
            ),
            CK64EntranceData(
                region_names.WollowsHollowMusic,
                [Rule.Level3]
            ),
            CK64EntranceData(
                region_names.WollowsHollowRavine,
                [Rule.DrillMinimal]
            ),
            CK64EntranceData(region_names.WollowsHollowTrinkets),
            CK64EntranceData(
                region_names.WollowsHollowRooftops,
                [Rule.Jump, Rule.WallJump, Rule.Climb]
            ),
            CK64EntranceData(
                region_names.WollowsHollowZooOutside,
                [Rule.Jump, Rule.WallJump, Rule.Headbutt, Rule.Drill]
            ),
            CK64EntranceData(
                region_names.WollowsHollowTree,
                [[Rule.CanReachFlippedHollow, Rule.MaxPlatforming, Rule.Level3],
                [Rule.PostOwllohDefeated, Rule.Platforming]],
                [region_names.WollowsHollowDrillChamber]
            ),
            CK64EntranceData(
                region_names.WollowsHollowTreeSideRoom,
                [Rule.CanReachFlippedHollow, Rule.CrankZooSide,
                 Rule.Jump, Rule.Drill, Rule.Headbutt, Rule.WallJump],
[region_names.WollowsHollowDrillChamber]
            ),
            CK64EntranceData(
                region_names.SomeOtherPlace,
                [Rule.Jump, Rule.Headbutt, Rule.WallJump_Or_Climb]
            )
        ]
    ),
    CK64RegionData(
        region_names.WollowsHollowChurch,
        [
            CK64EntranceData(
                region_names.WollowsHollowAboveGraveyard,
                [Rule.MaxPlatforming]
            ),
            CK64EntranceData(
                region_names.WollowsHollowChurchTop,
                [Rule.MaxPlatforming],
            )
        ]
    ),
    CK64RegionData(region_names.WollowsHollowChurchTop),
    CK64RegionData(
        region_names.WollowsHollowGraveyard,
        [
            CK64EntranceData(
                region_names.WollowsHollow,
                [Rule.Jump, Rule.Headbutt]
            ),
            CK64EntranceData(
                region_names.WollowsHollowHouse,
                [Rule.Level2]
            ),
            CK64EntranceData(
                region_names.WollowsHollowCave,
                [Rule.AllTombstones, Rule.Drill,
                 Rule.Climb, Rule.Jump, Rule.WallJump],
                [region_names.WollowsHollowGraveyard]
            ),
            CK64EntranceData(
                region_names.WollowsHollowHouseTop,
                [Rule.DragonPlatforming, Rule.Jump, Rule.Slam]
            )
        ]
    ),
    CK64RegionData(
        region_names.WollowsHollowAboveGraveyard,
        [
            CK64EntranceData(region_names.WollowsHollowGraveyard)
        ]
    ),
    CK64RegionData(region_names.WollowsHollowHouse),
    CK64RegionData(region_names.WollowsHollowHouseTop),
    CK64RegionData(region_names.WollowsHollowMusic),
    CK64RegionData(region_names.WollowsHollowRavine),
    CK64RegionData(
        region_names.WollowsHollowTrinkets,
        [
            CK64EntranceData(
                region_names.WollowsHollowZombies,
                [Rule.MaxPlatforming, Rule.Punch, Rule.Level3, Rule.CanReachSpinnyChamber]
            )
        ]
    ),
    CK64RegionData(region_names.WollowsHollowZombies),
    CK64RegionData(
        region_names.WollowsHollowRooftops,
        [
            CK64EntranceData(
                region_names.WollowsHollowCagedRooftops,
                [Rule.Jump, Rule.Headbutt, Rule.Climb]
            )
        ]
    ),
    CK64RegionData(
        region_names.WollowsHollowCagedRooftops,
        [
            CK64EntranceData(
                region_names.WollowsHollowDrillChamber,
                [Rule.Jump, Rule.Climb]
            )
        ]
    ),
    CK64RegionData(region_names.WollowsHollowDrillChamber),
    CK64RegionData(
        region_names.WollowsHollowZooOutside,
        [
            CK64EntranceData(
                region_names.WollowsHollowZoo,
                [Rule.Jump, Rule.WallJump, Rule.Headbutt, Rule.Drill]
            )
        ]
    ),
    CK64RegionData(region_names.WollowsHollowZoo),
    CK64RegionData(region_names.WollowsHollowCave),
    CK64RegionData(region_names.WollowsHollowTree),
    CK64RegionData(region_names.WollowsHollowTreeSideRoom),
    # endregion
    # region Misc
    CK64RegionData(region_names.Tower),
    CK64RegionData(region_names.AnxietyTower),
    CK64RegionData(region_names.SomeOtherPlace),
    # endregion
]

