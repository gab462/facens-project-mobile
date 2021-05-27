from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatButton
from nav import *
from list_items import *
from plyer import notification


class NotificationButton(MDFillRoundFlatButton):
    def notif(self):
        notification.notify(title='New Notification', message='You just got notified!')
        print("You were notified!")

    pass


class App(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"

        return Builder.load_file('main.kv')


App().run()
