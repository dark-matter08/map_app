from kivymd.app import MDApp
from mapview_file import MapViewClass
import sqlite3
from searchpopupmenu import SearchPopupMenu

class MainApp(MDApp):
    connection = None
    cursor = None
    search_menu = None
    def on_start(self):
        #initialize GPS

        #connect to datatbase
        self.connection = sqlite3.connect("markets.db")
        self.cursor = self.connection.cursor()


        #instantiate search pop up menu
        self.search_menu = SearchPopupMenu()
    pass

MainApp().run()
