import pdb
import unittest
import pytest
from utils.read_files import *
from utils.api_helper import ApiHelper
from utils.custom_logger import allurelogs as al
@pytest.mark.usefixtures("oneTimeSetup")
class PlanetTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        print("class setup")
        self.test_data=read_yaml_file(self.test_data,"saved_seach")
        self.request_body = read_json_file(self.payload_path)
        self.api=ApiHelper(self.apikey)

    @pytest.mark.run(order=1)
    def test_create_saved_search(self):
        uri=self.test_data['uri']
        body=self.request_body['saved_search_create_request']
        body['item_types'] = [self.test_data['item_types']]
        body['name'] = self.test_data['name']
        response = self.api.post(uri,payload=body)
        search_id=response['id']
        al("successfully created saved search and search id is " + search_id)
        print(f"search_id generated is {search_id}")
        assert response['search_type'] =="saved"
        assert response['name']==self.test_data['name']
        al("successfully verified search name")

    @pytest.mark.run(order=2)
    def test_update_saved_search(self):
        uri = self.test_data['uri']
        body = self.request_body['saved_search_create_request']
        body['item_types'] = [self.test_data['item_types']]
        body['name'] = self.test_data['name']
        create_response = self.api.post(uri, payload=body)
        search_id = create_response['id']
        al("successfully created saved search and search id is " + search_id)

        assert create_response['search_type'] == "saved"
        assert create_response['name'] == self.test_data['name']
        url=uri+"/"+search_id
        body['name'] = self.test_data['update_name']
        update_response = self.api.put(url, payload=body)
        assert update_response['id']==create_response['id']
        assert update_response['search_type'] == "saved"
        assert update_response['name'] == self.test_data['update_name']
        al("successfully updated search name " + update_response['name'])

        get_response=self.api.get(url)
        assert get_response['id'] == create_response['id']
        assert get_response['search_type'] == "saved"
        assert get_response['name'] == self.test_data['update_name']
        assert get_response['filter']==body['filter']
        al("successfully verified updated search name in get api call " + update_response['name'])



