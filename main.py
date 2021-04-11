from kivy.lang import Builder
from kivymd.app import MDApp
from nav import ContentNavigationDrawer


class App(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"

        return Builder.load_file('main.kv')



App().run()
