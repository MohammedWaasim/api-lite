
import configparser
import os
import pdb
import pytest
from utils import custom_logger as cl

@pytest.fixture(scope='class')
def oneTimeSetup(request):
    print("in ots")
    config=configparser.ConfigParser()
    config.read('properties.ini')
    if request.cls is not None:
        request.cls.test_data_file_path=config['planet']['test_data_path']
        cl.allurelogs(f"reading test data from {str(request.cls.test_data_file_path)}")
        request.cls.apiRapidKey=os.environ['apiRapidKey']
        request.cls.apiRapidHost=os.environ['apiRapidHost']
    yield
    print("exiting ots")
