from dataclasses import dataclass

from Options import Choice, Range, Toggle, DefaultOnToggle, PerGameCommonOptions, OptionGroup, DeathLinkMixin, \
    StartInventoryPool


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


class Movesanity(Toggle):
    """
    Adds the following player moves to the item pool:
    - Punch
    - Climb
    - Ground Pound
    - Headbutt
    - Wall Jump
    - Crouch
    NOTE: This has as high failure rate for worlds with only few filler items or single worlds. Try regenerating or turning on Open Wollow's Hollow to help with these failures.
    """
    display_name  = "Movesanity"


class OpenWollowsHollow(Toggle):
    """
    Makes Wollow's Hollow accessible from the beginning without any moves needed.
    """
    display_name = "Open Wollow's Hollow"


@dataclass
class CornKidz64Options(PerGameCommonOptions, DeathLinkMixin):
    start_inventory_from_pool: StartInventoryPool
    goal: Goal
    xp_count: XPCount
    xp_item_count: XPItemCount
    # max_hp: MaxHP
    cranksanity: Cranksanity
    ratsanity: Ratsanity
    fishsanity: Fishsanity
    achievementsanity: Achievementsanity
    trap_percentage: TrapPercentage
    movesanity: Movesanity
    open_wollows_hollow: OpenWollowsHollow


corn_kidz_option_groups: list[OptionGroup] = [
    OptionGroup(
        name="Base Options",
        options=[
            Goal,
            OpenWollowsHollow,
            # MaxHP,
            TrapPercentage
        ]
    ),
    OptionGroup(
        name="Randomization Options",
        options=[
            Cranksanity,
            Ratsanity,
            Fishsanity,
            Achievementsanity,
            Movesanity
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
