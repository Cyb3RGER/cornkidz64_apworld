#ToDo: add typing.Final to all constants
from . import item_names

GameName = "Corn Kidz 64"
# C(orn) K(idz) 64 A P
# 3      11     64 1 16
BaseId = 3116411600

xp_name_to_value = {
    item_names.XPCube: 1,
    item_names.RedScrew: 3,
    item_names.Moth: 5,
    item_names.XPCrystal: 10
}

xp_value_to_name = {v: k for k, v in xp_name_to_value.items()}
