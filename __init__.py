# Special Thanks to mica/thejanjan for providing a **huge** chunk of the apworld.
import logging
from dataclasses import field
from typing import TextIO

from BaseClasses import Item, Tutorial, ItemClassification, Region, MultiWorld, CollectionState
from Options import Accessibility
from worlds.AutoWorld import World, WebWorld
from .items import item_table, CornKidzItem, lookup_name_to_id as item_name_to_id, get_trap_item_names, get_filler_item_names
from .locations import location_table, CK64LocationData, lookup_name_to_id as loc_name_to_id, achievement_locations, CornKidzLocation, goal_locations, locked_locations, rat_locations, crank_locations, CornKidzLocationType, fish_locations
from .options import CornKidz64Options, Goal, corn_kidz_option_groups
from .regions import region_table, CK64EntranceData, CK64RegionData
from .rules import rules_to_func
from .constants import item_names, GameName, region_names, BaseId, xp_name_to_value, xp_value_to_name

ck64_version = (0, 0, 5)

logger = logging.getLogger("Corn Kidz 64")

class CornKidzWeb(WebWorld):
    theme = "partyTime"
    option_groups = corn_kidz_option_groups
    rich_text_options_doc = True
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Corn Kidz 64 integration for Archipelago multiworld games.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Cyb3R"]
    )]


class CornKidz(World):
    """
    Corn Kidz 64
    The unique aura of bygone 64-bit worlds resurrected in this
    "pilot episode" 3D platformer roughly 1/3rd the size of the classics.
    """
    game = GameName
    options_dataclass = CornKidz64Options
    options: CornKidz64Options
    topology_present = True

    item_name_to_id = item_name_to_id
    location_name_to_id = loc_name_to_id

    web = CornKidzWeb()

    goal_name = "Defeat Owlloh"
    excluded_locations = field(default_factory=list)
    is_first_mega_soda = True
    ut_can_gen_without_yaml = True

    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)
        self.xp_counter = 0
        self.xp_required = 360


    def generate_early(self) -> None:
        if hasattr(self.multiworld, "re_gen_passthrough"):
            if GameName in self.multiworld.re_gen_passthrough:
                self.apply_options_from_slot_data(self.multiworld.re_gen_passthrough[GameName])

        if self.options.accessibility == self.options.accessibility.option_minimal:
            self.xp_required = 200
            if self.options.goal == Goal.option_anxiety:
                self.xp_required = 300
            elif self.options.goal == Goal.option_god:
                self.xp_required = 360
        if (self.options.goal == Goal.option_god or self.options.accessibility == Accessibility.option_full) and self.options.xp_count < 360:
            logger.warning(f"[Corn Kidz 64 - {self.multiworld.get_player_name(self.player)}] forcing xp count to 360 because it's required either by goal or accessibility")
            self.options.xp_count.value = 360
        elif self.options.goal == Goal.option_anxiety and self.options.xp_count < 300:
            logger.warning(f"[Corn Kidz 64 - {self.multiworld.get_player_name(self.player)}] forcing xp count to 300 because it's required by goal")
            self.options.xp_count.value = 300

    def create_filler(self) -> "Item":
        return self.create_item(self.random.choice(get_filler_item_names()))

    def get_filler_item_name(self) -> str:
        return self.random.choice(get_filler_item_names())

    def get_xp_items(self):
        current_counts = {k: 0 for k in xp_value_to_name.keys()}
        diff = self.options.xp_count
        # fill the "biggest" items first (fewest items possible for this xp count)
        for v in sorted(xp_value_to_name.keys(), reverse=True):
            while diff >= v:
                current_counts[v] += 1
                diff -= v

        #logger.debug(f"min item fill: {current_counts}")

        current_item_count = sum(current_counts.values())
        diff = self.options.xp_item_count - current_item_count
        # as long as we still need more location, split the current items apart
        while diff > 0:
            made_change = False
            # smallest first (lowest quantity)
            for v in [3,5,10]:
                if diff == 0:
                    break
                if v == 10 and current_counts[10] > 0 and diff >= 3:
                    current_counts[10] -= 1
                    current_counts[3] += 3
                    current_counts[1] += 1
                    diff -= 3
                    made_change = True
                if v == 10 and current_counts[10] > 0 and diff >= 3:
                    current_counts[10] -= 1
                    current_counts[5] += 1
                    current_counts[3] += 1
                    current_counts[1] += 2
                    diff -= 3
                    made_change = True
                if v == 10 and current_counts[10] > 0 and diff >= 1:
                    current_counts[10] -= 1
                    current_counts[5] += 2
                    diff -= 1
                    made_change = True
                if v == 5 and current_counts[5] > 0 and diff >= 4:
                    current_counts[5] -= 1
                    current_counts[1] += 5
                    diff -= 4
                    made_change = True
                if v == 5 and current_counts[5] > 0 and diff >= 2:
                    current_counts[5] -= 1
                    current_counts[3] += 1
                    current_counts[1] += 2
                    diff -= 2
                    made_change = True
                if v == 3 and current_counts[3] > 0 and diff >= 2:
                    current_counts[3] -= 1
                    current_counts[1] += 3
                    diff -= 2
                    made_change = True
            # we are done, early exit
            if diff == 0:
                break
            # prevent infinite loops
            if not made_change:
                break

        # check location count matches
        total_items = sum(current_counts.values())
        assert total_items <= self.options.xp_item_count, f"Impossible to distribute xp items with current constraints. off by {total_items - self.options.xp_item_count} items"
        # check xp count matches
        total_xp = sum([k * v for k, v in current_counts.items()])
        assert total_xp == self.options.xp_count, f"Impossible to distribute xp items with current constraints. off by {sum([k*v for k,v in current_counts.items()]) - self.options.xp_count} xp"
        # logger.debug(f"calculated item fill: {current_counts}, {self.options.xp_count}->{total_xp}, {self.options.xp_item_count}->{total_items}")
        # vanilla_proportions = {10:20/134, 5:4/134, 3:15/134, 1:95/134}
        # new_proportions = {k:v/self.options.xp_item_count for k,v in current_counts.items()}
        # logger.debug(f"vanilla proportions: {vanilla_proportions}, new proportions: {new_proportions}")

        xp_items = [xp_value_to_name[xp_value] for xp_value, amount in current_counts.items() for _ in range(amount)]

        return xp_items

    def get_items(self):
        crank_items: list[str] = [item_names.CrankMonsterPark] + \
            [item_names.CrankHollowElevator] + \
            [item_names.CrankHollowZooWall] + \
            [item_names.CrankAnxietyTower] if self.options.cranksanity else []
        rat_items: list[str] = [item_names.Rat] * 6 if self.options.ratsanity else []
        fish_items: list[str] = [item_names.Fish] * 3 if self.options.fishsanity else []
        move_items: list[str] = [item_names.Punch, item_names.Climb, item_names.Slam, item_names.Headbutt, item_names.WallJump, item_names.Crouch] if self.options.movesanity else []
        xp_items: list[str] = self.get_xp_items()
        itempool: list[str] = \
            [item_names.Drill] + \
            [item_names.FallWarp] + \
            xp_items + \
            [item_names.BottleCap] * 5 + \
            [item_names.MegaDreamSoda] * 2 + \
            crank_items + \
            [item_names.VoidScrew] * 11 + \
            [item_names.TrashCan] * 8 + \
            [item_names.DiscoBall] * 5 + \
            [item_names.CheeseGrater] + \
            [item_names.MetalWorm] + \
            rat_items + \
            fish_items + \
            move_items

        # fill rest with junk
        junk: int = len(self.multiworld.get_unfilled_locations(self.player)) - len(itempool)
        assert junk >= 0, f"[Corn Kidz 64 - {self.multiworld.get_player_name(self.player)}] Generated with too many items ({-junk}). Please tweak your settings to include more location with possible filler items."
        trap: int = round(junk * (self.options.trap_percentage / 100))
        filler: int = junk - trap
        # logger.info(f"[Corn Kidz 64 - {self.multiworld.get_player_name(self.player)}] junk: {junk} -> filler {filler} - trap {trap}")
        itempool += [self.random.choice(get_trap_item_names()) for _ in range(trap)]
        itempool += [self.random.choice(get_filler_item_names()) for _ in range(filler)]

        return list(map(lambda name: self.create_item(name), itempool))

    def create_item(self, name: str) -> Item:
        item_id = self.item_name_to_id[name]
        assert item_id - BaseId >= 0, f"{name} doesn't have a valid id: {item_id - BaseId}"
        assert (item_id - BaseId) < len(item_table), f"{name} doesn't have a valid id: {item_id - BaseId} {len(item_table)}"
        item_data = item_table[item_id - BaseId]
        classification = item_data.classification
        if name in xp_name_to_value.keys():
            if self.xp_counter >= self.xp_required:
                classification = ItemClassification.useful
            self.xp_counter += xp_name_to_value[name]
        elif name == item_names.MegaDreamSoda:
            if not self.options.achievementsanity or not self.is_first_mega_soda:
                classification = ItemClassification.useful
            self.is_first_mega_soda = False
        if self.options.accessibility == Accessibility.option_minimal:
            if name == item_names.CrankAnxietyTower:
                 # Anxiety tower crank is filler on non-anxiety/god runs
                 if self.options.goal <= Goal.option_tower:
                     classification = ItemClassification.filler
            elif name == item_names.VoidScrew:
                 # Void screws are useless on non-god runs
                 if self.options.goal <= Goal.option_anxiety:
                     classification = ItemClassification.filler
        # Todo: adjust based on options
        item = CornKidzItem(name, classification, item_id, self.player)
        return item

    def create_items(self):
        self.multiworld.itempool += self.get_items()

    def set_rules(self):
        def test_location(location_data: CK64LocationData, state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options) -> bool:
            res = True
            if location_data.rules:
                res = any(all(rules_to_func[_and](state, world, player, options) for _and in _or) for _or in location_data.rules)
            return res

        def test_entrance(entrance_data: CK64EntranceData, state: CollectionState, world: MultiWorld, player: int, options: CornKidz64Options) -> bool:
            res = True
            if entrance_data.rules:
                res = any(all(rules_to_func[_and](state, world, player, options) for _and in _or) for _or in entrance_data.rules)
            return res

        # Add location rules.
        for i, location_data in enumerate(location_table):
            if location_data in self.excluded_locations:
                continue
            location = self.multiworld.get_location(location_data.name, self.player)
            location.access_rule = lambda state, _i=i, mw=self.multiworld, player=self.player, _options=self.options: test_location(location_table[_i], state, mw, player, _options)

        # Add entrance rules.
        for i, region_data in enumerate(region_table):
            for o, entrance_data in enumerate(region_data.connects_to):
                entrance_name = f"{region_data.name} -> {entrance_data.target}"
                entrance = self.multiworld.get_entrance(entrance_name, self.player)
                entrance.access_rule = lambda state, _i=i, _o=o, mw=self.multiworld, player=self.player, _options=self.options: test_entrance(region_table[_i].connects_to[_o], state, mw, player, _options)
                for condition in entrance_data.indirect_conditions:
                    self.multiworld.register_indirect_condition(self.multiworld.get_region(condition, self.player), entrance)

    def create_event(self, event: str, progression: bool = True):
        return CornKidzItem(event, ItemClassification.progression if progression else ItemClassification.filler, None, self.player)

    def create_regions(self):
        # Create all regions.
        regions: dict[str, Region] = {}
        for region_data in region_table:
            region = Region(region_data.name, self.player, self.multiworld)
            regions[region_data.name] = region
            self.multiworld.regions.append(region)

        # Create all entrances.
        for region_data in region_table:
            parent_region = regions[region_data.name]
            for entrance_data in region_data.connects_to:
                entrance_name = f"{region_data.name} -> {entrance_data.target}"
                child_region = regions[entrance_data.target]
                parent_region.connect(child_region, entrance_name)

        # Create all locations.
        placed_goal = False
        self.excluded_locations = []
        for i, location_data in enumerate(location_table):
            if (location_data.name in achievement_locations and not self.options.achievementsanity) or \
                    (location_data.name in rat_locations and not self.options.ratsanity) or \
                    (location_data.name in fish_locations and not self.options.fishsanity) or \
                    (location_data.name in crank_locations and not self.options.cranksanity):
                self.excluded_locations.append(location_data)
                continue

            region = regions[location_data.region]
            location_id = None if location_data.name in locked_locations else loc_name_to_id[location_data.name]
            location = CornKidzLocation(self.player, location_data.name, location_id, region)
            region.locations.append(location)

            if location_data.name == goal_locations[self.options.goal]:
                self.goal_name = location_data.name
                location.place_locked_item(self.create_event(self.goal_name))
                self.multiworld.completion_condition[self.player] = lambda state, _i=i: state.has(self.goal_name, self.player)
                placed_goal = True
            elif location_data.name in locked_locations:
                location.place_locked_item(self.create_event(location_data.name, False))

        if not placed_goal:
            raise Exception(f"[Corn Kidz 64 - {self.multiworld.get_player_name(self.player)}] "
                            f"Goal could not be placed properly. This game will not generate.")

    def fill_slot_data(self):
        return {
            "version": ".".join(map(str, ck64_version)),
            "goal": self.options.goal.value,
            "xp_count": self.options.xp_count.value,
            "xp_item_count": self.options.xp_item_count.value,
            #"max_hp": self.options.max_hp.value,
            "cranksanity": self.options.cranksanity.value,
            "ratsanity": self.options.ratsanity.value,
            "fishsanity": self.options.fishsanity.value,
            "achievementsanity": self.options.achievementsanity.value,
            "movesanity": self.options.movesanity.value,
            "trap_percentage": self.options.trap_percentage.value,
            "open_wollows_hollow": self.options.open_wollows_hollow.value,
            "death_link": self.options.death_link.value,
        }

    @staticmethod
    def interpret_slot_data(slot_data: dict):
        #TODO: version check?
        return slot_data

    def apply_options_from_slot_data(self, slot_data: dict):
        for k, v in slot_data.items():
            if hasattr(self.options, k):
                option = getattr(self.options, k)
                if option.value != v:
                    option.value = v

    def write_spoiler(self, spoiler_handle: TextIO) -> None:
        pass

    def generate_output(self, output_directory: str) -> None:
        # import Utils
        # Utils.visualize_regions(self.get_region(region_names.Menu), f'{output_directory}/{self.multiworld.get_out_file_name_base(self.player)}.puml')
        # ToDo: remove; dev only
        # TAB = '    '
        # with open(f'{output_directory}/LocationMappingDump.cs', 'w') as f:
        #     lines = [f'{TAB}public static readonly Dictionary<long, int> APLocIdToSaveItemId = new()', f'{TAB}{{']
        #     for i, loc in enumerate(location_table):
        #         if loc.type == CornKidzLocationType.SAVEITEM:
        #             lines += [f'{TAB * 2}{{ BaseID + {i}, {loc.game_id} }}, //{loc.name}']
        #     lines += [f'{TAB}}};', '']
        #     lines += [f'{TAB}public static readonly Dictionary<long, int> APLocIdToUpgradeId = new()', f'{TAB}{{']
        #     for i, loc in enumerate(location_table):
        #         if loc.type == CornKidzLocationType.UPGRADE:
        #             lines += [f'{TAB * 2}{{ BaseID + {i}, {loc.game_id} }}, //{loc.name}']
        #     lines += [f'{TAB}}};', '']
        #     lines += [f'{TAB}public static readonly Dictionary<long, int> APLocIdToAchievementId = new()', f'{TAB}{{']
        #     for i, loc in enumerate(location_table):
        #         if loc.type == CornKidzLocationType.ACHIEVEMENT:
        #             lines += [f'{TAB * 2}{{ BaseID + {i}, {loc.game_id} }}, //{loc.name}']
        #     lines += [f'{TAB}}};', '']
        #     lines += [f'{TAB}public static readonly Dictionary<long, int> APLocIdToSwitchId = new()', f'{TAB}{{']
        #     for i, loc in enumerate(location_table):
        #         if loc.type == CornKidzLocationType.SWITCH:
        #             lines += [f'{TAB * 2}{{ BaseID + {i}, {loc.game_id} }}, //{loc.name}']
        #     lines += [f'{TAB}}};', '']
        #     lines += [f'{TAB}public static readonly Dictionary<long, int> APLocIdToRatIndex = new()', f'{TAB}{{']
        #     j = 0
        #     for i, loc in enumerate(location_table):
        #         if loc.type == CornKidzLocationType.RAT:
        #             lines += [f'{TAB * 2}{{ BaseID + {i}, {j} }}, //{loc.name}']
        #             j += 1
        #     lines += [f'{TAB}}};', '']
        #     lines += [f'{TAB}public static readonly Dictionary<long, string> APLocIdToString = new()', f'{TAB}{{']
        #     for i, loc in enumerate(location_table):
        #         if loc.type == CornKidzLocationType.TEXT:
        #             lines += [f'{TAB * 2}{{ BaseID + {i}, "{loc.text}" }}, //{loc.name}']
        #     lines += [f'{TAB}}};', '']
        #     f.write('\n'.join(lines))
        pass
