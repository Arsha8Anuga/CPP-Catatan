from src.code.main_screen import MainScreenApp
from helper.db import Database

if __name__ == '__main__':
    Database()
    MainScreenApp().run()