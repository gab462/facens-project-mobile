from kivymd.uix.list import TwoLineAvatarIconListItem, ILeftBodyTouch
from kivymd.uix.selectioncontrol import MDCheckbox


class ListItemWithCheckbox(TwoLineAvatarIconListItem):
    pass


class LeftCheckbox(ILeftBodyTouch, MDCheckbox):
    pass
