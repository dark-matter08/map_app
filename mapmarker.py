from locationpopupmenu import LocationPopupMenu
from kivy.garden.mapview import MapMarkerPopup
from locationpopupmenu import LocationPopupMenu


class MapMarker(MapMarkerPopup):
    market_data = []
    def on_release(self):
        # open up the LocationPopupMenu
        menu = LocationPopupMenu(self.market_data)
        menu.size_hint = [.8,.9]
        menu.border_radius = 12
        menu.radius = [10]
        menu.open()