from kivymd.uix.dialog import MDInputDialog
from urllib import parse
from kivy.network.urlrequest import UrlRequest
from kivy.app  import App
import certifi
from kivy.clock import Clock

class SearchPopupMenu(MDInputDialog):
    title = "Search by Address"
    text_button_ok = 'Search'

    def __init__(self):
        super().__init__()
        self.size_hint = [.9, .3]
        self.events_callback = self.callback

    def open(self):
        super().open()
        Clock.schedule_once(self.set_field_focus, 0.5)

    def callback(self, *args):
        address = self.text_field.text
        self.geocode_get_lat_lon(address)
        print(address)

    def geocode_get_lat_lon(self, address):
        app_id = "iEpVjEIo8E9uDXq0a3jy"
        app_code = "52sDaKnghNEIet9hh0ASzw"
        api_key = "CgKwCe5ht2zOBIb0SfGgZzX6HQUEYruQaAzDQUVKgm0"
        google_api_key = "AIzaSyCkf-jwvZ1V0EwSg_SZkJBku4-woyzeLO4"
        address = parse.quote(address)
        url = f"https://geocode.search.hereapi.com/v1/geocode?apiKey={api_key}&q={address}"
        # url = f"https://geocoder.ls.hereapi.com/6.2/geocode.json?apiKey={api_key}&searchtext={address}";
        # url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={google_api_key}"
        # url = "https://geocoder.api.here.com/6.2/geocode.json?searchtext=%s&app_id=%s&app_code=%s"%(address, app_id, app_code)

        UrlRequest(url, on_success=self.success, on_failure=self.failure, on_error=self.error, ca_file=certifi.where())

    def success(self, urlrequest, result):
        print("Success")
        # print(result)
        latitude = result['items'][0]['position']['lat']
        longitude = result['items'][0]['position']['lng']
        print(" ")
        print("===============================================")
        # longitude = result['items'][0]['lng']
        print(f"latitude: {latitude} and longitude: {longitude}")
        app = App.get_running_app()
        mapview = app.root.ids.mapview
        mapview.center_on(latitude, longitude)

    def failure(self, urlrequest, result):
        print("Failure")
        print(result)

    def error(self, urlrequest, result):
        print("Error")
        print(result)
