from . import CornKidzTestBase
from ..constants import location_names, region_names, item_names


class TestDogGodAccess(CornKidzTestBase):

    def test_dog_god_access(self) -> None:
        """Test locations that require a sword"""
        #self.collect_all_but(["Dog God"])
        self.collect(self.multiworld.get_items())
        print(self.multiworld.get_items())
        print(self.multiworld.state.count(item_names.VoidScrew, self.player))
        self.assertTrue(self.multiworld.state.has(item_names.VoidScrew, self.player, 11))
        self.assertTrue(self.can_reach_region(region_names.SomeOtherPlace))
        self.assertTrue(self.can_reach_location(location_names.DogGod))