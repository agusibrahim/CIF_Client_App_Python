__author__ = 'Don'
# CIF application

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
import requests
from kivy.uix.listview import ListItemButton
from kivy.factory import Factory
import json

class SearchCIF(BoxLayout):
    search_input = ObjectProperty()
    search_results = ObjectProperty()

    def search(self):
        """
        :param apikey: Key used to access the CIF instance
        :param host: Host url of the CIF instance
        :param data: This is the data that the user entered into the search box from the app
        :param array: Contains the splitted json lines from the results of the search
        :param result_data: Contains the referenced json data based on key:value pair called.
        """

        apikey = 'f079399a-28f8-4874-8bc3-b916fb1cd16c'
        host = 'https://cif.laelapssecurity.net/'
        data = self.search_input.text
        headers = {'accept': 'application/json'}
        url = ('%sapi?apikey=%s&q=%s' % (host, apikey, data))
        results = requests.get(url, verify=False, headers=headers)
        array = results.text.split('\n')
        result_data = []
        for result in array:
            if result:
                r = json.loads(result)
                result_data.append("{}, {}, {}, {}, {}, {}".format(r['assessment'], r['description'],r['detecttime'], r['alternativeid'],
                                                  r['address'], r['confidence']))
        self.print_data(result_data)

    def print_data(self, array):
        """
        :param array:   Displays the array passed on from search in the ListView layout in the app
        """
        self.search_results.item_strings = array


class CIFApp(App):
    pass

if __name__ == '__main__':
    CIFApp().run()