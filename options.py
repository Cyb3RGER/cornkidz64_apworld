from dataclasses import dataclass

from Options import Range, Toggle, DefaultOnToggle, PerGameCommonOptions, OptionGroup, DeathLinkMixin, \
    StartInventoryPool, OptionSet
from .constants import goal_owlloh, goal_tower, goal_anxiety, goal_god


class GoalSelection(OptionSet):
    """Select which goal(s) you need to reach to finish the game.

    Possible values are:
    - **Defeat Owlloh**
    - **Climb the Tower**
    - **Climb the Anxiety Tower**
    - **Meet the Dog God**
    """
    display_name = "Goal Selection"
    valid_keys = [
        goal_owlloh,
        goal_tower,
        goal_anxiety,
        goal_god
    ]
    default = frozenset({goal_owlloh, goal_tower})


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


class Switchsanity(Toggle):
    """Adds the 4 cube switches in Some Other Place into the location pool."""
    display_name = "Switchsanity"

class TestCubesanity(Toggle):
    """Adds the 25 cubes in the Test Zone into the location pool."""
    display_name = "Test Cubesanity"

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
    - Slam
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
    goal_selection: GoalSelection
    xp_count: XPCount
    xp_item_count: XPItemCount
    # max_hp: MaxHP
    cranksanity: Cranksanity
    ratsanity: Ratsanity
    fishsanity: Fishsanity
    achievementsanity: Achievementsanity
    switchsanity: Switchsanity
    test_cubesanity: TestCubesanity
    trap_percentage: TrapPercentage
    movesanity: Movesanity
    open_wollows_hollow: OpenWollowsHollow


corn_kidz_option_groups: list[OptionGroup] = [
    OptionGroup(
        name="Base Options",
        options=[
            GoalSelection,
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
            Movesanity,
            Switchsanity,
            TestCubesanity
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
