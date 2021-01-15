import inspect
import unittest
import pytest
from utils.read_files import *
from utils.api_helper import ApiHelper
from utils.test_status import TestStatus
from utils import custom_logger as cl
@pytest.mark.usefixtures("oneTimeSetup")
class RapidTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        print("class setup")
        self.rapid_data=read_yaml_file(self.test_data_file_path)['rapid_data']
        self.api=ApiHelper(self.apiRapidKey,self.apiRapidHost)
        self.ts = TestStatus()

    @pytest.mark.run(order=1)
    def test_rapid_country(self):
        uri=self.rapid_data['country_uri']
        resp=self.api.get(uri)
        my_country={}
        for country in resp:
            if(country['name']=="India"):
                my_country['India']=country
        for k,v in my_country['India'].items():
            cl.allurelogs(f"asserting {k} to have {repr(v)}")
            self.ts.mark(my_country['India'][k]==self.rapid_data['india_meta'][k],f"failed bcoz test data"
                f" {self.rapid_data['india_meta'][k]}, did not match with /"
                f"the response value {my_country['India'][k]}")
        self.ts.markFinal(len(my_country['India'].keys())==len(self.rapid_data['india_meta'].keys()),
                          f"faield bcoz the expected and actualy keys count do not match")

    @pytest.mark.run(order=2)
    def test_rapid_currency(self):
        uri=self.rapid_data['currency_uri']
        url=uri.replace("CUR",self.rapid_data['india_meta']['currencies'][0])
        resp = self.api.get(url)
        country_list=[countries['name'] for countries in resp ]
        self.ts.markFinal(self.rapid_data['india_meta']['name'] in country_list,
                          f"Failed as expected country {self.rapid_data['india_meta']['name']}"
                    f" is not in the give list {str(country_list)}")

    @pytest.mark.run(order=3)
    def test_fail_language_validation(self):
        uri = self.rapid_data['language_uri']
        url = uri.replace("LANG", self.rapid_data['india_meta']['languages'][0])
        resp = self.api.get(url)
        country_list = [countries['name'] for countries in resp]
        self.ts.markFinal( self.rapid_data['invalid_country_language'] in country_list,
                          f"Failed as expected country {self.rapid_data['invalid_country_language']}"
                          f" is not in the give list {str(country_list)}")




