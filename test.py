from kivy.garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
# from kivy.garden.mapview import MapMarkerPopup
from mapmarker import MapMarker


class MapViewClass(MapView):
    getting_marker_timer = None

    def start_getting_markers_in_fov(self):
        #After one secopnd, start gettiing markers in field of view
        try:
            self.getting_marker_timer.cancel()
        except:
            pass

        self.getting_marker_timer = Clock.schedule_once(self.get_markers_in_fov, 1)

    def get_markers_in_fov(self, *args):
        #get reference to main app and the database cursor
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        app = App.get_running_app()

        # This code is specific for markers ==  markets
        sql_statement = "SELECT * FROM markets WHERE x > %s AND x < %s AND y > %s AND y < %s "%(min_lon, max_lon, min_lat, max_lat)
        app.cursor.execute(sql_statement)
        markets = app.cursor.fetchall()
        
        for market in markets:
            self.add_marker(market)

    def add_marker(self, market):
        # create MarketMarker
        lat, lon = market[21], market[20]
        print(f"Lat: {lon} and Lon: {lon}")
        marker = MapMarker(lat=lat, lon=lon)
        print(marker)

        # Add the MapMarker to the map
        self.add_widget(marker)


        # keep track of the marker's name
