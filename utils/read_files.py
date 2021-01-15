import pdb
import os
import yaml
import json

def read_yaml_file(filename):
    with open(filename) as file:
        data=yaml.full_load(file)
        return data

def read_json_file(filename):
    with open(filename) as file:
        data=json.load(file)
    return data



