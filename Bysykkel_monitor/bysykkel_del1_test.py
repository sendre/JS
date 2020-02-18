import unittest
import bymonitor
import pandas as pd

class TestSum(unittest.TestCase):
    def setUp(self):
        self.id = 'sindre_kodeoppgave-bymonitor'
        self.auto_discovery_url = 'https://gbfs.urbansharing.com/oslobysykkel.no/gbfs.json'
        self.url_404 = 'https://gbfs.urbansharing.com/oslobysykkel.no/b.jn'

    def test_fetch_json_as_dict_correct(self):
        """Tests if the return type from the fetch_json_as_dict function
        is a dictionary when the valid auto discovery url is passed as argument,
        and response:200"""
        ret, status = bymonitor.fetch_json_as_dict(self.auto_discovery_url, self.id)
        self.assertIs(type(ret), dict)
        self.assertEqual(status, 200)

    def test_fetch_json_as_dict_404(self):
        """Tests that the fetch_json_as_dict function returns None and response:404
        if a faulty url is passed as argument"""
        ret, status = bymonitor.fetch_json_as_dict(self.url_404, self.id)
        self.assertIs(ret, None)
        self.assertEqual(status, 404)

    def test_list_stations_correct(self):
        """Tests if the return type from the list_stations function is a pandas
        DataFrame when the valid auto discovery url is passed as argument, and
        response:200"""
        ret, status = bymonitor.list_stations(self.id, self.auto_discovery_url, False)
        self.assertIs(type(ret), pd.DataFrame)
        self.assertEqual(status, 200)

    def test_list_stations_404(self):
        """Tests that the list_stations function returns None and response:404
        if a faulty url is passed as argument"""
        ret, status = bymonitor.list_stations(self.id, self.url_404, False)
        self.assertIs(ret, None)
        self.assertEqual(status, 404)


if __name__ == '__main__':
    unittest.main()
