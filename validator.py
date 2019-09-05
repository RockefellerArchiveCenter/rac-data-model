import argparse
import json
from jsonschema import validate, exceptions
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
        try:
            v = validate(instance=instance, schema=schema)
            print("Instance {} is valid according to schema {}".format(self.instance_path, SCHEMA_PATH))
        except exceptions.ValidationError as e:
            errors = sorted(v.iter_errors(instance), key=lambda e: e.path)
            for suberror in sorted(error.context, key=lambda e: e.schema_path):
                print(list(suberror.schema_path), suberror.message, sep=", ")

parser = argparse.ArgumentParser(description='Validates instances against a JSON Schema')
parser.add_argument('instance_path', help='File path of JSON file containing the instance to be validated.')
args = parser.parse_args()

Validator(args.instance_path).validate()
