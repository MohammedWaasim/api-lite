
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
        request.cls.test_data=config['planet']['test_data_path']
        request.cls.payload_path=config['planet']['payload_path']
        request.cls.lib_testdata_file = config['Library']["TestData"]
        request.cls.apikey=os.environ['apikey']
    yield
    print("exiting ots")
