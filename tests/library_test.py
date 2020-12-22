import pdb

import pytest

import unittest

from utils.api_helper import ApiHelper
from utils.read_files import *


@pytest.mark.usefixtures("oneTimeSetup")
class LibraryValidation(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.api=ApiHelper(self.apikey)
        self.endpoint = read_yaml_file(self.lib_testdata_file, 'end_points')

    @pytest.mark.regression
    def test_api_reading_book_details(self):
        print("inside lib_test test_reading_book_details method")
        params={}
        test_data=read_yaml_file(self.lib_testdata_file,'library_data')
        params['AuthorName']=test_data['author']
        url = test_data['base_url'] + self.endpoint['read_api']
        response=self.api.get(url,params)
        exp_result={k:v for k,v in test_data.items() if k!='author' and k!='base_url'}
        results= exp_result in response
        assert results == True

