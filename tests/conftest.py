
import configparser
import os
import pdb
import pytest

@pytest.fixture(scope='class')
def oneTimeSetup(request):
    print("in ots")
    config=configparser.ConfigParser()
    config.read('properties.ini')
    if request.cls is not None:
        request.cls.test_data_file_path=config['planet']['test_data_path']
        request.cls.apiRapidKey=os.environ['apiRapidKey']
        request.cls.apiRapidHost=os.environ['apiRapidHost']
    yield
    print("exiting ots")
