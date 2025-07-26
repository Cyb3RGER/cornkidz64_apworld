from . import CornKidzTestBase
from .. import CornKidz, crank_locations, rat_locations, fish_locations, achievement_locations
from ..options import XPCount, XPItemCount
from ..constants import location_names

class TestOpenModeOffAccess(CornKidzTestBase):
    options = {
        "open_mode": "false",
    }

    def test_open_mode_access(self) -> None:
        if not isinstance(self.world, CornKidz):
            return

        self.assertFalse(self.multiworld.state.can_reach(location_names.CubeHollowBridge1, "Location", self.player))

class TestOpenModeOnAccess(CornKidzTestBase):
    options = {
        "open_mode": "true",
    }

    def test_open_mode_access(self) -> None:
        if not isinstance(self.world, CornKidz):
            return

        self.assertTrue(self.multiworld.state.can_reach(location_names.CubeHollowBridge1, "Location", self.player))


class TestSanityOptionExcludes(CornKidzTestBase):
    options = {
        "cranksanity": "false",
        "ratsanity": "false",
        "fishsanity": "false",
        "achievementsanity": "false",
    }


    def test_sanity_options_excludes(self) -> None:
        if not isinstance(self.world, CornKidz):
            return

        checks = {
            'cranksanity': crank_locations,
            'ratsanity': rat_locations,
            'fishsanity': fish_locations,
            'achievementsanity': achievement_locations
        }

        for option, locations in checks.items():
            assert self.world.options.__getattribute__(option).value == 0
            for loc in locations:
                with self.assertRaises(KeyError):
                    self.multiworld.get_location(loc, self.player)

class TestXPOptions(CornKidzTestBase):
    def test_all_xp_options(self) -> None:
        for xp_count in range(XPCount.range_start, XPCount.range_end):
            for xp_item_count in range(XPItemCount.range_start, XPItemCount.range_end):
                if not isinstance(self.world, CornKidz):
                    return
                self.world.options.xp_count.value = xp_count
                self.world.options.xp_item_count.value = xp_item_count
                try:
                    self.world.get_xp_items()
                except Exception as e:
                    raise AssertionError(f"failed get_xp_item with the following values:\nxp_count:{xp_count}\nxp_item_count:{xp_item_count}") from e
