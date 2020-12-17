import pdb
import unittest
import pytest
from utils.read_files import *
from utils.api_helper import ApiHelper
import os
class PlanetTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        print("class setup")
        self.test_data=read_yaml_file("/Users/mohammedwaasim/Documents/workspace_python/moka/testdata/planet_test_data.yaml","saved_seach")
        self.request_body=read_json_file("/Users/mohammedwaasim/Documents/workspace_python/moka/testdata/payload.json")
        self.api=ApiHelper(os.environ['apikey'])

    def test_create_saved_search(self):
        print("in create saved search")
        uri=self.test_data['uri']
        body=self.request_body['saved_search_create_request']
        body['item_types'] = [self.test_data['item_types']]
        body['name'] = self.test_data['name']
        #body['name']="some junk"
        response = self.api.post(uri,payload=body)
        search_id=response['id']
        print(f"search_id generated is {search_id}")
        assert response['search_type'] =="saved"
        assert response['name']==self.test_data['name']

    def test_update_saved_search(self):
        uri = self.test_data['uri']
        body = self.request_body['saved_search_create_request']
        body['item_types'] = [self.test_data['item_types']]
        body['name'] = self.test_data['name']
        create_response = self.api.post(uri, payload=body)
        search_id = create_response['id']
        print(f"search_id generated is {search_id}")
        assert create_response['search_type'] == "saved"
        assert create_response['name'] == self.test_data['name']
        print("in update saved search")
        url=uri+"/"+search_id
        body['name'] = self.test_data['update_name']
        update_response = self.api.put(url, payload=body)
        assert update_response['id']==create_response['id']
        assert update_response['search_type'] == "saved"
        assert update_response['name'] == self.test_data['update_name']
        print("verify get operation")
        get_response=self.api.get(url)
        assert get_response['id'] == create_response['id']
        assert get_response['search_type'] == "saved"
        assert get_response['name'] == self.test_data['update_name']
        assert get_response['filter']==body['filter']



