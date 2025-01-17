from typing import Callable, Dict

from BaseClasses import MultiWorld, CollectionState
from .options import CornKidz64Options
from .rules_defs import CK64Rule
from .constants import item_names, region_names

rules_to_func: Dict[CK64Rule, Callable] = {}


def rule(rule: CK64Rule):
    def decorator(f):
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)

        rules_to_func[rule] = f
        return wrapper

    return decorator


"""
Rule definitions
"""


def get_xp_count(state: CollectionState, player: int, options: CornKidz64Options) -> int:
    return state.count(item_names.XPCube, player) + \
        state.count(item_names.RedScrew, player) * 3 + \
        state.count(item_names.Moth, player) * 5 + \
        state.count(item_names.XPCrystal, player) * 10


# def get_xp_count(state: CollectionState, player: int, options: CornKidz64Options) -> int:
#     total_xp = 360
#     curr_xp = math.floor((total_xp / options.xp_count) * state.count(Item.XP.value, player))
#     return curr_xp


@rule(CK64Rule.Level2)
def Level2(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return get_xp_count(state, player, options) >= 70


@rule(CK64Rule.Level3)
def Level3(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return get_xp_count(state, player, options) >= 140


@rule(CK64Rule.Level4)
def Level4(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return get_xp_count(state, player, options) >= 200


@rule(CK64Rule.Level5)
def Level5(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return get_xp_count(state, player, options) >= 300


@rule(CK64Rule.Level6)
def Level6(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return get_xp_count(state, player, options) >= 360


@rule(CK64Rule.AllBottlecaps)
def AllBottlecaps(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return state.has(item_names.BottleCap, player, 5)


@rule(CK64Rule.AllTrashcans)
def AllTrashcans(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return state.has(item_names.TrashCan, player, 8)


@rule(CK64Rule.AllDiscoBalls)
def AllDiscoBalls(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return state.has(item_names.DiscoBall, player, 5)


@rule(CK64Rule.CheeseGrater)
def CheeseGrater(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return state.has(item_names.CheeseGrater, player)


@rule(CK64Rule.AllTombstones)
def AllTombstones(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return state.can_reach(region_names.WollowsHollowGraveyard, None, player) and \
        BreakGroundedObject(state, world, player, options)


@rule(CK64Rule.CanUseVoidScrewsButNotLevel6)
def CanUseFourVoidScrews(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    # technically you can only waste 10, if you're not level 6, but that would require looking level 6 behind the 11th Void Screw
    return state.has(item_names.VoidScrew, player, 11)


@rule(CK64Rule.CanUseAllVoidScrews)
def CanUseAllVoidScrews(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return state.has(item_names.VoidScrew, player, 11) and Level6(state, world, player, options)


@rule(CK64Rule.AnyVoidScrew)
def AnyVoidScrew(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return state.has(item_names.VoidScrew, player)


@rule(CK64Rule.AnyHPItem)
def AnyHPItem(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return state.has(item_names.MegaDreamSoda, player)

# ToDo: implement movement rando
@rule(CK64Rule.Jump)
def Jump(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    #return state.has(item_names.Jump, player) or options.can_jump
    return True


@rule(CK64Rule.Punch)
def Punch(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    #return state.has(item_names.Punch, player) or options.can_punch
    return True


@rule(CK64Rule.Climb)
def Climb(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    #return state.has(item_names.Climb, player) or options.can_climb
    return True


@rule(CK64Rule.Slam)
def Slam(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    #return state.has(item_names.Slam, player) or options.can_ground_pound
    return True


@rule(CK64Rule.Headbutt)
def Headbutt(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    #return state.has(item_names.Headbutt, player) or options.can_headbutt
    return True


@rule(CK64Rule.WallJump)
def WallJump(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    #return state.has(item_names.WallJump, player) or options.can_wall_jump
    return True


@rule(CK64Rule.Swim)
def Swim(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    #return state.has(item_names.Swim, player) or options.can_swim
    return True


@rule(CK64Rule.Crouch)
def Crouch(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    #return state.has(item_names.Crouch, player) or options.can_crouch
    return True


@rule(CK64Rule.Drill)
def Drill(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return state.has(item_names.Drill, player) #or options.can_drill


@rule(CK64Rule.FallWarp)
def FallWarp(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return state.has(item_names.FallWarp, player) #or options.can_fall_warp


@rule(CK64Rule.TowerMovement)
def TowerMovement(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return Jump(state, world, player, options) and \
        Punch(state, world, player, options) and \
        Climb(state, world, player, options) and \
        Slam(state, world, player, options) and \
        Headbutt(state, world, player, options) and \
        WallJump(state, world, player, options) and \
        Crouch(state, world, player, options) and \
        Drill(state, world, player, options)


@rule(CK64Rule.WallJump_Or_Climb)
def WallJump_Or_Climb(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return WallJump(state, world, player, options) or \
        Climb(state, world, player, options)


@rule(CK64Rule.Jump_Or_Headbutt)
def Jump_Or_Headbutt(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return Jump(state, world, player, options) or \
        Headbutt(state, world, player, options)


@rule(CK64Rule.WallButton)
def WallButton(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return Jump(state, world, player, options) and \
        Headbutt(state, world, player, options)


@rule(CK64Rule.HighClimb)
def HighClimb(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return Jump(state, world, player, options) and \
        Climb(state, world, player, options)


@rule(CK64Rule.Climb_Or_Headbutt)
def Climb_Or_Headbutt(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return Climb(state, world, player, options) or \
        Headbutt(state, world, player, options)


@rule(CK64Rule.WallJump_Or_Headbutt)
def WallJump_Or_Headbutt(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return WallJump(state, world, player, options) or \
        Headbutt(state, world, player, options)


@rule(CK64Rule.WallJump_Or_Slam)
def WallJump_Or_Slam(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return WallJump(state, world, player, options) or \
        Slam(state, world, player, options)


@rule(CK64Rule.Platforming)
def Platforming(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return Jump(state, world, player, options) and \
        WallJump(state, world, player, options) and \
        Climb(state, world, player, options)


@rule(CK64Rule.MaxPlatforming)
def MaxPlatforming(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return Platforming(state, world, player, options) and \
        Headbutt(state, world, player, options)


@rule(CK64Rule.BreakGroundedObject)
def BreakGroundedObject(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return Headbutt(state, world, player, options) and \
        (Jump(state, world, player, options) or
         Crouch(state, world, player, options))


@rule(CK64Rule.VerticalHeadbutt)
def VerticalHeadbutt(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return Crouch(state, world, player, options) and \
        Headbutt(state, world, player, options)


@rule(CK64Rule.BreakCrystal)
def BreakCrystal(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return Jump(state, world, player, options) and \
        Headbutt(state, world, player, options)


@rule(CK64Rule.BreakTrashcan)
def BreakTrashcan(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return Punch(state, world, player, options) or \
        (Jump(state, world, player, options) and Headbutt(state, world, player, options)) or \
        (Crouch(state, world, player, options) and Headbutt(state, world, player, options)) or \
        (Jump(state, world, player, options) and Slam(state, world, player, options))


@rule(CK64Rule.BombBird)
def BombBird(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return BreakGroundedObject(state, world, player, options)


@rule(CK64Rule.OpenChest)
def OpenChest(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return Jump(state, world, player, options) and \
        Headbutt(state, world, player, options)


@rule(CK64Rule.Chameleon)
def Chameleon(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return Jump(state, world, player, options) and \
        Headbutt(state, world, player, options)


@rule(CK64Rule.DrillDownwards)
def DrillDownwards(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return Jump(state, world, player, options) and \
        Slam(state, world, player, options) and \
        Drill(state, world, player, options)


@rule(CK64Rule.DrillWall)
def DrillWall(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return Jump(state, world, player, options) and \
        Headbutt(state, world, player, options) and \
        Drill(state, world, player, options)


@rule(CK64Rule.DrillMinimal)
def DrillMinimal(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return Drill(state, world, player, options) and \
        (Headbutt(state, world, player, options) or
         Slam(state, world, player, options))


@rule(CK64Rule.CanBeatZombieTurtle)
def CanBeatZombieTurtle(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return BreakGroundedObject(state, world, player, options) and \
        Punch(state, world, player, options) and \
        Slam(state, world, player, options)


@rule(CK64Rule.CanGetHurt)
def CanGetHurt(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    # ToDo: this might need a better rule
    # if options.max_hp > 1:
    #     return True
    # return state.has(item_names.MegaDreamSoda, player)
    return True


@rule(CK64Rule.DragonPlatforming)
def DragonPlatforming(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return CrankHollowDragonWall(state, world, player, options) and \
        Jump(state, world, player, options) and \
        WallJump(state, world, player, options) and \
        Headbutt(state, world, player, options)


@rule(CK64Rule.CanFreeHauntedHouseBird)
def CanFreeHauntedHouseBird(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return state.can_reach(region_names.WollowsHollowHouseTop, None, player) and \
        Jump(state, world, player, options) and \
        Slam(state, world, player, options) and \
        CanBeatZombieTurtle(state, world, player, options)


@rule(CK64Rule.CanUseMetalWorm)
def CanUseMetalWorm(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return state.has(item_names.MetalWorm, player) and \
        (CanCleanZoo(state, world, player, options) or CanGetHurt(state, world, player, options)) and \
        Jump(state, world, player, options) and \
        Headbutt(state, world, player, options)


@rule(CK64Rule.CanReachAttic)
def CanReachAttic(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return (Platforming(state, world, player, options) and VerticalHeadbutt(state, world, player, options)) or \
        (CanReachParkTop(state, world, player, options) and Jump(state, world, player, options) and
         Climb(state, world, player, options) and Headbutt(state, world, player, options))


@rule(CK64Rule.CanReachParkTop)
def CanReachParkTop(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return state.can_reach(region_names.MonsterParkTop, None, player)


@rule(CK64Rule.CanReachRooftops)
def CanReachRooftops(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return state.can_reach(region_names.WollowsHollowRooftops, None, player)


@rule(CK64Rule.CanReachCagedRooftops)
def CanReachCagedRooftops(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return state.can_reach(region_names.WollowsHollowCagedRooftops, None, player)


@rule(CK64Rule.CanReachGraveyard)
def CanReachGraveyard(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return state.can_reach(region_names.WollowsHollowGraveyard, None, player)


@rule(CK64Rule.CanReachGraveyardTop)
def CanReachGraveyardTop(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return state.can_reach(region_names.WollowsHollowAboveGraveyard, None, player)


@rule(CK64Rule.CanReachFlippedHollow)
def CanReachFlippedHollow(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return state.can_reach(region_names.WollowsHollowDrillChamber, None, player) and \
        Slam(state, world, player, options) and \
        Drill(state, world, player, options) and \
        AllDiscoBalls(state, world, player, options)


@rule(CK64Rule.CanEnterFountain)
def CanEnterFountain(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return CanReachFlippedHollow(state, world, player, options) and \
        Jump(state, world, player, options) and \
        Headbutt(state, world, player, options) and \
        (Climb(state, world, player, options) or WallJump(state, world, player, options)) and \
        Swim(state, world, player, options)


@rule(CK64Rule.CanClimbInteriorTree)
def CanClimbInteriorTree(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return state.can_reach(region_names.WollowsHollowTree, None, player) and \
        MaxPlatforming(state, world, player, options) and \
        Slam(state, world, player, options) and \
        Drill(state, world, player, options)


@rule(CK64Rule.BatTreeSideRoom)
def BatTreeSideRoom(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return CanReachFlippedHollow(state, world, player, options) and \
        CrankZooSide(state,world,player,options) and \
        Jump(state, world, player, options) and \
        Drill(state, world, player, options) and \
        Headbutt(state, world, player, options) and \
        WallJump(state, world, player, options)


@rule(CK64Rule.BatTreeSideRoomCollectables)
def BatTreeSideRoomCollectables(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return state.can_reach(region_names.WollowsHollowTreeSideRoom, None, player) and \
        (Slam(state, world, player, options) or
         WallJump(state, world, player, options)) and \
        Headbutt(state, world, player, options)


@rule(CK64Rule.CrankMonsterPark)
def CrankMonsterPark(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return not options.cranksanity or state.has(item_names.CrankMonsterPark, player)


@rule(CK64Rule.CrankHollowDragonWall)
def CrankHollowDragonWall(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return not options.cranksanity or state.has(item_names.CrankHollowElevator, player)


@rule(CK64Rule.CrankZooSide)
def CrankZooSide(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return not options.cranksanity or state.has(item_names.CrankHollowZooWall, player)


@rule(CK64Rule.CanCleanZoo)
def CanCleanZoo(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    if options.ratsanity:
        return state.can_reach(region_names.WollowsHollowZoo, None, player) and \
            state.has(item_names.Rat, player, 6)
    else:
        return state.can_reach(region_names.WollowsHollowZoo, None, player) and \
            MaxPlatforming(state, world, player, options) and \
            Drill(state, world, player, options) and \
            Punch(state, world, player, options)

@rule(CK64Rule.CanKillAllFish)
def CanKillAllFish(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    if options.fishsanity:
        return state.has(item_names.Fish, player, 3)
    else:
        return CanClimbInteriorTree(state, world, player, options) and CanAccessGraveyardBomb(state, world, player, options)


@rule(CK64Rule.CanDefeatOwlloh)
def CanDefeatOwlloh(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return CanClimbInteriorTree(state, world, player, options) and \
        Level4(state, world, player, options)


@rule(CK64Rule.AnxietyTowerChecks)
def AnxietyTowerChecks(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return PostOwllohDefeated(state, world, player, options) and \
        Level5(state, world, player, options) and \
        TowerMovement(state, world, player, options)


@rule(CK64Rule.PostOwllohDefeated)
def PostOwllohDefeated(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return CanDefeatOwlloh(state, world, player, options)


@rule(CK64Rule.CanAccessGraveyardBomb)
def CanAccessGraveyardBomb(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options):
    return CanReachGraveyard(state, world, player, options) and \
        Swim(state, world, player, options) and \
        BombBird(state, world, player, options) and \
        Platforming(state, world, player, options)
