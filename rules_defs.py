from enum import Enum, auto

class CK64Rule(Enum):
    Level2 = auto()
    Level3 = auto()
    Level4 = auto()
    Level5 = auto()
    Level6 = auto()

    AllBottlecaps = auto()
    AllTrashcans = auto()
    AllDiscoBalls = auto()
    CheeseGrater = auto()
    AllTombstones = auto()

    CanUseVoidScrewsButNotLevel6 = auto()
    CanUseAllVoidScrews = auto()
    AnyVoidScrew = auto()
    AnyHPItem = auto()

    Jump = auto()
    Punch = auto()
    Climb = auto()
    Slam = auto()
    Headbutt = auto()
    WallJump = auto()
    Swim = auto()
    Crouch = auto()
    Drill = auto()
    FallWarp = auto()

    TowerMovement = auto()  # everything except fall warp and swim

    WallJump_Or_Climb = auto()
    Jump_Or_Headbutt = auto()
    WallButton = auto()  # Jump & Headbutt
    HighClimb = auto()   # Jump & Climb
    Climb_Or_Headbutt = auto()
    WallJump_Or_Headbutt = auto()
    WallJump_Or_Slam = auto()
    Platforming = auto()  # Jump, Walljump, Climb
    MaxPlatforming = auto()  # Jump, Walljump, Climb, Headbutt
    BreakGroundedObject = auto()  # Headbutt and (Jump or Crouch)
    VerticalHeadbutt = auto()  # Crouch and Headbutt
    BreakCrystal = auto()  # Jump and Headbutt
    BreakTrashcan = auto()  # Punch or (Jump + Headbutt) or (Crouch + Headbutt) or Slam
    BombBird = auto()  # Same as BreakGroundedObject
    OpenChest = auto()  # Same as WallButton
    Chameleon = auto()  # Jump and Headbutt
    DrillDownwards = auto()  # Jump and Slam and Drill
    DrillWall = auto()  # Jump, Headbutt and Drill
    DrillMinimal = auto()  # Drill and (Headbutt or Slam)
    CanBeatZombieTurtle = auto()  # BreakGroundedObject, Punch, Slam
    CanGetHurt = auto()  # Has at least 2 max HP

    DragonPlatforming = auto()  # CrankHollowDragonWall, Jump, WallJump, Headbutt
    CanFreeHauntedHouseBird = auto()  # WollowsHollowHouseTop, Jump+Slam, CanBeatZombieTurtle
    CanUseMetalWorm = auto()  # CanClimbInteriorTree, (CanCleanZoo or CanGetHurt), Jump, Headbutt

    CanReachAttic = auto()  # (Platforming and VerticalHeadbutt) or (CanReachParkTop, Jump, Headbutt, Climb)
    CanReachParkTop = auto()  # MonsterParkTop
    CanReachRooftops = auto()  # Rooftops
    CanReachCagedRooftops = auto()
    CanReachGraveyard = auto()
    CanReachGraveyardTop = auto()
    CanReachSpinnyChamber = auto() # WollowsHollowDrillChamber, Slam, Drill
    CanReachFlippedHollow = auto() # CanReachSpinnyChamber, 5 disco balls
    CanEnterFountain = auto()  # CanReachFlippedHollow, jump, headbutt, climb or walljump, swim
    CanClimbInteriorTree = auto()  # WollowsHollowTree, MaxPlatforming, slam, drill

    BatTreeSideRoom = auto()  # CanReachFlippedHollow, CrankZooSide, jump, drill, headbutt, walljump
    BatTreeSideRoomCollectables = auto()  # (slam or walljump) and headbutt

    CrankMonsterPark = auto()
    CrankHollowDragonWall = auto()
    CrankZooSide = auto()  # SaveTrigger 229 when placed

    CanKillAllFish = auto() # CanClimbInteriorTree and CanAccessGraveyardBomb or Fishsantiy and has 3 Fish
    CanCleanZoo = auto()  # WollowsHollowZoo, ((max platforming, drill, punch) or ratsanity)
    CanDefeatOwlloh = auto()  # CanClimbInteriorTree, Level 4

    AnxietyTowerChecks = auto()  # PostOwllohDefeated, Level 5, MaxPlatforming

    PostOwllohDefeated = auto()  # Has DefeatOwlloh
    CanAccessGraveyardBomb = auto()  # CanReachGraveyard, Swim, BombBird, Platforming

