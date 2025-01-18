from dataclasses import dataclass

from Options import Choice, Range, Toggle, DefaultOnToggle, PerGameCommonOptions, OptionGroup, DeathLinkMixin


class Goal(Choice):
    """The clear condition to finish the game."""
    display_name = "Goal"
    option_owlloh = 0
    option_tower = 1
    option_anxiety = 2
    option_god = 3
    default = 1


class XPCount(Range):
    """The total amount of XP in the item pool."""
    display_name = "XP Count"
    range_start = 200
    range_end = 500
    default = 360


class XPItemCount(Range):
    """The amount of XP items in the item pool. Use this to make more space for junk (filler/trap) items."""
    display_name = "XP Item Count"
    range_start = 52
    range_end = 134
    default = 134


class MaxHP(Range):
    """Seve's starting max HP.
    Adds max HP items into the item pool."""
    # ToDo: implement
    display_name = "Max HP"
    range_start = 1
    range_end = 8
    default = 8


class Cranksanity(DefaultOnToggle):
    """Randomizes the locations where cranks can be found."""
    display_name = "Cranksanity"


class Ratsanity(Toggle):
    """Adds the Sanitary Zoo rats into the item and location pool.
    Collecting them all is required for the zoo to be clean."""
    display_name = "Ratsanity"


class Fishsanity(Toggle):
    """Adds the purple Fish into the item and location pool.
    Collecting them all is required for the Void Screw in the Zombie Chamber."""
    display_name = "Fishsanity"


class Achievementsanity(Toggle):
    """Adds achievements into the location pool."""
    display_name = "Achievementsanity"


class TrapPercentage(Range):
    """Determines the number of trap items when populating the item pool with filler."""
    display_name = "Trap Percentage"
    range_start = 0
    range_end = 100
    default = 25


class CanJump(DefaultOnToggle):
    """Determines if Seve can jump by default."""
    display_name = "can_jump"


class CanPunch(DefaultOnToggle):
    """Determines if Seve can punch by default."""
    display_name = "can_punch"


class CanClimb(DefaultOnToggle):
    """Determines if Seve can climb ledges or pipes by default."""
    display_name = "can_climb"


class CanGroundPound(DefaultOnToggle):
    """Determines if Seve can ground pound by default."""
    display_name = "can_ground_pound"


class CanHeadbutt(DefaultOnToggle):
    """Determines if Seve can headbutt by default."""
    display_name = "can_headbutt"


class CanWallJump(DefaultOnToggle):
    """Determines if Seve can wall jump by default."""
    display_name = "can_wall_jump"


class CanSwim(DefaultOnToggle):
    """Determines if Seve can swim underwater by default."""
    display_name = "can_swim"


class CanCrouch(DefaultOnToggle):
    """Determines if Seve can crouch by default."""
    display_name = "can_crouch"


class OpenMode(Toggle):
    # ToDo: implement
    """Determines if all levels should be open form the start"""
    display_name = "Open Mode"


@dataclass
class CornKidz64Options(PerGameCommonOptions, DeathLinkMixin):
    goal: Goal
    xp_count: XPCount
    xp_item_count: XPItemCount
    # max_hp: MaxHP
    cranksanity: Cranksanity
    ratsanity: Ratsanity
    fishsanity: Fishsanity
    achievementsanity: Achievementsanity
    trap_percentage: TrapPercentage
    # ToDo: probably just make a move rando option?
    # can_jump: CanJump
    # can_punch: CanPunch
    # can_climb: CanClimb
    # can_ground_pound: CanGroundPound
    # can_headbutt: CanHeadbutt
    # can_wall_jump: CanWallJump
    # can_swim: CanSwim
    # can_crouch: CanCrouch
    # open_mode: OpenMode


corn_kidz_option_groups: list[OptionGroup] = [
    OptionGroup(
        name="Base Options",
        options=[
            Goal,
            # OpenMode,
            TrapPercentage]
    ),
    OptionGroup(
        name="Randomization Options",
        options=[
            Cranksanity,
            Ratsanity,
            Fishsanity,
            Achievementsanity,
            # Movesanity
        ],
    ),
    OptionGroup(
        name="XP Options",
        options=[
            XPCount,
            XPItemCount
        ],
    ),
]
