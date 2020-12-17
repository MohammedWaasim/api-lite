import pdb
import os
import yaml
import json

def read_yaml_file(filename,root="testdata"):
    with open(filename) as file:
        data=yaml.full_load(file)
        if(root=="testdata"):
            return data['testdata']
        return data[root]

def read_json_file(filename):
    with open(filename) as file:
        data=json.load(file)
    return data



