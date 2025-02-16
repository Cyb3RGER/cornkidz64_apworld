import typing
from dataclasses import dataclass, field

from BaseClasses import Location
from BaseClasses import LocationProgressType
from .options import Goal
from .rules import CK64Rule as Rule
from .constants import location_names, region_names, GameName, BaseId
from enum import IntEnum


class CornKidzLocation(Location):
    game = GameName


class CornKidzLocationType(IntEnum):
    SAVEITEM = 1,
    UPGRADE = 2,
    ACHIEVEMENT = 3,
    SWITCH = 4,
    TEXT = 5,
    RAT = 6,
    EVENT = 7


@dataclass
class CK64LocationData:
    name: str
    game_id: typing.Optional[int]
    region: str
    # Rule lists are OR'd together.
    text: typing.Optional[str]  # text for LocationProgressType.Text
    rules: list[list[Rule]] = field(default_factory=list)
    type: CornKidzLocationType = CornKidzLocationType.SAVEITEM  # this doesn't do anything rn, just for me to keep track
    progress_type: LocationProgressType = LocationProgressType.DEFAULT  # ignored for now

    def __init__(self, name: str, game_id: typing.Optional[int], region: str, rules=None, _type: CornKidzLocationType = CornKidzLocationType.SAVEITEM, progress_type: LocationProgressType = LocationProgressType.DEFAULT, text: typing.Optional[str] = None):
        if rules is None:
            rules = []
        if text is None and type == CornKidzLocationType.TEXT:
            text = name
        self.name = name
        self.game_id = game_id
        self.region = region
        if len(rules) < 1:
            self.rules = [[]]
        elif isinstance(rules[0], Rule):
            self.rules = [rules]
        else:
            self.rules = rules
        self.progress_type = progress_type
        self.type = _type
        self.text = text
        assert isinstance(self.rules, list) and isinstance(self.rules[0], list), f"rules couldn't be converted to a list of lists {rules}"


location_table: list[CK64LocationData] = [
    # region Park Cubes
    CK64LocationData(
        location_names.CubeParkNearSlide, 116,
        region_names.MonsterPark,
        [Rule.Jump, Rule.WallJump_Or_Climb],
    ),
    CK64LocationData(
        location_names.CubeParkSlide, 100,
        region_names.MonsterPark,
        [Rule.Climb, Rule.Jump, Rule.WallJump],
    ),
    CK64LocationData(
        location_names.CubeParkUnderSlide, 118,
        region_names.MonsterPark,
        [Rule.Jump, Rule.WallJump_Or_Climb],
    ),
    CK64LocationData(
        location_names.CubeParkBouncyMoose, 113,
        region_names.MonsterPark,
        [Rule.Slam],
    ),
    CK64LocationData(
        location_names.CubeParkTopHat, 106,
        region_names.MonsterPark,
        [Rule.WallButton, Rule.Platforming, Rule.Slam],
    ),
    CK64LocationData(
        location_names.CubeParkWater1, 101,
        region_names.MonsterParkAcrossLake,
        [Rule.Swim],
    ),
    CK64LocationData(
        location_names.CubeParkWater2, 102,
        region_names.MonsterParkAcrossLake,
        [Rule.Swim],
    ),
    CK64LocationData(
        location_names.CubeParkAcrossWater1, 103,
        region_names.MonsterParkAcrossLake,
        [Rule.Jump, Rule.WallJump_Or_Climb],
    ),
    CK64LocationData(
        location_names.CubeParkAcrossWater2, 104,
        region_names.MonsterParkAcrossLake,
    ),
    CK64LocationData(
        location_names.CubeParkAcrossWater3, 119,
        region_names.MonsterParkAcrossLake,
        [Rule.BombBird],
    ),
    CK64LocationData(
        location_names.CubeParkAcrossWater4, 105,
        region_names.MonsterParkAcrossLake,
        [Rule.Platforming],
    ),
    CK64LocationData(
        location_names.CubeStoneStatue1, 122,
        region_names.MonsterParkAcrossLake,
        [Rule.Platforming, Rule.Slam],
    ),
    CK64LocationData(
        location_names.CubeStoneStatue2, 123,
        region_names.MonsterParkAcrossLake,
        [Rule.Platforming, Rule.Slam],
    ),
    CK64LocationData(
        location_names.CubeStoneStatue3, 124,
        region_names.MonsterParkAcrossLake,
        [Rule.Platforming, Rule.Slam],
    ),
    CK64LocationData(
        location_names.CubeParkFence, 112,
        region_names.MonsterPark,
        [Rule.Jump, Rule.WallJump],
    ),
    CK64LocationData(
        location_names.CubeParkLowerSlamPillar, 120,
        region_names.MonsterPark,
        [Rule.Jump, Rule.WallJump],
    ),
    CK64LocationData(
        location_names.CubeParkUpperSlamPillar, 121,
        region_names.MonsterPark,
        [[Rule.Jump, Rule.WallJump, Rule.VerticalHeadbutt],
         [Rule.CanReachParkTop, Rule.Headbutt]],
    ),
    CK64LocationData(
        location_names.CubeParkAtticDrill1, 126,
        region_names.MonsterParkAttic,
        [Rule.BreakGroundedObject, Rule.Jump, Rule.WallJump, Rule.Drill],
    ),
    CK64LocationData(
        location_names.CubeParkAtticDrill2, 127,
        region_names.MonsterParkAttic,
        [Rule.BreakGroundedObject, Rule.Jump, Rule.WallJump, Rule.Drill],
    ),
    CK64LocationData(
        location_names.CubeParkAtticHigh1, 128,
        region_names.MonsterParkAttic,
        [Rule.BreakGroundedObject, Rule.Platforming, Rule.Drill],
    ),
    CK64LocationData(
        location_names.CubeParkAtticHigh2, 130,
        region_names.MonsterParkAttic,
        [Rule.BreakGroundedObject, Rule.Platforming, Rule.Drill],
    ),
    CK64LocationData(
        location_names.CubeParkAtticHallway, 129,
        region_names.MonsterParkAttic,
        [Rule.BreakGroundedObject, Rule.Platforming],
    ),
    CK64LocationData(
        location_names.CubeParkHouseBookcase, 117,
        region_names.MonsterParkHouse,
    ),
    CK64LocationData(
        location_names.CubeParkHouseFoyer1, 107,
        region_names.MonsterParkHouseFoyer,
        [Rule.Jump, Rule.Headbutt, Rule.WallJump_Or_Climb],
    ),
    CK64LocationData(
        location_names.CubeParkHouseFoyer2, 115,
        region_names.MonsterParkHouseFoyer,
        [Rule.Jump, Rule.Headbutt, Rule.WallJump_Or_Climb],
    ),
    CK64LocationData(
        location_names.CubeParkHouseFoyer3, 114,
        region_names.MonsterParkHouseFoyer,
        [[Rule.MaxPlatforming],
         [Rule.CanReachParkTop, Rule.Climb]],
    ),
    CK64LocationData(
        location_names.CubeParkHouseFoyerTower, 131,
        region_names.MonsterParkHouseFoyer,
        [[Rule.MaxPlatforming],
         [Rule.CanReachParkTop, Rule.Jump_Or_Headbutt]],
    ),
    CK64LocationData(
        location_names.CubeParkTopBouncyMoose, 125,
        region_names.MonsterParkTop,
        [Rule.Slam, Rule.Headbutt, Rule.WallJump],
    ),
    CK64LocationData(
        location_names.CubeParkTopButtonChallenge1, 109,
        region_names.MonsterParkTop,
        [Rule.Platforming, Rule.Headbutt],
    ),
    CK64LocationData(
        location_names.CubeParkTopButtonChallenge2, 110,
        region_names.MonsterParkTop,
        [Rule.Platforming, Rule.Headbutt],
    ),
    CK64LocationData(
        location_names.CubeParkTopButtonChallenge3, 111,
        region_names.MonsterParkTop,
        [Rule.Platforming, Rule.Headbutt],
    ),
    CK64LocationData(
        location_names.CubeParkDrillPastLake, 108,
        region_names.MonsterParkAcrossLake,
        [Rule.DrillDownwards],
    ),
    # endregion
    # region Park Screws
    CK64LocationData(
        location_names.ScrewParkLakeBombYeet, 135,
        region_names.MonsterParkAcrossLake,
        [Rule.BombBird, Rule.Slam, Rule.Swim],
    ),
    CK64LocationData(
        location_names.ScrewParkAtticScrewScrew, 137,
        region_names.MonsterParkAttic,
        [Rule.BreakGroundedObject, Rule.Jump, Rule.Headbutt, Rule.WallJump],
    ),
    CK64LocationData(
        location_names.ScrewParkAtticDrill, 136,
        region_names.MonsterParkAttic,
        [Rule.BreakGroundedObject, Rule.Platforming, Rule.Headbutt, Rule.Drill],
    ),
    CK64LocationData(
        location_names.ScrewParkAboveCrank, 134,
        region_names.MonsterParkAcrossLake,
        [[Rule.Platforming, Rule.Slam, Rule.Headbutt],
         [Rule.CanReachParkTop, Rule.Headbutt]],
    ),
    CK64LocationData(
        location_names.ScrewParkHouseFoyer, 138,
        region_names.MonsterParkHouseFoyer,
        [Rule.Jump, Rule.WallJump, Rule.Headbutt],
    ),
    CK64LocationData(
        location_names.ScrewParkTopWallJumpChallenge, 133,
        region_names.MonsterParkTop,
        [Rule.Jump, Rule.Slam, Rule.WallJump, Rule.WallJump_Or_Climb, Rule.Headbutt],
    ),
    # endregion
    # region Park Chameleons
    CK64LocationData(
        location_names.ChameleonPark, 139,
        region_names.MonsterPark,
        [Rule.Chameleon],
    ),
    CK64LocationData(
        location_names.ChameleonInterior, 140,
        region_names.MonsterParkHouse,
        [Rule.Chameleon],
    ),
    # endregion
    # region Park Crystals
    CK64LocationData(
        location_names.CrystalParkAttic, 143,
        region_names.MonsterParkAttic,
        [Rule.Jump, Rule.WallJump, Rule.BreakCrystal],
    ),
    CK64LocationData(
        location_names.CrystalGarbageGrump, 144,
        region_names.MonsterParkSewers,
        [Rule.AllTrashcans, Rule.BreakGroundedObject],
    ),
    # endregion
    # region Park Mirrors
    CK64LocationData(
        location_names.MirrorParkSewers, 142,
        region_names.MonsterParkSewers,
        [Rule.Platforming, Rule.Headbutt],
    ),
    CK64LocationData(
        location_names.MirrorFoyerLevel3, 141,
        region_names.MonsterParkHouseFoyer,
        [Rule.Level3, Rule.Slam, Rule.Headbutt, Rule.Jump, Rule.WallJump_Or_Climb],
    ),
    # endregion
    # region Park Cranks
    CK64LocationData(
        location_names.CrankMonsterParkAcrossLake, 132,
        region_names.MonsterParkAcrossLake,
        [Rule.OpenChest, Rule.Platforming],
    ),
    # endregion
    # region Trash Cans
    CK64LocationData(
        location_names.TrashCanPark, 152,
        region_names.MonsterPark,
        [Rule.BreakTrashcan],
    ),
    CK64LocationData(
        location_names.TrashCanAttic1, 153,
        region_names.MonsterParkAttic,
        [Rule.Jump, Rule.WallJump, Rule.Headbutt, Rule.BreakTrashcan],
    ),
    CK64LocationData(
        location_names.TrashCanAttic2, 151,
        region_names.MonsterParkAttic,
        [Rule.Platforming, Rule.BreakTrashcan],
    ),
    CK64LocationData(
        location_names.TrashCanSewers, 148,
        region_names.MonsterParkSewers,
        [Rule.Jump, Rule.WallJump, Rule.BreakTrashcan],
    ),
    CK64LocationData(
        location_names.TrashCanFoyer, 155,
        region_names.MonsterParkHouseFoyer,
        [Rule.Jump, Rule.Headbutt, Rule.WallJump_Or_Climb, Rule.BreakTrashcan],
    ),
    CK64LocationData(
        location_names.TrashCanParkTop, 150,
        region_names.MonsterParkTop,
        [Rule.CanReachParkTop, Rule.BreakTrashcan],
    ),
    CK64LocationData(
        location_names.TrashCanParkTopWallJumpChallenge, 149,
        region_names.MonsterParkTop,
        [Rule.Jump, Rule.Slam, Rule.WallJump, Rule.WallJump_Or_Climb, Rule.BreakTrashcan],
    ),
    CK64LocationData(
        location_names.TrashCanFoyerLevel3, 154,
        region_names.MonsterParkHouseFoyer,
        [Rule.Level3, Rule.BreakTrashcan],
    ),
    # endregion
    # region Hollow Cubes
    CK64LocationData(
        location_names.CubeHollowBridge1, 254,
        region_names.WollowsHollow,
    ),
    CK64LocationData(
        location_names.CubeHollowBridge2, 275,
        region_names.WollowsHollow,
    ),
    CK64LocationData(
        location_names.CubeHollowBridge3, 276,
        region_names.WollowsHollow,
    ),
    CK64LocationData(
        location_names.CubeHollowOnTrees, 209,
        region_names.WollowsHollow,
        [Rule.Jump, Rule.Slam],
    ),
    CK64LocationData(
        location_names.CubeHollowLeavesUnderOwlTree, 225,
        region_names.WollowsHollow,
    ),
    CK64LocationData(
        location_names.CubeHollowLeavesOnOwlTree, 226,
        region_names.WollowsHollow,
        [Rule.Jump],
    ),
    CK64LocationData(
        location_names.CubeHollowPillar1, 216,
        region_names.WollowsHollow,
        [Rule.Jump, Rule.WallJump],
    ),
    CK64LocationData(
        location_names.CubeHollowPillar2, 217,
        region_names.WollowsHollow,
        [Rule.Jump, Rule.WallJump, Rule.Headbutt],
    ),
    CK64LocationData(
        location_names.CubeHollowTrampoline, 266,
        region_names.WollowsHollow,
        [Rule.Slam],
    ),
    CK64LocationData(
        location_names.CubeHollowTrinketShop, 232,
        region_names.WollowsHollowTrinkets,
        [Rule.MaxPlatforming, Rule.CanReachSpinnyChamber],
    ),
    CK64LocationData(
        location_names.CubeHollowClockWallClimb1, 231,
        region_names.WollowsHollow,
        [Rule.Platforming],
    ),
    CK64LocationData(
        location_names.CubeHollowClockWallClimb2, 230,
        region_names.WollowsHollow,
        [Rule.MaxPlatforming],
    ),
    CK64LocationData(
        location_names.CubeHollowPillarOutsideChurch, 224,
        region_names.WollowsHollow,
        [Rule.Jump, Rule.Climb_Or_Headbutt, Rule.WallJump],
    ),
    CK64LocationData(
        location_names.CubeHollowClockwiseVomit, 265,
        region_names.WollowsHollow,
        [Rule.Jump, Rule.Slam],
    ),
    CK64LocationData(
        location_names.CubeHollowFartTunnel1, 215,
        region_names.WollowsHollow,
    ),
    CK64LocationData(
        location_names.CubeHollowFartTunnel2, 214,
        region_names.WollowsHollow,
        [Rule.Jump, Rule.WallJump],
    ),
    CK64LocationData(
        location_names.CubeHollowChurch1, 233,
        region_names.WollowsHollowChurch,
        [Rule.Jump, Rule.Climb, Rule.WallJump_Or_Headbutt],
    ),
    CK64LocationData(
        location_names.CubeHollowChurch2, 255,
        region_names.WollowsHollowChurch,
        [Rule.MaxPlatforming],
    ),
    CK64LocationData(
        location_names.CubeHollowChurch3, 271,
        region_names.WollowsHollowChurch,
        [Rule.MaxPlatforming],
    ),
    CK64LocationData(
        location_names.CubeHollowGraveyardPole1, 273,
        region_names.WollowsHollowGraveyard,
        [Rule.Climb],
    ),
    CK64LocationData(
        location_names.CubeHollowGraveyardTacoCat, 261,
        region_names.WollowsHollowGraveyard,
        [Rule.Platforming],
    ),
    CK64LocationData(
        location_names.CubeHollowGraveyardPole2, 274,
        region_names.WollowsHollowGraveyard,
        [[Rule.Climb],
         [Rule.CanReachGraveyardTop]],
    ),
    CK64LocationData(
        location_names.CubeHollowGraveyardBehindWetTree, 253,
        region_names.WollowsHollowGraveyard,
        [Rule.Platforming],
    ),
    CK64LocationData(
        location_names.CubeHollowGraveyardWater, 256,
        region_names.WollowsHollowGraveyard,
        [Rule.Swim],
    ),
    CK64LocationData(
        location_names.CubeHollowGraveyardTombstoneCode1, 262,
        region_names.WollowsHollowGraveyard,
        [Rule.BreakGroundedObject],
    ),
    CK64LocationData(
        location_names.CubeHollowGraveyardTombstoneCode2, 263,
        region_names.WollowsHollowGraveyard,
        [Rule.BreakGroundedObject],
    ),
    CK64LocationData(
        location_names.CubeHollowGraveyardTombstoneCode3, 264,
        region_names.WollowsHollowGraveyard,
        [Rule.BreakGroundedObject],
    ),
    CK64LocationData(
        location_names.CubeHollowBalcony1, 210,
        region_names.WollowsHollow,
        [Rule.Jump, Rule.Climb, Rule.Headbutt],
    ),
    CK64LocationData(
        location_names.CubeHollowBalcony2, 211,
        region_names.WollowsHollow,
        [Rule.Jump, Rule.Climb, Rule.Headbutt],
    ),
    CK64LocationData(
        location_names.CubeHollowNearBats1, 218,
        region_names.WollowsHollowCagedRooftops,
    ),
    CK64LocationData(
        location_names.CubeHollowNearBats2, 219,
        region_names.WollowsHollowCagedRooftops,
    ),
    CK64LocationData(
        location_names.CubeHollowDrillRoom1, 242,
        region_names.WollowsHollowDrillChamber,
        [Rule.DrillDownwards],
    ),
    CK64LocationData(
        location_names.CubeHollowDrillRoom2, 244,
        region_names.WollowsHollowDrillChamber,
        [Rule.DrillDownwards],
    ),
    CK64LocationData(
        location_names.CubeHollowDrillRoom3, 246,
        region_names.WollowsHollowDrillChamber,
        [Rule.DrillDownwards],
    ),
    CK64LocationData(
        location_names.CubeHollowDrillUnderRamp, 248,
        region_names.WollowsHollow,
        [Rule.DrillMinimal],
    ),
    CK64LocationData(
        location_names.CubeHollowDrillBars1, 220,
        region_names.WollowsHollow,
        [Rule.DrillMinimal],
    ),
    CK64LocationData(
        location_names.CubeHollowDrillBars2, 221,
        region_names.WollowsHollow,
        [Rule.DrillMinimal],
    ),
    CK64LocationData(
        location_names.CubeHollowDrillUnderChurch1, 236,
        region_names.WollowsHollow,
        [Rule.DrillMinimal],
    ),
    CK64LocationData(
        location_names.CubeHollowDrillUnderChurch2, 238,
        region_names.WollowsHollow,
        [Rule.DrillMinimal],
    ),
    CK64LocationData(
        location_names.CubeHollowDrillDragonMountainside1, 212,
        region_names.WollowsHollow,
        [[Rule.CanReachGraveyard, Rule.Slam, Rule.Drill],
         [Rule.DragonPlatforming, Rule.Drill]],
    ),
    CK64LocationData(
        location_names.CubeHollowDrillDragonMountainside2, 213,
        region_names.WollowsHollow,
        [[Rule.CanReachGraveyard, Rule.Slam, Rule.Drill],
         [Rule.DragonPlatforming, Rule.Drill]],
    ),
    CK64LocationData(
        location_names.CubeHollowHauntedHouseTop1, 222,
        region_names.WollowsHollow,
        [Rule.DragonPlatforming],
    ),
    CK64LocationData(
        location_names.CubeHollowHauntedHouseTop2, 223,
        region_names.WollowsHollow,
        [Rule.DragonPlatforming],
    ),
    CK64LocationData(
        location_names.CubeHollowHauntedHouseBehindChimney, 272,
        region_names.WollowsHollowHouseTop,
    ),
    CK64LocationData(
        location_names.CubeHollowRavine1, 229,
        region_names.WollowsHollowRavine,
        [Rule.Jump, Rule.WallJump, Rule.Climb_Or_Headbutt],
    ),
    CK64LocationData(
        location_names.CubeHollowRavine2, 227,
        region_names.WollowsHollowRavine,
        [Rule.Platforming],
    ),
    CK64LocationData(
        location_names.CubeHollowRavine3, 228,
        region_names.WollowsHollowRavine,
        [Rule.Platforming],
    ),
    CK64LocationData(
        location_names.CubeHollowFencedAcrossRavine, 277,
        region_names.WollowsHollowRavine,
        [Rule.MaxPlatforming],
    ),
    CK64LocationData(
        location_names.CubeHollowMusicBoxSwim1, 278,
        region_names.WollowsHollowMusic,
        [Rule.Swim],
    ),
    CK64LocationData(
        location_names.CubeHollowMusicBoxSwim2, 279,
        region_names.WollowsHollowMusic,
        [Rule.Swim],
    ),
    CK64LocationData(
        location_names.CubeHollowBrickWall1, 234,
        region_names.WollowsHollow,
        [[Rule.Jump, Rule.Headbutt, Rule.Slam, Rule.Climb_Or_Headbutt],
         [Rule.CanReachCagedRooftops, Rule.CanGetHurt]],
    ),
    CK64LocationData(
        location_names.CubeHollowBrickWall2, 235,
        region_names.WollowsHollowMusic,
        [[Rule.Jump, Rule.Headbutt, Rule.Slam, Rule.Climb_Or_Headbutt],
         [Rule.CanReachCagedRooftops, Rule.CanGetHurt]],
    ),
    CK64LocationData(
        location_names.CubeHollowBehindSanitaryZoo, 240,
        region_names.WollowsHollowZooOutside,
        [Rule.DrillDownwards],
    ),
    CK64LocationData(
        location_names.CubeHollowSpiderOutsideZoo, 252,
        region_names.WollowsHollowZooOutside,
        [Rule.Jump, Rule.Headbutt, Rule.Climb],
    ),
    CK64LocationData(
        location_names.CubeFlippedHollowDragonCrankDrill, 250,
        region_names.WollowsHollowTreeSideRoom,
        [Rule.BatTreeSideRoomCollectables],
    ),
    CK64LocationData(
        location_names.CubeFlippedHollowFountainSwim1, 267,
        region_names.WollowsHollow,
        [Rule.CanEnterFountain],
    ),
    CK64LocationData(
        location_names.CubeFlippedHollowFountainSwim2, 268,
        region_names.WollowsHollow,
        [Rule.CanEnterFountain],
    ),
    CK64LocationData(
        location_names.CubeFlippedHollowFountainSwim3, 269,
        region_names.WollowsHollow,
        [Rule.CanEnterFountain],
    ),
    CK64LocationData(
        location_names.CubeFlippedHollowFountainSwim4, 270,
        region_names.WollowsHollow,
        [Rule.CanEnterFountain],
    ),
    CK64LocationData(
        location_names.CubeHollowTreeFishTimer, 257,
        region_names.WollowsHollowTree,
        [Rule.Jump, Rule.Headbutt, Rule.Swim],
    ),
    CK64LocationData(
        location_names.CubeHollowTreeSwim, 259,
        region_names.WollowsHollowTree,
        [Rule.Swim],
    ),
    CK64LocationData(
        location_names.CubeHollowTreeNearMetalWorm, 258,
        region_names.WollowsHollowTree,
        [Rule.CanClimbInteriorTree],
    ),
    CK64LocationData(
        location_names.CubeHollowGraveyardSpiderCaveDrill, 260,
        region_names.WollowsHollowGraveyard,
        [Rule.Swim, Rule.BombBird, Rule.Platforming, Rule.Slam, Rule.Drill],
    ),
    # endregion
    # region Hollow Screws
    CK64LocationData(
        location_names.ScrewHollowTownClock, 203,
        region_names.WollowsHollow,
        [Rule.MaxPlatforming, Rule.Headbutt, Rule.CanReachFlippedHollow],
    ),
    CK64LocationData(
        location_names.ScrewHollowDrillTowerAlcove, 200,
        region_names.WollowsHollowCagedRooftops,
    ),
    CK64LocationData(
        location_names.ScrewHollowBehindHauntedHouse, 202,
        region_names.WollowsHollowGraveyard,
        [Rule.Jump, Rule.Headbutt],
    ),
    CK64LocationData(
        location_names.ScrewHollowDragonCave, 208,
        region_names.WollowsHollowCave,
        [Rule.Slam],
    ),
    CK64LocationData(
        location_names.ScrewHollowLargeCrankPit, 201,
        region_names.WollowsHollow,
        [Rule.Jump, Rule.Headbutt],
    ),
    CK64LocationData(
        location_names.ScrewHollowZoo, 207,
        region_names.WollowsHollowZoo,
        [Rule.MaxPlatforming, Rule.Drill],
    ),
    CK64LocationData(
        location_names.ScrewFlippedHollowTreeSideRoom, 204,
        region_names.WollowsHollow,
        [Rule.BatTreeSideRoomCollectables],
    ),
    CK64LocationData(
        location_names.ScrewHollowTreeHighScrew, 205,
        region_names.WollowsHollowTree,
        [Rule.MaxPlatforming, Rule.BatTreeSideRoomCollectables],
    ),
    CK64LocationData(
        location_names.ScrewHollowTreeLowScrew, 206,
        region_names.WollowsHollowTree,
        [Rule.MaxPlatforming],
    ),
    # endregion
    # region Hollow Chameleons
    CK64LocationData(
        location_names.ChameleonHollowBush, 297,
        region_names.WollowsHollow,
        [Rule.Chameleon],
    ),
    CK64LocationData(
        location_names.ChameleonHollowGraveyard, 296,
        region_names.WollowsHollowGraveyard,
        [Rule.Chameleon],
    ),
    # endregion
    # region Hollow Crystals
    CK64LocationData(
        location_names.CrystalHollowTimedFountain, 283,
        region_names.WollowsHollow,
        [Rule.Jump, Rule.WallJump_Or_Climb, Rule.Headbutt],
    ),
    CK64LocationData(
        location_names.CrystalHollowChurchBell, 282,
        region_names.WollowsHollowChurchTop,
        [Rule.MaxPlatforming],
    ),
    CK64LocationData(
        location_names.CrystalHollowGraveyardSpiderReward, 291,
        region_names.WollowsHollowGraveyard,
        [Rule.CheeseGrater],
    ),
    CK64LocationData(
        location_names.CrystalHollowDrillPillar, 286,
        region_names.WollowsHollow,
        [[Rule.MaxPlatforming, Rule.DrillDownwards],
         [Rule.CanReachRooftops, Rule.DrillDownwards, Rule.Headbutt]],
    ),
    CK64LocationData(
        location_names.CrystalHollowHauntedHouseFreeBird, 285,
        region_names.WollowsHollowHouse,
        [Rule.Jump, Rule.Headbutt, Rule.CanFreeHauntedHouseBird],
    ),
    CK64LocationData(
        location_names.CrystalHollowDragonCave, 295,
        region_names.WollowsHollowCave,
        [Rule.Jump, Rule.Headbutt, Rule.WallJump, Rule.Slam],
    ),
    CK64LocationData(
        location_names.CrystalHollowAboveEntry, 280,
        region_names.WollowsHollowRavine,
        [Rule.MaxPlatforming],
    ),
    CK64LocationData(
        location_names.CrystalHollowZombieChamber, 292,
        region_names.WollowsHollowZombies,
        [Rule.MaxPlatforming, Rule.CanBeatZombieTurtle, Rule.Drill],
    ),
    CK64LocationData(
        location_names.CrystalHollowFreeStuckPig, 294,
        region_names.WollowsHollow,
        [Rule.Jump, Rule.Headbutt],
    ),
    CK64LocationData(
        location_names.CrystalHollowBombChurchPillar, 281,
        region_names.WollowsHollow,
        [Rule.Jump, Rule.Headbutt],
    ),
    CK64LocationData(
        location_names.CrystalFlippedHollowCounterclockwiseVomit, 293,
        region_names.WollowsHollow,
        [Rule.Jump, Rule.Slam, Rule.CanReachFlippedHollow],
    ),
    CK64LocationData(
        location_names.CrystalFlippedHollowGassyMoosey, 287,
        region_names.WollowsHollowTrinkets,
        [Rule.MaxPlatforming, Rule.CanReachFlippedHollow],
    ),
    # endregion
    # region Hollow Mirrors
    CK64LocationData(
        location_names.MirrorHollowGraveyard, 289,
        region_names.WollowsHollowAboveGraveyard,
        [Rule.Jump, Rule.Headbutt, Rule.Climb, Rule.Slam],
    ),
    CK64LocationData(
        location_names.MirrorHollowZooSideCrank, 284,
        region_names.WollowsHollow,
        [Rule.CrankZooSide, Rule.MaxPlatforming, Rule.Drill, Rule.Crouch],
    ),
    CK64LocationData(
        location_names.MirrorFlippedHollowDragonCrank, 288,
        region_names.WollowsHollow,
        [Rule.CanReachFlippedHollow, Rule.Jump, Rule.Headbutt, Rule.CrankHollowDragonWall, Rule.Climb],
    ),
    CK64LocationData(
        location_names.MirrorZooMetalWorm, 290,
        region_names.WollowsHollowZoo,
        [Rule.CanUseMetalWorm],
    ),
    # endregion
    # region Hollow Cranks
    CK64LocationData(
        location_names.CrankHollowHauntedHouseGroundFloor, 298,
        region_names.WollowsHollowGraveyard,
        [Rule.Level2, Rule.Jump, Rule.Headbutt],
    ),
    CK64LocationData(
        location_names.CrankHollowRavine, 299,
        region_names.WollowsHollowRavine,
        [Rule.Platforming],
    ),
    # endregion
    # region Disco Balls
    CK64LocationData(
        location_names.DiscoBallHollowTrinketShop, 306,
        region_names.WollowsHollowTrinkets,
        [Rule.MaxPlatforming, Rule.CanReachSpinnyChamber],
    ),
    CK64LocationData(
        location_names.DiscoBallHollowDragonChest, 300,
        region_names.WollowsHollow,
        [Rule.DragonPlatforming, Rule.Headbutt, Rule.Drill],
    ),
    CK64LocationData(
        location_names.DiscoBallHollowMusicBox, 308,
        region_names.WollowsHollowMusic,
        [Rule.MaxPlatforming],
    ),
    CK64LocationData(
        location_names.DiscoBallHollowZombieChamber, 302,
        region_names.WollowsHollowZombies,
        [Rule.CanBeatZombieTurtle, Rule.Jump, Rule.Headbutt],
    ),
    CK64LocationData(
        location_names.DiscoBallHollowCleanZoo, 304,
        region_names.WollowsHollowZoo,
        [Rule.CanCleanZoo],
    ),
    # endregion
    # region Bottlecaps
    CK64LocationData(
        location_names.BottleCapHollowGraveyard, 319,
        region_names.WollowsHollowGraveyard,
        [Rule.MaxPlatforming],
    ),
    CK64LocationData(
        location_names.BottleCapHollowGraveyardInsideWetTree, 317,
        region_names.WollowsHollowGraveyard,
        [Rule.Swim, Rule.Jump, Rule.WallJump, Rule.Climb],
    ),
    CK64LocationData(
        location_names.BottleCapHollowRavineClimb, 311,
        region_names.WollowsHollowRavine,
        [Rule.MaxPlatforming],
    ),
    CK64LocationData(
        location_names.BottleCapHollowZooRooftop, 313,
        region_names.WollowsHollowZooOutside,
        [Rule.DrillDownwards, Rule.Slam, Rule.Climb],
    ),
    CK64LocationData(
        location_names.BottleCapHollowZooSideCrank, 315,
        region_names.WollowsHollow,
        [Rule.CrankZooSide, Rule.Drill],
    ),
    # endregion
    # region Void Screws
    CK64LocationData(
        location_names.VoidScrewParkHouse, 146,
        region_names.MonsterParkHouse,
        [Rule.Jump, Rule.WallJump_Or_Climb, Rule.VerticalHeadbutt],
    ),
    CK64LocationData(
        location_names.VoidScrewHollowOutsideTrinketShop, 324,
        region_names.WollowsHollow,
        [Rule.MaxPlatforming],
    ),
    CK64LocationData(
        location_names.VoidScrewHollowChurch, 321,
        region_names.WollowsHollowChurch,
        [Rule.MaxPlatforming],
    ),
    CK64LocationData(
        location_names.VoidScrewHollowSky, 323,
        region_names.WollowsHollowCagedRooftops,
    ),
    CK64LocationData(
        location_names.VoidScrewSomeOtherPlace, 501,
        region_names.SomeOtherPlace,
    ),
    CK64LocationData(
        location_names.VoidScrewTree, 322,
        region_names.WollowsHollowTree,
        [Rule.MaxPlatforming, Rule.PostOwllohDefeated],
    ),
    CK64LocationData(
        location_names.VoidScrewKillFish, 325,
        region_names.WollowsHollowZombies,
        [Rule.CanKillAllFish],
    ),
    CK64LocationData(
        location_names.VoidScrewParkTopHat, 145,
        region_names.MonsterPark,
        [Rule.MaxPlatforming, Rule.Drill, Rule.Slam],
    ),
    CK64LocationData(
        location_names.VoidScrewParkOutofBounds, 147,
        region_names.MonsterPark,
        [Rule.MaxPlatforming, Rule.DrillDownwards, Rule.CanReachAttic],
    ),
    CK64LocationData(
        location_names.VoidScrewAnxietyTower1, 411,
        region_names.AnxietyTower,
        [Rule.AnxietyTowerChecks, Rule.CrankAnxietyTower, Rule.Slam],
    ),
    CK64LocationData(
        location_names.VoidScrewAnxietyTower2, 412,
        region_names.AnxietyTower,
        [Rule.AnxietyTowerChecks, Rule.CrankAnxietyTower, Rule.Slam, Rule.Crouch],
    ),
    # endregion
    # region Anxiety Tower
    CK64LocationData(
        location_names.CrankAnxietyTower, 414,
        region_names.AnxietyTower,
        [Rule.MaxPlatforming],
    ),
    # endregion
    # region Upgrades
    CK64LocationData(
        location_names.MiracleSoda1, 326,
        region_names.WollowsHollow,
        [Rule.AllBottlecaps],
    ),
    CK64LocationData(
        location_names.MiracleSoda2, 500,
        region_names.SomeOtherPlace,
        [Rule.CanUseVoidScrewsButNotLevel6, Rule.MaxPlatforming],
        progress_type=LocationProgressType.EXCLUDED,
    ),
    CK64LocationData(
        location_names.Drill, 1,
        region_names.WollowsHollowDrillChamber,
        [Rule.Jump, Rule.Climb],
        _type=CornKidzLocationType.UPGRADE,
    ),
    CK64LocationData(
        location_names.FallWarp, 2,
        region_names.WollowsHollowChurch,
        [Rule.MaxPlatforming],
        _type=CornKidzLocationType.UPGRADE,
    ),
    # endregion
    # region Misc Quest
    CK64LocationData(
        location_names.CheeseGrater, 310,
        region_names.WollowsHollowGraveyard,
        [Rule.CanAccessGraveyardBomb, Rule.Slam],
    ),
    CK64LocationData(
        location_names.MetalWorm, 236,
        region_names.WollowsHollowTree,
        [Rule.CanClimbInteriorTree],
        _type=CornKidzLocationType.SWITCH
    ),
    # endregion
    # region Silly
    CK64LocationData(
        location_names.THISGUYWASASICKO, None,
        region_names.WollowsHollowHouseTop,
        [Rule.Jump, Rule.Slam],
        _type=CornKidzLocationType.TEXT,
        text="OH DEAR GOD! THIS GUY WAS A SICKO!!"
    ),
    CK64LocationData(
        location_names.HOWDY, None,
        region_names.WollowsHollowZoo,
        [Rule.CanUseMetalWorm],
        _type=CornKidzLocationType.TEXT,
        text="HOWDY"
    ),
    CK64LocationData(
        location_names.STUPIDDUCK, None,
        region_names.SomeOtherPlace,
        [Rule.CanUseVoidScrewsButNotLevel6, Rule.MaxPlatforming],
        _type=CornKidzLocationType.TEXT,
        text="CAN SOMEBODY TELL ME WHAT THESE STUPID DUCK THINGS EVEN ARE?"
    ),
    CK64LocationData(
        location_names.SYBIL, None,
        region_names.SomeOtherPlace,
        [Rule.CanUseVoidScrewsButNotLevel6, Rule.MaxPlatforming],
        _type=CornKidzLocationType.TEXT,
        text="DANG... WHY COULDN'T I HAVE BEEN TRAPPED IN A REOCCURING DREAM WITH HER INSTEAD OF ALEXIS?"
    ),
    # endregion
    # region Events
    CK64LocationData(
        location_names.DefeatOwlloh, None,
        region_names.WollowsHollowTree,
        [Rule.CanDefeatOwlloh],
        _type=CornKidzLocationType.EVENT
    ),
    CK64LocationData(
        location_names.TowerComplete, None,
        region_names.Tower,
        [Rule.PostOwllohDefeated, Rule.TowerMovement],
        _type=CornKidzLocationType.EVENT
    ),
    CK64LocationData(
        location_names.AnxietyComplete, None,
        region_names.AnxietyTower,
        [Rule.PostOwllohDefeated, Rule.TowerMovement],
        _type=CornKidzLocationType.EVENT
    ),
    CK64LocationData(
        location_names.DogGod, None,
        region_names.SomeOtherPlace,
        [Rule.CanUseAllVoidScrews, Rule.TowerMovement, Rule.Swim],
        _type=CornKidzLocationType.EVENT
    ),
    # endregion
    # region Achievements
    CK64LocationData(
        location_names.Achievement_LittleCornCadet, 1,
        region_names.MonsterParkTop,
        _type=CornKidzLocationType.ACHIEVEMENT,
    ),
    CK64LocationData(
        location_names.Achievement_XPansionPak, 2,
        region_names.Menu,
        [Rule.Level2],
        _type=CornKidzLocationType.ACHIEVEMENT,
    ),
    CK64LocationData(
        location_names.Achievement_MaxPower, 3,
        region_names.Menu,
        [Rule.Level6],
        _type=CornKidzLocationType.ACHIEVEMENT,
    ),
    CK64LocationData(
        location_names.Achievement_ImALasagnaHog, 4,
        region_names.WollowsHollow,
        [Rule.PostOwllohDefeated],
        _type=CornKidzLocationType.ACHIEVEMENT,
    ),
    CK64LocationData(
        location_names.Achievement_GetNachosOrGetOut, 5,
        region_names.Tower,
        [Rule.TowerMovement],
        _type=CornKidzLocationType.ACHIEVEMENT,
    ),
    CK64LocationData(
        location_names.Achievement_AnxietyAttack, 6,
        region_names.AnxietyTower,
        [Rule.AnxietyTowerChecks, Rule.CrankAnxietyTower, Rule.TowerMovement],
        _type=CornKidzLocationType.ACHIEVEMENT,
    ),
    CK64LocationData(
        location_names.Achievement_PrivateScrew, 7,
        region_names.Menu,
        [Rule.AnyVoidScrew],
        _type=CornKidzLocationType.ACHIEVEMENT,
    ),
    CK64LocationData(
        location_names.Achievement_AnnoyedTheVoid, 8,
        region_names.SomeOtherPlace,
        [Rule.CanUseVoidScrewsButNotLevel6],  # ToDo: probably wrong
        _type=CornKidzLocationType.ACHIEVEMENT,
    ),
    CK64LocationData(
        location_names.Achievement_HighBreadHeaven, 9,
        region_names.SomeOtherPlace,
        [Rule.CanUseAllVoidScrews, Rule.TowerMovement, Rule.Swim],
        _type=CornKidzLocationType.ACHIEVEMENT,
    ),
    CK64LocationData(
        location_names.Achievement_SmokingKills, 10,
        region_names.MonsterPark,
        [Rule.BreakGroundedObject, Rule.Jump, Rule.WallJump_Or_Climb],
        _type=CornKidzLocationType.ACHIEVEMENT,
    ),
    CK64LocationData(
        location_names.Achievement_MagicalTetnisChallenge, 11,
        region_names.MonsterPark,
        [Rule.DrillDownwards],
        _type=CornKidzLocationType.ACHIEVEMENT,
    ),
    CK64LocationData(
        location_names.Achievement_CornSyrup, 12,
        region_names.Menu,
        [Rule.AnyHPItem],
        _type=CornKidzLocationType.ACHIEVEMENT,
    ),
    CK64LocationData(
        location_names.Achievement_FeastFitForAKid, 13,
        region_names.AnxietyTower,
        [Rule.Jump, Rule.Headbutt],
        _type=CornKidzLocationType.ACHIEVEMENT,
    ),
    CK64LocationData(
        location_names.Achievement_HeroesInAWholeShell, 14,
        region_names.WollowsHollow,
        [Rule.Jump, Rule.Headbutt, Rule.BombBird],
        _type=CornKidzLocationType.ACHIEVEMENT,
    ),
    CK64LocationData(
        location_names.Achievement_Highdive, 15,
        region_names.WollowsHollowTree,
        [Rule.CanClimbInteriorTree],
        _type=CornKidzLocationType.ACHIEVEMENT,
    ),
    # endregion
    # region Rats
    CK64LocationData(
        location_names.Rat1, 1,
        region_names.WollowsHollowZoo,
        [Rule.Punch, Rule.Jump, Rule.WallJump_Or_Climb],
        _type=CornKidzLocationType.RAT,
    ),
    CK64LocationData(
        location_names.Rat2, 2,
        region_names.WollowsHollowZoo,
        [Rule.Punch, Rule.MaxPlatforming],
        _type=CornKidzLocationType.RAT,
    ),
    CK64LocationData(
        location_names.Rat3, 3,
        region_names.WollowsHollowZoo,
        [Rule.Punch, Rule.MaxPlatforming],
        _type=CornKidzLocationType.RAT,
    ),
    CK64LocationData(
        location_names.Rat4, 4,
        region_names.WollowsHollowZoo,
        [Rule.Punch, Rule.Drill, Rule.MaxPlatforming],
        _type=CornKidzLocationType.RAT,
    ),
    CK64LocationData(
        location_names.Rat5, 5,
        region_names.WollowsHollowZoo,
        [Rule.Punch, Rule.Drill, Rule.MaxPlatforming],
        _type=CornKidzLocationType.RAT,
    ),
    CK64LocationData(
        location_names.Rat6, 6,
        region_names.WollowsHollowZoo,
        [Rule.Punch, Rule.Drill, Rule.MaxPlatforming],
        _type=CornKidzLocationType.RAT,
    ),
    # endregion
    # region Fish
    CK64LocationData(
        location_names.Fish1, 238,
        region_names.WollowsHollowGraveyard,
        [Rule.CanAccessGraveyardBomb],
        _type=CornKidzLocationType.SWITCH,
    ),
    CK64LocationData(
        location_names.Fish2, 239,
        region_names.WollowsHollowTree,
        [Rule.CanClimbInteriorTree],
        _type=CornKidzLocationType.SWITCH,
    ),
    CK64LocationData(
        location_names.Fish3, 240,
        region_names.WollowsHollowTree,
        [Rule.CanClimbInteriorTree],
        _type=CornKidzLocationType.SWITCH,
    ),
    # endregion
    # region Outfits
    CK64LocationData(
        location_names.BlueHeadband, None,
        region_names.SomeOtherPlace,
        [Rule.CanUseVoidScrewsButNotLevel6, Rule.MaxPlatforming],
        _type=CornKidzLocationType.TEXT,
        text="WEAR BLUE HEADBAND + SHIRT?"

    ),
    CK64LocationData(
        location_names.GreenHeadband, None,
        region_names.SomeOtherPlace,
        [Rule.CanUseVoidScrewsButNotLevel6, Rule.MaxPlatforming],
        _type=CornKidzLocationType.TEXT,
        text="WEAR GREEN HEADBAND + SHIRT?"
    ),
    CK64LocationData(
        location_names.BlackHeadband, None,
        region_names.AnxietyTower,
        [Rule.MaxPlatforming],
        _type=CornKidzLocationType.TEXT,
        text="WEAR BLACK HEADBAND + SHIRT?"
    ),
    # endregion
]

locked_locations = [
    location_names.DefeatOwlloh,
    location_names.TowerComplete,
    location_names.AnxietyComplete,
    location_names.DogGod,
]

goal_locations = {
    Goal.option_owlloh: location_names.DefeatOwlloh,
    Goal.option_tower: location_names.TowerComplete,
    Goal.option_anxiety: location_names.AnxietyComplete,
    Goal.option_god: location_names.DogGod,
}

achievement_locations = [
    location_names.Achievement_LittleCornCadet,
    location_names.Achievement_XPansionPak,
    location_names.Achievement_ImALasagnaHog,
    location_names.Achievement_CornSyrup,
    location_names.Achievement_GetNachosOrGetOut,
    location_names.Achievement_Highdive,
    location_names.Achievement_PrivateScrew,
    location_names.Achievement_SmokingKills,
    location_names.Achievement_MagicalTetnisChallenge,
    location_names.Achievement_HeroesInAWholeShell,
    location_names.Achievement_AnxietyAttack,
    location_names.Achievement_AnnoyedTheVoid,
    location_names.Achievement_MaxPower,
    location_names.Achievement_FeastFitForAKid,
]

crank_locations = [
    location_names.CrankMonsterParkAcrossLake,
    location_names.CrankHollowHauntedHouseGroundFloor,
    location_names.CrankHollowRavine,
    location_names.CrankAnxietyTower
]

rat_locations = [
    location_names.Rat1,
    location_names.Rat2,
    location_names.Rat3,
    location_names.Rat4,
    location_names.Rat5,
    location_names.Rat6,
]

fish_locations = [
    location_names.Fish1,
    location_names.Fish2,
    location_names.Fish3,
]

lookup_id_to_name: typing.Dict[int, str] = {BaseId + i: data.name for i, data in enumerate(location_table)}
lookup_name_to_id: typing.Dict[str, int] = {v: k for k, v in lookup_id_to_name.items()}
