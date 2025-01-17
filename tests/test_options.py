from . import CornKidzTestBase
from .. import CornKidz
from ..options import XPCount, XPItemCount


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
