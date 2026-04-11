import dataclasses
from enum import Enum
from typing import override, TYPE_CHECKING

from BaseClasses import CollectionState
from NetUtils import JSONMessagePart
from rule_builder.options import OptionFilter
from rule_builder.rules import Rule, False_, True_, Has, Filtered, CanReachRegion, And, Or
from worlds.cornkidz64.constants import item_names, region_names, GameName
from worlds.cornkidz64.options import Movesanity, OpenWollowsHollow, Cranksanity, Fishsanity, Ratsanity

if TYPE_CHECKING:
    from worlds.cornkidz64 import CornKidz


# Helper to convert your List[List[CK64Rule]] into a Rule Builder Tree
def get_logic(dnf_list) -> Rule["CornKidz"]:
    if not dnf_list:
        return True_()

    or_clauses = []
    for and_list in dnf_list:
        if len(and_list) == 1:
            and_clause = and_list[0].value
        elif len(and_list) == 0:
            and_clause = True_()
        else:
            and_clause = And(*[r.value for r in and_list])
        or_clauses.append(and_clause)
    if len(or_clauses) == 1:
        return or_clauses[0]
    elif len(or_clauses) == 0:
        return True_()
    else:
        return Or(*or_clauses)


level_vals = {
    1: 0,
    2: 70,
    3: 140,
    4: 200,
    5: 300,
    6: 360,
}

@dataclasses.dataclass()
class HasLevel(Rule["CornKidz"], game=GameName):
    level: int = 1

    @override
    def _instantiate(self, world: "CornKidz") -> Rule.Resolved:
        return self.Resolved(
            self.level,
            player=world.player,
            caching_enabled=getattr(world, "rule_caching_enabled", False),
        )

    class Resolved(Rule.Resolved):
        level: int = 1

        @override
        def _evaluate(self, state: CollectionState) -> bool:
            return state.count(item_names.XPCube, self.player) + \
                    state.count(item_names.RedScrew, self.player) * 3 + \
                    state.count(item_names.Moth, self.player) * 5 + \
                    state.count(item_names.XPCrystal, self.player) * 10 >= level_vals[self.level]

        @override
        def item_dependencies(self) -> dict[str, set[int]]:
            return {item_names.XPCube: {id(self)}}

        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            verb = "Missing " if state and not self(state) else "Has "
            messages: list[JSONMessagePart] = [{"type": "text", "text": verb}]
            messages.append({"type": "color", "color": "cyan", "text": str(level_vals[self.level])})
            messages.append({"type": "text", "text": "x "})
            if state:
                color = "green" if self(state) else "salmon"
                messages.append({"type": "color", "color": color, "text": item_names.XPCube})
            else:
                messages.append({"type": "item_name", "flags": 0b001, "text": item_names.XPCube, "player": self.player})
            return messages

        @override
        def explain_str(self, state: CollectionState | None = None) -> str:
            if state is None:
                return str(self)
            prefix = "Has" if self(state) else "Missing"
            count = f"{level_vals[self.level]}x "
            return f"{prefix} {count}{item_names.XPCube}"

        @override
        def __str__(self) -> str:
            count = f"{level_vals[self.level]}x "
            return f"Has {count}{item_names.XPCube}"


class CK64Rule(Enum):
    value: Rule

    OpenWollowsHollow = True_(options=[OptionFilter(OpenWollowsHollow, OpenWollowsHollow.option_true)])

    Jump = True_()
    Dive = True_()
    Punch = Has(item_names.Punch, options=[OptionFilter(Movesanity, Movesanity.option_true)], filtered_resolution=True)
    Climb = Has(item_names.Climb, options=[OptionFilter(Movesanity, Movesanity.option_true)], filtered_resolution=True)
    Slam = Has(item_names.Slam, options=[OptionFilter(Movesanity, Movesanity.option_true)], filtered_resolution=True)
    Headbutt = Has(item_names.Headbutt, options=[OptionFilter(Movesanity, Movesanity.option_true)], filtered_resolution=True)
    WallJump =Has(item_names.WallJump, options=[OptionFilter(Movesanity, Movesanity.option_true)], filtered_resolution=True)
    Crouch = Has(item_names.Crouch, options=[OptionFilter(Movesanity, Movesanity.option_true)], filtered_resolution=True)
    Drill = Has(item_names.Drill)

    Level2 = HasLevel(2) & Headbutt
    Level3 = HasLevel(3) & Headbutt
    Level4 = HasLevel(4) & Headbutt
    Level5 = HasLevel(5) & Headbutt
    Level6 = HasLevel(6) & Headbutt

    AllBottlecaps = Has(item_names.BottleCap, count=5)
    AllTrashcans = Has(item_names.TrashCan, count=8)
    AllDiscoBalls = Has(item_names.DiscoBall, count=5)
    CheeseGrater = Has(item_names.CheeseGrater)


    CanUseVoidScrewsButNotLevel6 = Has(item_names.VoidScrew, count=11)
    CanUseAllVoidScrews = Has(item_names.VoidScrew, count=11) & Level6
    AnyVoidScrew = Has(item_names.VoidScrew)
    AnyHPItem = Has(item_names.MegaDreamSoda)

    TowerMovement = Jump & Punch & Climb & Slam & Headbutt & WallJump & Crouch & Drill

    WallJump_Or_Climb = WallJump | Climb
    Jump_Or_Headbutt = Jump | Headbutt
    WallButton = Jump & Headbutt
    HighClimb = Jump & Climb
    Climb_Or_Headbutt = Climb | Headbutt
    WallJump_Or_Headbutt = WallJump | Headbutt
    WallJump_Or_Slam = WallJump | Slam
    Platforming = Jump & WallJump & Climb
    MaxPlatforming = Platforming & Headbutt
    BreakGroundedObject = Headbutt & (Jump | Crouch)
    VerticalHeadbutt = Crouch & Headbutt
    BreakCrystal = Jump & Headbutt
    BreakTrashcan = Punch | (Jump & Headbutt) | (Crouch & Headbutt) | (Jump & Slam)
    BombBird = BreakGroundedObject
    OpenChest = WallButton
    Chameleon = WallButton
    DrillDownwards = Jump & Slam & Drill
    DrillWall = Jump & Headbutt & Drill
    DrillMinimal = Jump & Drill & (Headbutt | Slam)
    CanBeatZombieTurtle = BreakGroundedObject & Punch & Slam
    CanGetHurt = True_()

    CrankMonsterPark = Has(item_names.CrankMonsterPark, options=[OptionFilter(Cranksanity, Cranksanity.option_true)], filtered_resolution=True) & WallButton
    CrankHollowDragonWall = Has(item_names.CrankHollowElevator, options=[OptionFilter(Cranksanity, Cranksanity.option_true)], filtered_resolution=True) & WallButton
    CrankZooSide = Has(item_names.CrankHollowZooWall, options=[OptionFilter(Cranksanity, Cranksanity.option_true)], filtered_resolution=True) & WallButton
    CrankAnxietyTower = Has(item_names.CrankAnxietyTower, options=[OptionFilter(Cranksanity, Cranksanity.option_true)], filtered_resolution=True) & WallButton

    DragonPlatforming = CrankHollowDragonWall & Jump & WallJump & Headbutt
    CanFreeHauntedHouseBird = CanReachRegion(region_names.WollowsHollowHouseTop) & Jump & Slam & CanBeatZombieTurtle

    AllTombstones = CanReachRegion(region_names.WollowsHollowGraveyard) & BreakGroundedObject

    CanReachParkTop = CanReachRegion(region_names.MonsterParkTop)
    CanReachAttic = (Platforming & VerticalHeadbutt) | (CanReachParkTop & Jump & Climb & Headbutt)

    CanReachRooftops = CanReachRegion(region_names.WollowsHollowRooftops)
    CanReachCagedRooftops = CanReachRegion(region_names.WollowsHollowCagedRooftops)
    CanReachGraveyard = CanReachRegion(region_names.WollowsHollowGraveyard)
    CanReachGraveyardTop = CanReachRegion(region_names.WollowsHollowAboveGraveyard)
    CanReachSpinnyChamber = CanReachRegion(region_names.WollowsHollowDrillChamber) & Slam & Drill
    CanReachFlippedHollow = CanReachSpinnyChamber & AllDiscoBalls
    CanEnterFountain = CanReachFlippedHollow & Jump & Headbutt & (Climb | WallJump) & Dive
    CanClimbInteriorTree = CanReachRegion(region_names.WollowsHollowTree) & MaxPlatforming & Slam & Drill

    BatTreeSideRoom = CanReachFlippedHollow & CrankZooSide & Jump & Drill & Headbutt & WallJump
    BatTreeSideRoomCollectables = CanReachRegion(region_names.WollowsHollowTreeSideRoom) & (Slam | WallJump) & Headbutt

    CanAccessGraveyardBomb = CanReachGraveyard & Dive & BombBird & Platforming
    CanKillAllFish = (
            Has(item_names.Fish, count=3, options=[OptionFilter(Fishsanity, Movesanity.option_true)])
            | Filtered(CanClimbInteriorTree & CanAccessGraveyardBomb, options=[OptionFilter(Fishsanity, Movesanity.option_false)])
    )

    CanCleanZoo = CanReachRegion(region_names.WollowsHollowZoo) & (
            Has(item_names.Rat, count=6, options=[OptionFilter(Ratsanity, Movesanity.option_true)])
            | Filtered(MaxPlatforming & Drill & Punch, options=[OptionFilter(Ratsanity, Movesanity.option_false)])
    )
    CanDefeatOwlloh = CanClimbInteriorTree & Level4
    CanUseMetalWorm = Has(item_names.MetalWorm) & (CanCleanZoo | CanGetHurt) & Jump & Headbutt

    MonsterParkHouseButtons = WallButton & WallJump_Or_Climb & Slam

    PostOwllohDefeated = CanDefeatOwlloh

    AnxietyTowerChecks = PostOwllohDefeated & Level5 & MaxPlatforming


