from helper.router import Router
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.widget import Widget


class MainScreenApp(App):
    def build(self):
        Router.kivyRoute("collage")
        return MainScreen()

class MainScreen(Widget):
    pass

class CollageApp(App):
    def build(self):
        return MainScreen()