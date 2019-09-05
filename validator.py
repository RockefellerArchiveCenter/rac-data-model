import argparse
import json
from jsonschema import validate
import os

SCHEMA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'schema.json')


class Validator:
    def __init__(self, instance_path):
        print(SCHEMA_PATH)
        if not os.path.isfile(instance_path):
            raise Exception("Instance file does not exist.")
        if not os.path.isfile(SCHEMA_PATH):
            raise Exception("Schema file does not exist.")
        self.instance_path = instance_path

    def json_from_file(self, path):
        with open(path, 'r') as jf:
            return json.load(jf)

    def validate(self):
        schema = self.json_from_file(SCHEMA_PATH)
        instance = self.json_from_file(self.instance_path)
        validate(instance=instance, schema=schema)

parser = argparse.ArgumentParser(description='Validates instances against a JSON Schema')
parser.add_argument('instance_path', help='File path of JSON file containing the instance to be validated.')
args = parser.parse_args()

Validator(args.instance_path).validate()
