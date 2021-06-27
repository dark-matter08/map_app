from kivy.garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from mapmarker import MapMarker

class MapViewClass(MapView):
    getting_markers_timer = None
    market_names = []

    def start_getting_markers_in_fov(self):
        # After one second, get the markets in the field of view
        try:
            self.getting_markers_timer.cancel()
        except:
            pass

        self.getting_markers_timer = Clock.schedule_once(self.get_markers_in_fov, 1)

    def get_markers_in_fov(self, *args):
        # Get reference to main app and the database cursor
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        app = App.get_running_app()

        # self.add_widget(MapMarker(lat=33.75, lon=-84.4, source="marker.png"))

        sql_statement = "SELECT * FROM markets WHERE x > %s AND x < %s AND y > %s AND y < %s "%(min_lon, max_lon, min_lat, max_lat)
        app.cursor.execute(sql_statement)
        markets = app.cursor.fetchall()

        for market in markets:
            name = market[1]
            if name in self.market_names:
                continue
            else:
                self.add_market(market)

    def add_market(self, market):
        # Create the MarketMarker
        lat, lon = market[21], market[20]
        # print(f"Lat: {lat} and Lon: {lon}")
        marker = MapMarker(lat=lat, lon=lon, source="marker.png")
        marker.market_data = market
        # Add the MarketMarker to the map
        self.add_widget(marker)

        # Keep track of the marker's name
        name = market[1]
        self.market_names.append(name)






