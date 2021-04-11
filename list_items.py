from kivymd.uix.list import TwoLineAvatarIconListItem, ILeftBodyTouch, IRightBodyTouch
from kivymd.uix.selectioncontrol import MDCheckbox, MDSwitch
from kivy.properties import StringProperty


class ListItemWithCheckbox(TwoLineAvatarIconListItem):
    pass


class LeftCheckbox(ILeftBodyTouch, MDCheckbox):
    pass


class ListItemWithToggle(TwoLineAvatarIconListItem):
    icon = StringProperty()


class RightToggle(IRightBodyTouch, MDSwitch):
    pass
