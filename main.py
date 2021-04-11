from kivy.lang import Builder
from kivymd.app import MDApp
from nav import ContentNavigationDrawer


class App(MDApp):
    def build(self):
        return Builder.load_file('nav.kv')


App().run()
