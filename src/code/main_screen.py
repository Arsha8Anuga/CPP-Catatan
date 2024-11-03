from os.path import join, dirname
from kivy.lang.Builder import load_file
from kivy.app import App
from kivy.uix.widget import Widget

# class MainScreen(Widget):

#     pass
#   hayya zak
class MainScreenApp(App):
    def build(self):
        
        file_path = join(dirname(__file__),'../pages/collage.kv')
        load_file(file_path)
        return MainScreen()

class MainScreen(Widget):
    pass

class CollageApp(App):
    def build(self):
        return MainScreen()